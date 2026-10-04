#!/usr/bin/env python3
"""Fixed-anisotropy checks of the threshold mechanism; no inherited module imports.

This diagnostic is a scope check, not a new platform or an independent review.
The complete physical model remains one attractive lattice site and one quadratic
round trip. Large L computations solve an auxiliary scalar energy equation only.
"""
from __future__ import annotations
import argparse, json, math, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.special import ellipk, ellipkm1, ellipe, roots_legendre
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise AssertionError(msg)


def edge(ax: float, ay: float) -> tuple[float, float]:
    if min(ax, ay) <= 0:
        raise ValueError('Both hoppings must be strictly positive and fixed.')
    return 1/(4*np.pi*np.sqrt(ax*ay)), 64*ax*ay/(ax+ay)


def resolvent(omega: float, ax: float=1., ay: float=1.) -> complex:
    """Exact physical g in negative energy and below the first positive saddle."""
    s=ax+ay; p=ax*ay
    if omega < 0:
        eta=-omega; d=16*p+eta*(4*s+eta); c=eta*(4*s+eta)/d
        return -2*ellipkm1(c)/(np.pi*np.sqrt(d))
    if omega == 0:
        return complex(-np.inf, -1/(4*np.sqrt(p)))
    if omega >= 4*min(ax,ay):
        raise ValueError('Positive formula is only below the first saddle.')
    c=omega*(4*s-omega)/(16*p)
    return -(ellipkm1(c)+1j*ellipk(c))/(2*np.pi*np.sqrt(p))


def log_derivative_g(omega: float, ax: float, ay: float) -> complex:
    """Exact g'/g; uses a small-c series only for a nonsingular elliptic derivative."""
    s=ax+ay; p=ax*ay
    if omega < 0:
        eta=-omega; d=16*p+eta*(4*s+eta); c=eta*(4*s+eta)/d
        return (4*s+2*eta)*ellipe(1-c)/(2*d*c*ellipkm1(c))
    if not 0 < omega < 4*min(ax,ay):
        raise ValueError('Derivative outside supported energy intervals.')
    c=omega*(4*s-omega)/(16*p); dc=(4*s-2*omega)/(16*p)
    kr=ellipkm1(c);ki=ellipk(c)
    dr=(c*kr-ellipe(1-c))/(2*c*(1-c))
    di=(np.pi/8)*(1+9*c/8+75*c*c/64) if c<1e-5 else (ellipe(c)-(1-c)*ki)/(2*c*(1-c))
    return dc*(dr+1j*di)/(kr+1j*ki)


def scalar(L: float, ax: float=1., ay: float=1.,
           exact: bool=True, upper_factor: float=10., lower_factor: float=30.,
           rtol: float=2e-11, step: float=.25, riccati: bool=True) -> dict:
    rho,lam=edge(ax,ay); estar=lam*np.exp(-L)
    left=-lower_factor*L;right=upper_factor*L
    require(right*estar < 4*min(ax,ay), 'Outer matching sample must lie below the first saddle.')
    def f(x: float) -> complex:
        if x==0:return 0j
        if exact:return -rho*L/resolvent(estar*x,ax,ay)
        return L/(L-np.log(abs(x))+(1j*np.pi if x>0 else 0))
    def h(x: float) -> complex:
        if exact:return -.5*estar*log_derivative_g(estar*x,ax,ay)
        d=L-np.log(abs(x))+(1j*np.pi if x>0 else 0)
        return 1/(2*x*d)
    qr=np.sqrt(complex(f(right)));mr=-1j*qr-h(right)/2
    def rhs(x:float,y:np.ndarray)->np.ndarray:
        return np.array([-f(x)-y[0]*y[0]]) if riccati else np.array([y[1],-f(x)*y[0]])
    y=np.array([mr],complex) if riccati else np.array([1.,mr],complex)
    for a,b in [(right,0.),(0.,left)]:
        sol=solve_ivp(rhs,(a,b),y,method='DOP853',rtol=rtol,atol=rtol*.02,max_step=step)
        require(sol.success,sol.message);y=sol.y[:,-1]
    ml=y[0] if riccati else y[1]/y[0];ql=np.sqrt(complex(f(left)))
    z=(ml+h(left)/2)/(1j*ql);r=(1+z)/(1-z);P=float(abs(r)**2)
    return dict(L=L,ax=ax,ay=ay,exact_local_resolvent=exact,return_probability=P,
                scaled_coefficient=4*L*L*P/(np.pi*np.pi),estar=float(estar),
                upper_physical_energy=float(right*estar),left=left,right=right)


