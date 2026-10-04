#!/usr/bin/env python3
"""Independent finite audits of the existing logarithmic threshold-return claim.

No previous scientific module is imported. Models with different terminal loads
are boundary-condition diagnostics, not added physical traps or incoming waves.
"""
from __future__ import annotations
import argparse
from functools import lru_cache
import json
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq
from scipy.special import ellipkm1, airye, hankel1, hankel2, h1vp, h2vp, gamma
import sympy as sp
import mpmath as mp

mp.mp.dps=50

def require(ok, message):
    if not ok: raise AssertionError(message)

def enc(z):return [float(np.real(z)),float(np.imag(z))]

def scales(T):
    L=brentq(lambda x:x+.5*np.log(x)-np.log(32*np.sqrt(np.pi)*T),1e-6,1000.,xtol=1e-13)
    return float(L),float(np.sqrt(L/np.pi)/T)

def green(w):
    if w in (0.,4.,8.):raise ValueError('Use reciprocal-resolvent limits at the singular points.')
    if 0<w<8:
        return complex(np.sign(w-4)*ellipkm1(w*(8-w)/16)/(2*np.pi),-ellipkm1((w-4)**2/16)/(2*np.pi))
    a=4-w if w<0 else w-4
    return complex(np.sign(w-4)*2*ellipkm1(w*(w-8)/(w-4)**2)/(np.pi*a))

@lru_cache(maxsize=None)
def full_band(T=100.,upper=12.,load='airy',rtol=5e-11):
    """Physical exact Green function through both band edges and van Hove point."""
    require(T>0 and upper>8,'Positive duration and endpoint beyond the entire band required.')
    alpha=4/T**2;L,es=scales(T)
    def F(w):return 0j if w in (0.,4.,8.) else -1/(alpha*green(w))
    def q(w):return np.sqrt(F(w)+0j)
    def h(w):
        d=abs(w)*1e-4
        return (np.log(q(w-2*d))-8*np.log(q(w-d))+8*np.log(q(w+d))-np.log(q(w+2*d)))/(12*d)
    if load=='airy':
        val=airye((upper-4)/alpha**(1/3));m=complex(val[1]/val[0]/alpha**(1/3))
    elif load=='neumann':m=0j
    elif load=='dissipative_test':m=-3j
    else:raise ValueError(load)
    calls=0;lower=-60*L*es
    for a,b in [(upper,8.),(8.,4.),(4.,0.),(0.,lower)]:
        sol=solve_ivp(lambda w,y:np.array([-F(w)-y[0]**2]),(a,b),[m],method='DOP853',rtol=rtol,atol=rtol*.02,max_step=.08,t_eval=[b])
        require(sol.success,sol.message);m=sol.y[0,-1];calls+=sol.nfev
    z=(m+h(lower)/2)/(1j*q(lower));r=(1+z)/(1-z)
    return dict(T=T,L=L,energy_scale=es,upper_energy=upper,lower_energy=lower,terminal_load=load,
                amplitude=enc(r),probability=float(abs(r)**2),function_evaluations=calls,
                scope='Auxiliary infinite parabola; asymptotic far-energy boundary and finite extraction checked by refinement, not the exact finite-time cycle.')

@lru_cache(maxsize=None)
def log_terminal(L=20.,Bfactor=8.,lower_factor=20.,load='wkb',method='riccati',rtol=3e-11,at_R=False):
    B=Bfactor*L;lower=L**.25 if at_R else -lower_factor*L
    require(L>=10 and B<np.exp(L),'Keep the log model inside its valid diagnostic interval.')
    def D(x):return L-np.log(complex(-x,-0.))
    def F(x):return 0j if x==0 else L/D(x)
    def q(x):return np.sqrt(F(x))
    def h(x):return .5/(x*D(x))
    m=-1j*q(B)-h(B)/2 if load=='wkb' else complex(load)
    require(m.imag<=1e-14,'Only passive terminal impedances in this audit.')
    if method=='riccati':
        y=np.array([m]);rhs=lambda x,y:np.array([-F(x)-y[0]**2])
    elif method=='vector':
        y=np.array([1+0j,m]);rhs=lambda x,y:np.array([y[1],-F(x)*y[0]])
    else:raise ValueError(method)
    segments=[(B,lower)] if at_R else [(B,0.),(0.,lower)]
    calls=0
    for a,b in segments:
        sol=solve_ivp(rhs,(a,b),y,method='DOP853',rtol=rtol,atol=rtol*.01,max_step=.2,t_eval=[b])
        require(sol.success,sol.message);y=sol.y[:,-1];calls+=sol.nfev
    m=y[0] if method=='riccati' else y[1]/y[0]
    r=(m+h(lower)/2+1j*q(lower))/(1j*q(lower)-m-h(lower)/2)
    return dict(L=L,positive_endpoint=B,extraction_point=lower,load=str(load),method=method,
                amplitude=enc(r),squared_modulus=float(abs(r)**2),function_evaluations=calls,
                scope='Local-WKB reflection at R, or return at a common negative extraction point. Terminal loads are mathematical stress tests.')

