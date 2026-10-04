#!/usr/bin/env python3
"""Local 2D threshold: energy ODE, independent time evolution and matching checks.
No previous scout module is imported. J=hbar=1. Numerical checks are not proofs.
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
from scipy.special import ellipkm1, roots_legendre, sici
RHO=1/(4*np.pi)
LAMBDA=32.

def require(ok, message):
    if not ok:raise AssertionError(message)

def scales(T, g0=4.):
    require(T>0 and g0>0,'Positive duration and attraction required.')
    rhs=np.log(LAMBDA*T/np.sqrt(g0*RHO))
    L=brentq(lambda x:x+.5*np.log(x)-rhs,1e-8,max(1000.,2*rhs),xtol=1e-13)
    return float(L),float(np.sqrt(g0*RHO*L)/T)

def green(w):
    """Exact retarded <0|(w-H0+i0)^-1|0> in the square-lattice convention."""
    if w in (0.,4.,8.):raise ValueError('Use a limit at a band singularity.')
    if w<0:return complex(-2*ellipkm1(w*(w-8)/(4-w)**2)/(np.pi*(4-w)))
    if w<8:
        a=(w-4)**2/16;comp=w*(8-w)/16
        return complex(np.sign(w-4)*ellipkm1(comp)/(2*np.pi),-ellipkm1(a)/(2*np.pi))
    return complex(2*ellipkm1(w*(w-8)/(w-4)**2)/(np.pi*(w-4)))

def density(e):return float(ellipkm1((e-4)**2/16)/(2*np.pi**2))

@lru_cache(maxsize=None)
def energy_return(L=10., T=None, kind='log',positive=15.,negative=20.,method='vector',rtol=2e-10,step=.35):
    if T is not None:L,es=scales(T)
    else:es=LAMBDA*np.exp(-L)
    require(L>0 and positive>0 and negative>0,'Invalid parameters.')
    def f(x):
        if x==0.:return 0j
        if kind=='log':return L/(L-np.log(complex(-x,-0.0)))
        if kind=='one_dimensional':return np.sqrt(complex(-x,-0.0))
        if kind=='lattice':return -RHO*L/green(es*x)
        raise ValueError('Unknown model.')
    def q(x):return np.sqrt(f(x))
    def h(x):
        if kind=='log':return .5/(x*(L-np.log(complex(-x,-0.0))))
        if kind=='one_dimensional':return .25/x
        d=abs(x)*2e-4;v=[np.log(q(x+c*d)) for c in [-2,-1,1,2]]
        return (v[0]-8*v[1]+8*v[2]-v[3])/(12*d)
    xp=positive*L;xn=negative*L
    if kind=='lattice':xp=min(xp,2/es)
    if kind=='one_dimensional':xp=positive;xn=negative
    m0=-1j*q(xp)-.5*h(xp)
    if method=='vector':
        y=np.array([1+0j,m0]);rhs=lambda x,y:np.array([y[1],-f(x)*y[0]])
    elif method=='riccati':
        y=np.array([m0]);rhs=lambda x,y:np.array([-f(x)-y[0]**2])
    else:raise ValueError('Unknown formulation.')
    calls=0
    for a,b in [(xp,0.),(0.,-xn)]:
        sol=solve_ivp(rhs,(a,b),y,method='DOP853',rtol=rtol,atol=rtol*.005,max_step=step,t_eval=[b])
        require(sol.success,sol.message);y=sol.y[:,-1];calls+=sol.nfev
    m=y[1]/y[0] if method=='vector' else y[0]
    z=(m+.5*h(-xn))/(1j*q(-xn));prob=float(abs((1+z)/(1-z))**2)
    require(0<=prob<1+1e-8,'Unphysical reflection.')
    return dict(model=kind,half_duration=T,L=float(L),energy_scale=float(es),positive_endpoint=float(xp),negative_endpoint=float(-xn),
                return_probability=prob,probability_times_4L2_over_pi2=float(prob*4*L*L/np.pi**2),
                method=method,rtol=rtol,max_step=step,function_evaluations=calls,
                scope='Auxiliary infinite parabola with numerically refined WKB boundaries, not exact finite endpoints.')

@lru_cache(maxsize=None)
def spectral_grid(n):
    x,w=roots_legendre(n);x=(x+1)/2;w=w/2
    s,c=np.sin(np.pi*x/2),np.cos(np.pi*x/2);e=4*s**4
    mu=w*8*np.pi*s**3*c*ellipkm1((c*c*(1+s*s))**2)/(2*np.pi**2)
    return np.r_[e,8-e],np.sqrt(np.r_[mu,mu])

@lru_cache(maxsize=None)
def time_return(T,beta=1.,n=500,rtol=2e-11):
    """Finite ends +/-beta*T, g=4(t/T)^2; beta=1 is the original ramp."""
    e,v=spectral_grid(n);gstart=4*beta**2
    eta=brentq(lambda h:gstart*np.sum(v*v/(e+h))-1,1e-12,2*gstart+10,xtol=1e-13)
    initial=v/(e+eta);initial/=np.linalg.norm(initial)
    def rhs(t,y):return -1j*(e*y-4*(t/T)**2*v*(v@y))
    s=solve_ivp(rhs,(-beta*T,0.),initial.astype(complex),method='DOP853',rtol=rtol,atol=rtol*.001,t_eval=[0.])
    require(s.success,s.message);y=s.y[:,-1];norm=float(np.vdot(y,y).real)
    require(abs(norm-1)<2e-8,'Norm loss in unitary time propagation.')
    return dict(half_duration_parameter=T,endpoint_multiplier=beta,actual_full_duration=2*beta*T,
                endpoint_attraction=gstart,initial_binding=float(eta),quadrature_nodes=len(e),
                probability=float(abs(y@y)**2),norm=norm,rtol=rtol)

def test_resolvent():
    rows=[]
    for e in [.1,.7,2.,5.,7.7]:
        d=density(e)
        def nonsingular(x):
            if x==e:return -(density(e+1e-6)-density(e-1e-6))/2e-6
            return (density(x)-d)/(e-x)
        edges=sorted([0.,4.,8.,e]);re=d*np.log(e/(8-e))
        for a,b in zip(edges,edges[1:]):re+=quad(nonsingular,a,b,epsabs=2e-10,epsrel=2e-10,limit=150)[0]
        val=green(e);error=abs(val-(re-1j*np.pi*d))
        require(error<2e-8,'Retarded Green sign/convention mismatch.')
        rows.append(dict(energy=e,real=float(val.real),imag=float(val.imag),PV_error=float(error)))
    for e in [-.001,-.1,-1.]:
        val=quad(lambda x:density(x)/(e-x),0,4,epsabs=1e-10)[0]+quad(lambda x:density(x)/(e-x),4,8,epsabs=1e-10)[0]
        require(abs(val-green(e))<2e-9,'Negative resolvent mismatch.')
        rows.append(dict(energy=e,error=float(abs(val-green(e)))))
    weak=[]
    for e in [-1e-2,-1e-5,-1e-8,1e-2,1e-5,1e-8]:
        edge=-RHO*(np.log(LAMBDA)-np.log(complex(-e,-0.0)));weak.append(dict(energy=e,error=float(abs(green(e)-edge))))
    require(weak[2]['error']<1e-8 and weak[-1]['error']<1e-8,'Log-edge approximation.')
    return dict(cases=len(rows)+len(weak),resolvent=rows,edge=weak)

def test_scalar_solvers():
    rows=[]
    for kind,T,L in [('lattice',100.,10.),('lattice',1000.,10.),('log',None,50.),('one_dimensional',None,10.)]:
        options=dict(kind=kind,T=T,L=L)
        if kind=='one_dimensional':options.update(positive=20.,negative=200.)
        a=energy_return(**options);b=energy_return(**options,method='riccati',rtol=8e-11)
        err=abs(a['return_probability']-b['return_probability']);require(err<2e-8,'Riccati/vector mismatch.')
        rows.append(dict(vector=a,riccati=b,difference=err))
    known=float(4*np.cos(2*np.pi/5)**2)
    require(abs(rows[-1]['vector']['return_probability']-known)<1e-7,'Known 38 percent comparator.')
    return dict(cases=2*len(rows)+1,comparisons=rows,known_one_dimensional_limit=known)

def test_original_protocol_and_tails():
    rows=[];inherited={30.:.03580743687624,100.:.02699657990280}
    for T in [30.,100.]:
        values=[time_return(T,beta) for beta in [1.,2.,4.]]
        exact=energy_return(T=T,kind='lattice',negative=60.,positive=20.)
        require(abs(values[0]['probability']-inherited[T])<2e-7,'Original ramp mismatch.')
        last=abs(values[-1]['probability']-exact['return_probability']);first=abs(values[0]['probability']-exact['return_probability'])
        require(last<first/8 and last<1e-5,'Gapped-tail extension did not approach energy ODE.')
        rows.append(dict(T=T,time_domain=values,energy_domain=exact,last_difference=last,original_difference=first))
    return dict(cases=4*len(rows),rows=rows,scope='beta>1 is a tail control, not the original finite protocol.')

def test_asymptotic_coefficient():
    rows=[energy_return(L=L) for L in [10.,20.,50.,100.,200.]]
    ratios=[r['probability_times_4L2_over_pi2'] for r in rows]
    require(all(a<b for a,b in zip(ratios,ratios[1:])) and .97<ratios[-1]<1.01,'Derived coefficient check.')
    ints=[]
    for R in [10.,100.,1000.]:
        value=(2*sici(2*R)[0]+np.pi)/4
        ints.append(dict(cutoff=R,coefficient=float(value),limit=float(np.pi/2),error=float(abs(value-np.pi/2))))
    require(ints[-1]['error']<3e-4,'Finite sine-integral coefficient check.')
    return dict(cases=len(rows)+len(ints),log_equation=rows,coefficient_integrals=ints,
                scope='Coefficient derived analytically, not fitted. Large L is an auxiliary scalar test, not a feasible device duration.')

def test_matching_estimates():
    rows=[]
    for L in [20.,50.,100.,200.]:
        R=L**.25
        def resid(x,positive):
            V=np.log(x)-(1j*np.pi if positive else 0)
            return abs(L/(L-V)-1-V/L)
        central=sum(quad(lambda x:resid(x,pos),0.,R,epsabs=2e-10,limit=150)[0] for pos in [False,True])
        bound=10*(1+R*(1+np.log(R))**2)/L**2;require(central<bound,'Central L1 envelope.')
        def tail(u):
            x=R*np.exp(u);D=L-np.log(x)+1j*np.pi;q=np.sqrt(L/D)
            defect=1/(4*x*x*D)-3/(16*x*x*D*D)
            return abs(defect/q)*x
        integ=quad(tail,0,np.log(L*L/R),epsabs=1e-12)[0];require(integ<1/(L*R),'Outer WKB envelope.')
        attenuation=quad(lambda x:-np.sqrt(L/(L-np.log(x)+1j*np.pi)).imag,R,L*L,epsabs=1e-9)[0]
        require(attenuation>L,'Positive continuum attenuation.')
        rows.append(dict(L=L,R=R,central_L1_residual=central,central_bound=bound,
                         positive_tail_defect=integ,tail_bound=1/(L*R),oneway_attenuation=attenuation))
    return dict(cases=len(rows),rows=rows,scope='Finite diagnostics of matching estimates, not interval proofs.')

def test_boundaries_and_resolution():
    rows=[]
    for kind,T,L in [('lattice',100.,10.),('lattice',1000.,10.),('log',None,100.)]:
        a=energy_return(kind=kind,T=T,L=L)
        b=energy_return(kind=kind,T=T,L=L,positive=20.,negative=40.,rtol=4e-11,step=.2)
        err=abs(a['return_probability']-b['return_probability']);require(err<1e-6,'Endpoint/step refinement.')
        rows.append(dict(base=a,refined=b,absolute_difference=err))
    ref=time_return(30.,beta=2.,n=700,rtol=3e-12);base=time_return(30.,beta=2.)
    err=abs(ref['probability']-base['probability']);require(err<2e-8,'Time quadrature refinement.')
    return dict(cases=2*len(rows)+2,energy_controls=rows,time_control=dict(base=base,refined=ref,difference=err))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path(__file__).with_name('results.json'));a=p.parse_args()
    groups={}
    for name,fn in [('retarded_resolvent',test_resolvent),('scalar_solvers',test_scalar_solvers),
                    ('original_protocol_and_tails',test_original_protocol_and_tails),('asymptotic_coefficient',test_asymptotic_coefficient),
                    ('matching_estimates',test_matching_estimates),('boundaries_and_resolution',test_boundaries_and_resolution)]:
        groups[name]=fn();print('PASS',name,flush=True)
    report=dict(status='PASS',date='2026-10-04',group_count=len(groups),cases=sum(g['cases'] for g in groups.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),groups=groups,
                scope='Author-side finite checks and convergence diagnostics; not independent review, experimental validation, or exhaustive priority.')
    a.output.parent.mkdir(exist_ok=True,parents=True);a.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print('WROTE',a.output)
if __name__=='__main__':main()