def tests() -> dict:
    groups={}
    stat=[]
    # Independent single-angle integral: integrate ky analytically, kx by quadrature.
    for ax,ay in [(1.,1.),(1.,.5),(1.,.25),(2.,1.),(.4,1.7)]:
        for eta in [.05,.5,2.]:
            direct=quad(lambda k:1/np.sqrt((eta+2*(ax+ay)-2*ax*np.cos(k))**2-(2*ay)**2),
                        0,np.pi,epsabs=2e-12,epsrel=2e-12)[0]/np.pi
            closed=-resolvent(-eta,ax,ay).real
            require(abs(direct-closed)<5e-12,'Closed Green function versus independent momentum integral')
            # Analytic derivative versus real finite difference away from threshold.
            ds=eta*1e-4
            derivative=(np.log(-resolvent(-eta+ds,ax,ay).real)-np.log(-resolvent(-eta-ds,ax,ay).real))/(2*ds)
            predicted=log_derivative_g(-eta,ax,ay)
            require(abs(derivative-predicted)<1e-7*max(1,abs(predicted)),'Negative resolvent derivative')
            stat.append(dict(ax=ax,ay=ay,eta=eta,resolvent=float(closed),integral=float(direct),error=float(abs(direct-closed))))
    groups['exact_green_function']=dict(cases=len(stat),rows=stat)
    print('PASS exact_green_function',flush=True)

    limits=[]
    for ax,ay in [(1.,1.),(1.,.5),(1.,.25),(2.,1.),(.4,1.7)]:
        rho,lam=edge(ax,ay)
        for eta in [1e-5,1e-9,1e-13]:
            g=resolvent(-eta,ax,ay)
            recovered=eta*np.exp(-g.real/rho)
            gp=resolvent(eta,ax,ay)
            require(abs(recovered/lam-1)<5e-5,'Logarithmic cutoff constant')
            require(abs(-gp.imag/(np.pi*rho)-1)<2e-5,'Retarded density coefficient')
            limits.append(dict(ax=ax,ay=ay,eta=eta,rho0=float(rho),Lambda=float(lam),
                               inferred_Lambda=float(recovered),threshold_density_ratio=float(-gp.imag/(np.pi*rho))))
    groups['threshold_constants_and_causality']=dict(cases=len(limits),rows=limits)
    print('PASS threshold_constants_and_causality',flush=True)

    # Fixed endpoint depth and a fully local Hamiltonian, not a separable-potential substitution.
    n=41;T=4.;ax=1.;ay=.5
    q=2*np.pi*np.arange(n)/n
    energies=2*ax*(1-np.cos(q[:,None]))+2*ay*(1-np.cos(q[None,:]))
    flat=energies.ravel();v=np.ones(flat.size)/n
    eta=brentq(lambda eta:4*np.sum(v*v/(flat+eta))-1,1e-12,10.,xtol=1e-14)
    b=v/(flat+eta);b=b/np.linalg.norm(b)
    def momentum_rhs(time,y):
        return -1j*(flat*y-4*(time/T)**2*v*np.dot(v,y))
    m=solve_ivp(momentum_rhs,(-T,0),b.astype(complex),method='DOP853',rtol=3e-11,atol=2e-14)
    require(m.success,m.message)
    bpos=np.fft.ifft2(b.reshape(n,n),norm='ortho')
    def coordinate_rhs(time,y):
        z=y.reshape(n,n)
        hz=2*(ax+ay)*z-ax*(np.roll(z,1,0)+np.roll(z,-1,0))-ay*(np.roll(z,1,1)+np.roll(z,-1,1))
        hz=hz.copy();hz[0,0]-=4*(time/T)**2*z[0,0]
        return -1j*hz.ravel()
    c=solve_ivp(coordinate_rhs,(-T,0),bpos.ravel(),method='DOP853',rtol=3e-11,atol=2e-14)
    require(c.success,c.message)
    pm=float(abs(np.dot(m.y[:,-1],m.y[:,-1]))**2)
    pc=float(abs(np.dot(c.y[:,-1],c.y[:,-1]))**2)
    require(abs(pc-pm)<2e-9,'Finite local coordinate/momentum reduction')
    groups['local_model_reduction']=dict(cases=1,n=n,T=T,ax=ax,ay=ay,
           momentum_return=pm,coordinate_return=pc,difference=abs(pm-pc),scope='Finite moderate-time check, not the asymptotic law.')
    print('PASS local_model_reduction',flush=True)

    rows=[]
    for L in [10.,20.,40.]:
        universal=scalar(L,exact=False)
        for ax,ay in [(1.,1.),(1.,.5),(1.,.25),(2.,1.)]:
            r=scalar(L,ax,ay)
            difference=abs(r['return_probability']-universal['return_probability'])
            bound={10.:1e-4,20.:2e-7,40.:1e-9}[L]
            require(difference<bound,'Fixed-anisotropy local threshold matching')
            rows.append({**r,'log_equation_return':universal['return_probability'],'difference':difference})
    groups['fixed_anisotropy_scope']=dict(cases=len(rows),rows=rows,
          scope='Auxiliary scalar equation with exact lower-edge resolvent. No full real-time simulation at corresponding enormous durations.')
    print('PASS fixed_anisotropy_scope',flush=True)

    ref=scalar(20.,1.,.25)
    refined=scalar(20.,1.,.25,upper_factor=14,lower_factor=40,rtol=7e-12,step=.15)
    vector=scalar(20.,1.,.25,riccati=False)
    require(abs(ref['return_probability']-refined['return_probability'])<2e-8,'Matching boundary refinement')
    require(abs(ref['return_probability']-vector['return_probability'])<2e-8,'First/second order formulations')
    groups['independent_scalar_and_boundary_checks']=dict(cases=2,standard=ref,refined=refined,vector=vector)
    print('PASS independent_scalar_and_boundary_checks',flush=True)
    return groups


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if args.output.exists():raise FileExistsError('Use a new output path; saved scientific references are not overwritten.')
    groups=tests();result=dict(status='PASS',date='2026-10-04',groups=groups,group_count=len(groups),
        case_count=sum(g['cases'] for g in groups.values()),environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        scope='Author-side algebraic and finite numerical checks, not independent review or evidence of a new apparatus.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print('WROTE',args.output,flush=True)

if __name__=='__main__':main()