def test_algebra_and_normalization():
    m,q,h,hp=sp.symbols('m q h hp',nonzero=True)
    r=(m+h/2+sp.I*q)/(sp.I*q-m-h/2)
    dr=sp.diff(r,m)*(-q*q-m*m)+sp.diff(r,q)*h*q+sp.diff(r,h)*hp
    residue=sp.cancel(dr-2*sp.I*q*r-sp.I*(h*h/4-hp/2)*(1+r)**2/(2*q))
    require(residue==0,'Riccati/WKB identity has a sign or factor error.')
    x,L=sp.symbols('x L',positive=True);D=L-sp.log(x)+sp.I*sp.pi;hh=1/(2*x*D)
    res2=sp.cancel(hh*hh/4-sp.diff(hh,x)/2-(1/(4*x*x*D)-3/(16*x*x*D**2)))
    require(res2==0,'WKB defect mismatch.')
    rows=[]
    def g(w):return -2*mp.ellipk(16/(4-w)**2)/(mp.pi*(4-w))
    for T in [30,100]:
        alpha=mp.mpf(4)/T**2
        for energy in ['-0.001','-0.1','-1','-10']:
            w=mp.mpf(energy);G=g(w);gp=mp.diff(g,w)
            pp=mp.sqrt(-1/(alpha*G));pprime=mp.diff(lambda v:mp.sqrt(-1/(alpha*g(v))),w)
            site=G*G/(-gp)
            ratio=(1/(pp*abs(pprime)))/site
            require(abs(ratio-2*alpha)<mp.mpf('1e-45'),'Stationary-phase normalization is not channel symmetric.')
            rows.append(dict(T=T,energy=float(w),site_weight=float(site),normalization_ratio=float(ratio),expected=float(2*alpha)))
    return dict(cases=2+len(rows),symbolic_riccati_residual=str(residue),symbolic_defect_residual=str(res2),normalization=rows,
                scope='Algebraic and static identities; full time-scattering interpretation additionally uses the stated no-incoming-continuum boundary.')

def test_exact_full_band():
    # These older low-energy-boundary values are comparators, not newly fitted references.
    prior={30.:.0347104052,100.:.0271230811}
    rows=[]
    for T in [30.,100.]:
        values=[full_band(T,upper=12.,load=load) for load in ['airy','neumann','dissipative_test']]
        values.append(full_band(T,upper=16.,load='airy',rtol=2e-11))
        spread=max(v['probability'] for v in values)-min(v['probability'] for v in values)
        error=abs(values[0]['probability']-prior[T])
        require(spread<2e-8 and error<2e-8,'Full band changes the predicted auxiliary return.')
        rows.append(dict(T=T,values=values,spread=spread,prior_local_boundary=prior[T],difference_from_prior=error))
    return dict(cases=8,rows=rows,scope='Includes omega=4 singularity, upper band edge, and forbidden positive-energy tail; not merely one absorbing boundary placed near zero.')

def test_passive_boundary_family():
    rows=[]
    loads=['wkb',0.,10.,-10.,-1j,-100j]
    for L in [10.,20.,50.]:
        values=[log_terminal(L=L,load=load) for load in loads]
        ps=[v['squared_modulus'] for v in values];spread=max(ps)-min(ps)
        require(spread<1e-8,'Passive terminal dependence exceeds recorded numerical accuracy.')
        rows.append(dict(L=L,values=values,probability_spread=spread))
    vector=log_terminal(L=20.,load=0.,method='vector')
    riccati=log_terminal(L=20.,load=0.)
    err=abs(vector['squared_modulus']-riccati['squared_modulus'])
    require(err<2e-8,'Vector and logarithmic-derivative formulations disagree.')
    return dict(cases=20,rows=rows,independent_formulation=dict(vector=vector,riccati=riccati,error=err),
                scope='Six stress-test terminations are finite evidence. The all-passive statement follows from the analytic half-plane bound, not sampling.')

def test_finite_passivity_bound():
    rows=[]
    for L in [10.,20.,50.]:
        R=L**.25;B=L*L
        def D(x):return L-np.log(x)+1j*np.pi
        def q(x):return np.sqrt(L/D(x))
        def h(x):return 1/(2*x*D(x))
        def omega(x):return 1/(4*x*x*D(x))-3/(16*x*x*D(x)**2)
        A=quad(lambda x:-q(x).imag,R,B,epsabs=1e-10)[0]
        I=quad(lambda u:abs(omega(R*np.exp(u))/q(R*np.exp(u)))*R*np.exp(u),0,np.log(B/R),epsabs=1e-13)[0]
        bound=4*np.exp(-2*A)+12.5*I
        vals=[log_terminal(L=L,Bfactor=L,load=load,at_R=True) for load in [0.,10.,-1j]]
        biggest=max(np.sqrt(v['squared_modulus']) for v in vals)
        require(biggest<=bound+2e-10,'Explicit passive reflection bound failed.')
        sampled=0.
        for x in [R,np.sqrt(R*B),B]:
            for re in [-100.,-1.,0.,1.,100.]:
                for im in [0.,-1e-6,-1.,-100.]:
                    m=re+1j*im
                    rv=(m+h(x)/2+1j*q(x))/(1j*q(x)-m-h(x)/2)
                    sampled=max(sampled,abs(rv))
        require(sampled<4.,'Half-plane bound diagnostic.')
        require(I<1/(L*R),'Integrated defect does not meet earlier envelope.')
        rows.append(dict(L=L,R=R,B=B,oneway_attenuation=A,integrated_defect=I,
                         amplitude_bound=bound,largest_tested_local_reflection=float(biggest),
                         half_plane_sample_max=sampled,terminations=vals))
    return dict(cases=9,rows=rows,scope='Universal constant is proved by Mobius/half-plane geometry. Sampling only tests the implementation.')

