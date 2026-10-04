#!/usr/bin/env python3
"""Single-particle threshold return in a local square-lattice trap.

Standalone diagnostics. No previous scout module is imported. J=hbar=1.
The finite calculations do not prove a large-time two-dimensional asymptotic law.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import ellipk, ellipkm1, roots_legendre, j0


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


@lru_cache(maxsize=None)
def spectrum(n: int = 800, dimension: int = 2) -> tuple[np.ndarray, np.ndarray]:
    """Quadrature of the infinite lattice's local spectral measure, not a box."""
    x, weights = roots_legendre(n)
    x, weights = (x+1)/2, weights/2
    if dimension == 2:
        s, c = np.sin(np.pi*x/2), np.cos(np.pi*x/2)
        lower = 4*s**4
        derivative = 8*np.pi*s**3*c
        # ellipkm1 evaluates K(1-complement) accurately near the middle-band log.
        density = ellipkm1((c*c*(1+s*s))**2)/(2*np.pi**2)
        energies = np.r_[lower, 8-lower]
        measure = np.r_[weights*derivative*density, weights*derivative*density]
    elif dimension == 1:
        energies = 2-2*np.cos(np.pi*x)
        measure = weights
    else:
        raise ValueError('This scout tests dimensions one and two only.')
    return energies, np.sqrt(measure)


def bound_energy(g: float, dimension: int = 2) -> float:
    if g <= 0:
        raise ValueError('Positive attraction required.')
    if dimension == 1:
        return np.hypot(2.,g)-2
    def green(eta: float) -> float:
        complement = eta*(eta+8)/(eta+4)**2
        return 2*ellipkm1(complement)/(np.pi*(eta+4))
    logeta = brentq(lambda x:g*green(np.exp(x))-1,
                    -min(700.,20+4*np.pi/g),np.log(max(10.,2*g)),xtol=2e-13,rtol=2e-14)
    return float(np.exp(logeta))


def initial(energies: np.ndarray, v: np.ndarray, g: float) -> tuple[float, np.ndarray]:
    eta = brentq(lambda e:g*np.sum(v*v/(energies+e))-1, 1e-16, max(20.,2*g), xtol=1e-14)
    b = v/(energies+eta)
    return eta, b/np.linalg.norm(b)


@lru_cache(maxsize=None)
def evolve(T: float, n: int = 800, dimension: int = 2, g: float = 4.,
           minimum: float = 0., rtol: float = 2e-11, atol: float = 3e-14,
           full: bool = False) -> dict:
    if T <= 0 or not 0 <= minimum <= g:
        raise ValueError('Require T>0 and 0<=minimum<=g.')
    energies, v = spectrum(n,dimension)
    eta, b = initial(energies,v,g)
    def rhs(time: float, psi: np.ndarray) -> np.ndarray:
        u = minimum+(g-minimum)*(time/T)**2
        return -1j*(energies*psi-u*v*np.dot(v,psi))
    endpoint = T if full else 0.
    sol = solve_ivp(rhs,(-T,endpoint),b.astype(complex),method='DOP853',
                    rtol=rtol,atol=atol,t_eval=[endpoint])
    require(sol.success, sol.message)
    psi = sol.y[:,-1]
    amplitude = np.vdot(b,psi) if full else np.dot(psi,psi)
    norm = float(np.vdot(psi,psi).real)
    require(abs(norm-1)<2e-8,'Unexpected loss of norm in closed-system calculation.')
    return dict(half_duration=T,full_duration=2*T,nodes=len(energies),quadrature_order=n,
                dimension=dimension,initial_attraction=g,minimum_attraction=minimum,
                initial_binding_energy=eta,return_probability=float(abs(amplitude)**2),
                norm=norm,final_time_of_computation=endpoint,
                midpoint_free_energy=float(np.vdot(psi,energies*psi).real) if not full else None,
                rtol=rtol,atol=atol,full_cycle_explicit=full)


def split_return(T: float, n: int, dt: float) -> dict:
    """Unitary fourth-order composition, independent of adaptive ODE stepping."""
    energies, v = spectrum(n,2)
    _, b = initial(energies,v,4.)
    psi=b.astype(complex);v2=float(v@v)
    steps=int(np.ceil(T/dt));h=T/steps
    a=1/(2-2**(1/3));coefficients=[a,1-2*a,a]
    phases=[np.exp(-.5j*energies*h*c) for c in coefficients]
    for i in range(steps):
        time=-T+i*h
        for c, phase in zip(coefficients,phases):
            duration=c*h
            integrated_g=4*duration*(time*time+time*duration+duration*duration/3)/T**2
            psi*=phase
            psi+=np.expm1(1j*integrated_g*v2)*(v@psi)*v/v2
            psi*=phase
            time+=duration
    return dict(half_duration=T,step=h,nodes=len(energies),
                return_probability=float(abs(psi@psi)**2),norm=float(np.vdot(psi,psi).real))


