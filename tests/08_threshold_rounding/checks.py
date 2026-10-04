#!/usr/bin/env python3
"""Finite depth/volume rounding of the same single-particle local trap.

Own companion model.py only; no predecessor scientific modules imported.
Numerical controls supplement, but do not prove, the analytical joint limit.
"""
from __future__ import annotations
import argparse, json, platform, time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import eigvalsh
from model import continuous, torus, initial, evolve, binding, scales, residual_log, coordinate, barrier_per_time

def require(ok,message):
    if not ok:raise AssertionError(message)

def group_static():
    rows=[]
    for n in [5,7,9,33]:
        e,v=torus(n);a,b=initial(e,v)
        require(abs(v@v-1)<1e-13,'Degeneracy weights')
        require(abs((v*v)@e-4)<1e-12 and abs((v*v)@(e*e)-20)<1e-11,'Finite free moments')
        k=2*np.pi*np.arange(n)/n;full=(4-2*np.cos(k[:,None])-2*np.cos(k[None,:])).ravel()
        direct_eta=scipy.optimize.brentq(lambda z:4*np.mean(1/(full+z))-1,1e-15,20,xtol=5e-15)
        require(abs(a-direct_eta)<1e-12,'Compressed finite spectral measure')
        if n<=9:
            H=np.diag(full)-4*np.ones((n*n,n*n))/(n*n)
            direct=eigvalsh(H,subset_by_index=[0,0])[0]
            require(abs(a+direct)<1e-12,'Dense finite bound energy')
        rows.append(dict(side=n,compressed_states=len(e),binding=a,full_momentum_binding=direct_eta))
    vals=[barrier_per_time(u) for u in [.25,.5,1.,2.]]
    require(abs(vals[0]['ratio']-1)<.02,'Small-minimum barrier action')
    return dict(cases=8,finite_static=rows,barrier_actions=vals,
      scope='Static identities and auxiliary action. The inverse-action time is an asymptotic scale, not a rigorous device threshold or exact loss fit.')

def group_residual_time():
    rows=[]
    for T in [100.,300.,1000.]:
        for u in [0.,.1,.5,1.]:
            a=evolve(T,u);require(abs(a['norm']-1)<2e-8,'Norm');a['scales']=scales(T,u);rows.append(a)
    g=evolve(1000.,2.);require(g['probability']>.99999,'Gapped positive-minimum control')
    baseline=next(a for a in rows if a['T']==100. and a['minimum']==0.)
    require(abs(baseline['probability']-.02699657985)<2e-8,'Preserved touching-model limit')
    return dict(cases=len(rows)+1,rows=rows,gapped_control=g,
                scope='Actual finite-time cycles with endpoint depth 4; not the infinite auxiliary parabola or asymptotic percentage predictions.')

def group_finite_size():
    rows=[]
    for T,n in [(100.,17),(100.,33),(100.,65),(100.,129),(100.,257),(300.,129),(300.,257),(300.,385)]:
        a=evolve(T,.1,n=n,finite=True);ref=evolve(T,.1)
        a['infinite_quadrature_probability']=ref['probability'];a['finite_infinite_difference']=abs(a['probability']-ref['probability']);rows.append(a)
        require(abs(a['norm']-1)<2e-8,'Finite evolution norm')
    require(rows[4]['finite_infinite_difference']<2e-6,'Finite T100 bulk regime')
    require(rows[-1]['finite_infinite_difference']<2e-6,'Finite T300 bulk regime')
    fixed=[evolve(T,.1,n=17,finite=True) for T in [30.,100.,300.,1000.]]
    require(fixed[-1]['probability']>fixed[1]['probability'],'Fixed-box recovery control')
    return dict(cases=len(rows)+len(fixed),residual_minimum=.1,size_rows=rows,fixed_box=fixed,
                scope='Exact finite torus dynamics. No monotonic-size law, fitted sharp size threshold or atom-number-independent finite-box limit is inferred.')

def group_log_limit():
    rows=[residual_log(L,b) for b in [0.,.25,.5] for L in [20.,50.,100.,200.]]
    for b in [0.,.25,.5]:
        sub=[a for a in rows if a['b']==b]
        err=[abs(1-a['scaled_coefficient']) for a in sub]
        require(all(x>y for x,y in zip(err,err[1:])) and err[-1]<.02,'Joint residual coefficient')
    refined=residual_log(50.,.5,Bfactor=12.,lower_factor=50.,rtol=3e-12)
    base=residual_log(50.,.5)
    difference=abs(refined['probability']-base['probability'])
    require(difference<1e-7,'Log-boundary refinement')
    return dict(cases=len(rows)+1,rows=rows,refined=refined,refinement_difference=difference,
                scope='Scaled low-energy logarithmic equation, not huge-duration full lattice simulation. General residual crossover near b=1 is not claimed.')