def power_return(sigma,X=25.):
    require(0<sigma<1,'This comparator is passive only in the declared exponent range.')
    s=1/(2+sigma)
    C=s**(2*s)*gamma(1-s)/gamma(1+s)
    m0=-C*np.exp(1j*np.pi*s*(1-sigma))
    sol=solve_ivp(lambda x,y:np.array([y[1],-(-x)**sigma*y[0]]),(0.,-X),[1+0j,m0],method='DOP853',rtol=2e-11,atol=2e-13,max_step=.05,t_eval=[-X])
    require(sol.success,sol.message)
    z=2*s*X**(1/(2*s));root=np.sqrt(X);q=X**(sigma/2)
    basis=np.array([[root*hankel1(s,z),root*hankel2(s,z)],
                    [-hankel1(s,z)/(2*root)-root*h1vp(s,z)*q,-hankel2(s,z)/(2*root)-root*h2vp(s,z)*q]])
    A,B=np.linalg.solve(basis,sol.y[:,-1]);p=float(abs(B/A)**2)
    exact=float(4*np.cos(np.pi/(2+sigma))**2)
    return dict(spectral_power=sigma,numerical_reflection=p,bessel_reflection=exact,error=abs(p-exact))

def test_power_law_comparator():
    rows=[power_return(sigma) for sigma in [.05,.1,.25,.5,.75]]
    require(max(v['error'] for v in rows)<1e-8,'Exact Bessel comparator failed.')
    tangent=[]
    for L in [20,100,500]:
        p=4*np.cos(np.pi/(2+1/L))**2
        tangent.append(dict(L=L,power_comparator=float(p),ratio_to_log_leading=float(4*L*L*p/np.pi**2)))
    require(abs(tangent[-1]['ratio_to_log_leading']-1)<.003,'Marginal tangent coefficient.')
    return dict(cases=len(rows)+len(tangent),power_rows=rows,tangent=tangent,
                scope='Standard Bessel matching comparator, not a new physical model or an attribution of the general spectral-power formula to the time-ramp exponents of Sokolovski-Pons.')


def test_gapless_projection_boundary():
    ratio=mp.mpf(4)
    expected=mp.sqrt(ratio)*mp.log(ratio)/(ratio-1)
    expected_distance=mp.sqrt(1-expected**2)
    def G(w):return -2*mp.ellipk(16/(4-w)**2)/(mp.pi*(4-w))
    rows=[]
    for eta in ['0.001','0.000001','0.0000000001']:
        a=mp.mpf(eta);b=ratio*a
        cross=(-G(-a)+G(-b))/(b-a)
        overlap=cross/mp.sqrt((-mp.diff(G,-a))*(-mp.diff(G,-b)))
        distance=mp.sqrt(1-overlap**2)
        rows.append(dict(binding_energy=float(a),binding_ratio=float(ratio),overlap=float(overlap),
                         projector_distance=float(distance),limiting_overlap=float(expected),limiting_projector_distance=float(expected_distance)))
    require(abs(rows[-1]['projector_distance']-float(expected_distance))<3e-9,'Non-Cauchy projection limit check.')
    return dict(cases=len(rows),rows=rows,scope='A concrete failure of the continuous-projection hypothesis of a gapless adiabatic theorem, not a contradiction to that theorem.')

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path.cwd()/'rerun.json');args=ap.parse_args()
    groups={}
    for name,fn in [('algebra_and_bound_normalization',test_algebra_and_normalization),('full_physical_band',test_exact_full_band),
                    ('passive_boundary_family',test_passive_boundary_family),('finite_passivity_bound',test_finite_passivity_bound),
                    ('power_law_comparator',test_power_law_comparator),('gapless_projection_boundary',test_gapless_projection_boundary)]:
        groups[name]=fn();print('PASS',name,flush=True)
    data=dict(status='PASS',date='2026-10-04',group_count=len(groups),cases=sum(v['cases'] for v in groups.values()),
              environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,mpmath=mp.__version__),
              groups=groups,scope='Author-side analytical-audit diagnostics. No independent review, physical realization, or complete novelty certification.')
    if args.output.resolve()==Path(__file__).with_name('results.json').resolve() and args.output.exists():
        raise ValueError('Do not overwrite the preserved reference; choose a different output path.')
    args.output.parent.mkdir(exist_ok=True,parents=True);args.output.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n');print('WROTE',args.output)
if __name__=='__main__':main()