@lru_cache(maxsize=None)
def real_space(T: float, side: int, full: bool = False) -> dict:
    """Direct local-neighbor evolution on a finite periodic square, not a DOS RHS."""
    k=2*np.pi*np.arange(side)/side
    energies=4-2*np.cos(k[:,None])-2*np.cos(k[None,:])
    eta=brentq(lambda e:4*np.mean(1/(energies+e))-1,1e-15,20,xtol=1e-14)
    b=np.fft.ifft2(1/(energies+eta)).real
    b=(b/np.linalg.norm(b)).ravel()
    def rhs(time: float, state: np.ndarray) -> np.ndarray:
        a=state.reshape(side,side)
        out=4*a-np.roll(a,1,0)-np.roll(a,-1,0)-np.roll(a,1,1)-np.roll(a,-1,1)
        out[0,0]-=4*(time/T)**2*a[0,0]
        return -1j*out.ravel()
    endpoint=T if full else 0.
    sol=solve_ivp(rhs,(-T,endpoint),b.astype(complex),method='DOP853',
                  rtol=2e-11,atol=3e-14,t_eval=[endpoint])
    require(sol.success,sol.message)
    state=sol.y[:,-1];a=state.reshape(side,side)
    far=np.zeros((side,side),bool)
    far[max(0,side//2-2):side//2+3,:]=True
    far[:,max(0,side//2-2):side//2+3]=True
    return dict(half_duration=T,side=side,sites=side*side,
                return_probability=float(abs(np.vdot(b,state) if full else np.dot(state,state))**2),
                norm=float(np.vdot(state,state).real),
                far_boundary_band_probability=float(np.sum(abs(a[far])**2)),
                initial_binding_energy=eta,full_cycle_explicit=full)


def static_checks() -> dict:
    rows=[]
    for dimension in [1,2]:
        e,v=spectrum(800,dimension)
        targets=[1.,2.*dimension,4.*dimension**2+2.*dimension]
        moments=[float(np.dot(v*v,e**p)) for p in range(3)]
        require(max(abs(a-b) for a,b in zip(moments,targets))<3e-9,'Spectral moment mismatch')
        for time in [.1,1.,5.]:
            val=np.dot(v*v,np.exp(-1j*e*time))
            exact=np.exp(-2j*dimension*time)*j0(2*time)**dimension
            err=float(abs(val-exact));require(err<1e-9,'Clean return kernel mismatch')
            rows.append(dict(dimension=dimension,time=time,kernel_error=err))
        for g in [2.,4.,6.]:
            eta,b=initial(e,v,g);exact=bound_energy(g,dimension)
            residual=float(np.linalg.norm(e*b-g*v*(v@b)+eta*b))
            require(abs(eta-exact)<1e-9 and residual<1e-11,'Bound eigenstate mismatch')
            rows.append(dict(dimension=dimension,g=g,binding=eta,analytic_binding=exact,residual=residual))
        rows.append(dict(dimension=dimension,moments=moments,targets=targets))
    weak=[]
    for g in [2.,1.,.5,.25]:
        eta=bound_energy(g,2);approx=32*np.exp(-4*np.pi/g)
        weak.append(dict(g=g,binding=eta,weak_coupling_formula=approx,ratio=eta/approx))
    require(abs(weak[-1]['ratio']-1)<1e-10,'Essential weak-binding asymptotic check')
    return dict(cases=len(rows)+len(weak),identities=rows,weak_binding=weak,
                scope='Static formulas are derived from the exact local lattice resolvent; not new weak-binding physics.')


def main_dynamics() -> dict:
    eta=bound_energy(4.,2);g1=float(np.sqrt(eta*(eta+4)))
    rows=[]
    for T in [30.,100.,300.,1000.,3000.]:
        two=evolve(T)
        one=evolve(T,n=600,dimension=1,g=g1)
        require(abs(one['initial_binding_energy']-two['initial_binding_energy'])<1e-9,'Unmatched initial gap')
        rows.append(dict(half_duration=T,square_lattice=two,chain=one))
    p=[r['square_lattice']['return_probability'] for r in rows]
    require(all(a>b for a,b in zip(p,p[1:])), 'Recorded sweep sequence is not decreasing')
    known=float(4*np.cos(2*np.pi/5)**2)
    require(abs(rows[-1]['chain']['return_probability']-known)<5e-6,'Known one-dimensional limit comparator')
    return dict(cases=2*len(rows),matched_initial_binding=eta,one_dimensional_attraction=g1,
                one_dimensional_known_limit=known,rows=rows,
                scope='Finite-duration results. Decreasing sampled values are not a monotonicity or infinite-time theorem for two dimensions.')


def numerical_controls() -> dict:
    rows=[]
    # Grid checks include the logarithmic van Hove singularity as well as the threshold.
    for T in [100.,1000.,3000.]:
        base=evolve(T)
        coarse=evolve(T,n=400)
        fine=evolve(T,n=1200)
        delta=abs(base['return_probability']-fine['return_probability'])
        require(delta<3e-7,'Quadrature refinement did not converge at the stated tolerance')
        rows.append(dict(test='quadrature',half_duration=T,coarse=coarse,base=base,fine=fine,base_fine_difference=delta))
    tight=evolve(1000.,n=1000,rtol=2e-12,atol=2e-15)
    delta=abs(tight['return_probability']-evolve(1000.)['return_probability'])
    require(delta<5e-8,'Tighter integration changed displayed scientific scale')
    rows.append(dict(test='tighter_integration',tight=tight,base_difference=delta))
    for T in [10.,100.]:
        base=evolve(T,n=600)
        splits=[split_return(T,600,h) for h in [.05,.025,.0125]]
        errs=[abs(x['return_probability']-base['return_probability']) for x in splits]
        require(errs[-1]<1e-8 and errs[-1]<errs[0]/30,'Independent fourth-order stepping mismatch')
        rows.append(dict(test='unitary_split',base=base,splittings=splits,absolute_errors=errs))
    full=evolve(30.,n=600,full=True)
    half=evolve(30.,n=600)
    delta=abs(full['return_probability']-half['return_probability'])
    require(delta<1e-9,'Real time-reflection identity failed')
    rows.append(dict(test='explicit_full_cycle',full=full,half=half,difference=delta))
    return dict(cases=3*3+1+2*4+2,controls=rows,
                scope='Grid/time convergence and distinct stepping algorithms, not a rigorous continuum error bound.')


def coordinate_checks() -> dict:
    rows=[]
    for T,L in [(10.,64),(10.,128),(30.,256)]:
        real=real_space(T,L);spectral=evolve(T,n=1000)
        delta=abs(real['return_probability']-spectral['return_probability'])
        require(delta<2e-8,'Real-space versus spectral-measure mismatch')
        rows.append(dict(real_space=real,spectral=spectral,difference=delta))
    full=real_space(10.,64,True)
    delta=abs(full['return_probability']-real_space(10.,64)['return_probability'])
    require(delta<1e-9,'Full coordinate propagation differs from half-cycle identity')
    return dict(cases=4,comparisons=rows,explicit_full_cycle=full,full_half_difference=delta,
                scope='Finite torus propagation checks the local model and reduction at stated times; not used to infer infinite-time continuum physics.')


def gap_and_size_controls() -> dict:
    residual=[];small=[]
    for T in [30.,100.,300.,1000.]:
        residual.append(evolve(T,n=600,minimum=2.))
        small.append(real_space(T,9))
    require(residual[-1]['return_probability']>.99999,'Gapped control fails to return')
    require(small[-1]['return_probability']>.9999,'Finite-volume adiabatic control fails')
    return dict(cases=8,residual_attraction=residual,residual_binding=bound_energy(2.,2),
                finite_periodic_square=small,
                finite_free_gap=float(4*np.sin(np.pi/9)**2),
                scope='A residual attraction and a fixed finite volume remove the relevant continuum touching. This does not prove the unknown infinite-lattice limit.')


GROUPS={'static_spectrum':static_checks,'matched_dynamics':main_dynamics,
        'numerical_controls':numerical_controls,'coordinate_checks':coordinate_checks,
        'gap_and_finite_size':gap_and_size_controls}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'))
    ap.add_argument('--group',choices=list(GROUPS))
    a=ap.parse_args();chosen={a.group:GROUPS[a.group]} if a.group else GROUPS
    result={}
    for name,fn in chosen.items():
        result[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-04',group_count=len(result),cases=sum(x['cases'] for x in result.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
                groups=result,scope='Author-side finite controls. No proof of a two-dimensional zero-survival or logarithmic asymptotic law is claimed.')
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print('WROTE',a.output)


if __name__=='__main__':main()