def group_locality():
    rows=[]
    mu=.5;bound=4*np.sinh(mu);eta=binding(4.)
    require(4*(np.cosh(mu)-1)<eta,'Endpoint exponential weight admissibility')
    for n in [5,7,9]:
        coords=np.arange(n);distance=np.minimum(coords,n-coords)
        d=(distance[:,None]+distance[None,:]).ravel();W=np.exp(mu*d)
        H=np.zeros((n*n,n*n))
        for x in range(n):
            for y in range(n):
                p=x*n+y;H[p,p]=4
                for xx,yy in [((x+1)%n,y),((x-1)%n,y),(x,(y+1)%n),(x,(y-1)%n)]:H[p,xx*n+yy]-=1
        Hw=W[:,None]*H/W[None,:]
        A=(Hw-Hw.T)/(2j)
        worknorm=float(np.max(np.abs(eigvalsh(A))))
        realmin=float(eigvalsh((Hw+Hw.T)/2,subset_by_index=[0,0])[0])
        require(worknorm<=bound+1e-12 and realmin>=-4*(np.cosh(mu)-1)-1e-12,'Weighted hopping inequalities')
        rows.append(dict(side=n,weight=mu,weighted_antihermitian_norm=worknorm,bound=float(bound),symmetric_part_minimum=realmin))
    exponents=[]
    for T in [20.,100.,1000.]:
        n=2*int(np.ceil(4.5*T))+1;R=(n-1)/2
        exponent=float(4*np.sinh(mu)*T-mu*R)
        require(exponent<-.16*T,'Linear-size sufficient family')
        exponents.append(dict(T=T,side=n,bound_exponent=exponent,scope='Exponent in an upper bound with a fixed prefactor, not a simulated return or optimal resource count.'))
    return dict(cases=6,finite_matrix_controls=rows,sufficient_size_examples=exponents,
                scope='Checks of algebraic norm estimates. The written Duhamel argument, not these samples, gives the uniform volume bound.')

def group_independent():
    rows=[]
    for T,u,n,full in [(10.,.3,17,True),(30.,.1,33,False),(100.,.1,65,False)]:
        a=coordinate(T,u,n,full);b=evolve(T,u,n,finite=True)
        err=abs(a['probability']-b['probability']);require(err<2e-9,'Independent coordinate-space evolution')
        rows.append(dict(coordinate=a,spectral=b,probability_difference=err))
    tighter=evolve(300.,.1,n=2400,rtol=2e-12,atol=2e-15)
    delta=abs(tighter['probability']-evolve(300.,.1)['probability'])
    require(delta<3e-8,'Infinite quadrature/tolerance refinement')
    far=evolve(1000.,1.,n=6500,rtol=2e-12,atol=2e-15)
    far_delta=abs(far['probability']-evolve(1000.,1.)['probability'])
    require(far_delta<3e-8,'Longest-time quadrature/tolerance refinement')
    full=evolve(30.,.5,n=600,full=True);half=evolve(30.,.5,n=600)
    diff=abs(full['probability']-half['probability']);require(diff<2e-9,'Full-cycle versus time-reflection identity')
    return dict(cases=6,coordinate_comparisons=rows,infinite_refinement=tighter,refinement_difference=delta,
                longest_time_refinement=far,longest_refinement_difference=far_delta,
                explicit_full_cycle=full,half_cycle_identity_difference=diff,
                scope='Independent coordinate RHS, direct full-cycle propagation and spectral refinement; not an all-time convergence theorem.')

GROUPS={'static_and_rounding_action':group_static,'finite_residual_cycles':group_residual_time,
        'finite_lattice_window':group_finite_size,'residual_logarithmic_limit':group_log_limit,
        'locality_and_joint_limit':group_locality,'independent_evolution_checks':group_independent}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=Path.cwd()/'rerun.json');ap.add_argument('--group',choices=list(GROUPS));args=ap.parse_args()
    if args.output.exists():ap.error('Choose a new output file; references are never overwritten.')
    selected={args.group:GROUPS[args.group]} if args.group else GROUPS
    data={};start=time.monotonic()
    for name,fn in selected.items():
        t0=time.monotonic();data[name]=fn();print('PASS',name,'seconds',round(time.monotonic()-t0,2),flush=True)
    report=dict(status='PASS',date='2026-10-04',group_count=len(data),cases=sum(d['cases'] for d in data.values()),
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),groups=data,
                scope='New author-side finite-depth/volume controls, not independent proof review, an optimized resource theorem or an experimental realization.')
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print('WROTE',args.output,'elapsed',round(time.monotonic()-start,2),flush=True)
if __name__=='__main__':main()
