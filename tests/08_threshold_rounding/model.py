"""Local square-lattice rounding controls. J=hbar=1. No predecessor imports."""
from __future__ import annotations
from functools import lru_cache
import numpy as np
from scipy.integrate import solve_ivp, quad
from scipy.optimize import brentq
from scipy.special import roots_legendre, ellipkm1

@lru_cache(None)
def continuous(n=600):
    x,w=roots_legendre(n);x=(x+1)/2;w=w/2
    s=np.sin(np.pi*x/2);c=np.cos(np.pi*x/2)
    e=4*s**4;deriv=8*np.pi*s**3*c
    rho=ellipkm1((c*c*(1+s*s))**2)/(2*np.pi**2)
    return np.r_[e,8-e],np.sqrt(np.r_[w*deriv*rho,w*deriv*rho])

@lru_cache(None)
def torus(n):
    if n<3:raise ValueError('side must be at least three')
    q=2*np.pi*np.arange(n//2+1)/n
    mult=np.full(len(q),2.);mult[0]=1
    if n%2==0:mult[-1]=1
    e=2-2*np.cos(q)
    a,b=np.triu_indices(len(e))
    weights=mult[a]*mult[b]*np.where(a==b,1,2)/(n*n)
    return e[a]+e[b],np.sqrt(weights)

def initial(e,v,U=4.):
    eta=brentq(lambda a:U*np.sum(v*v/(e+a))-1,1e-16,20,xtol=5e-15)
    b=v/(e+eta);return eta,b/np.linalg.norm(b)

@lru_cache(None)
def evolve(T,minimum=0.,n=None,finite=False,rtol=3e-11,atol=3e-14,full=False):
    if T<=0 or not 0<=minimum<4:raise ValueError('Require T>0 and 0<=minimum<4')
    if n is None:
        if finite:raise ValueError("A finite side length must be explicit")
        n=max(800,int(np.ceil(5*T)))
    e,v=torus(n) if finite else continuous(n)
    eta,b=initial(e,v)
    def rhs(t,y):
        u=minimum+(4-minimum)*(t/T)**2
        return -1j*(e*y-u*v*np.dot(v,y))
    end=T if full else 0.
    sol=solve_ivp(rhs,(-T,end),b.astype(complex),method='DOP853',rtol=rtol,atol=atol,t_eval=[end])
    if not sol.success:raise RuntimeError(sol.message)
    y=sol.y[:,-1];amp=np.vdot(b,y) if full else np.dot(y,y)
    return {'T':float(T),'full_duration':2*float(T),'minimum':minimum,'side' if finite else 'quadrature_order':n,
            'states':len(e),'finite_volume':finite,'initial_binding':eta,'probability':float(abs(amp)**2),
            'norm':float(np.vdot(y,y).real),'rtol':rtol,'atol':atol,'full_cycle':full}

def binding(u):
    if u<=0:return 0.
    def f(logeta):
        eta=np.exp(logeta)
        return u*2*ellipkm1(eta*(eta+8)/(eta+4)**2)/(np.pi*(eta+4))-1
    return float(np.exp(brentq(f,-min(700,4*np.pi/u+20),np.log(20),xtol=1e-13)))

def scales(T,u=0.):
    alpha=(4-u)/T**2;rho=1/(4*np.pi)
    L=brentq(lambda l:l+.5*np.log(l)-np.log(32/np.sqrt(alpha*rho)),1e-6,1000,xtol=1e-13)
    es=np.sqrt(alpha*rho*L)
    return dict(L=L,es=es,b=u*rho*L,alpha=alpha)

@lru_cache(None)
def residual_log(L,b,Bfactor=8.,lower_factor=25.,rtol=2e-11):
    if L<10 or not 0<=b<1:raise ValueError('L>=10 and 0<=b<1')
    B=Bfactor*L;end=-lower_factor*L
    def F(x):
        if x==0:return complex(-b)
        V=np.log(abs(x))-(1j*np.pi if x>0 else 0j)
        return L/(L-V)-b
    def q(x):return np.sqrt(F(x)+0j)
    def h(x):
        V=np.log(abs(x))-(1j*np.pi if x>0 else 0j);D=L-V
        return L/(2*x*D**2*F(x))
    m=-1j*q(B)-h(B)/2
    nfev=0
    for a,c in [(B,0.),(0.,end)]:
        z=solve_ivp(lambda x,y:np.array([-F(x)-y[0]**2]),(a,c),[m],method='DOP853',rtol=rtol,atol=rtol*.02,max_step=.2,t_eval=[c])
        if not z.success:raise RuntimeError(z.message)
        m=z.y[0,-1];nfev+=z.nfev
    z=(m+h(end)/2)/(1j*q(end));r=(1+z)/(1-z)
    return dict(L=L,b=b,probability=float(abs(r)**2),scaled_coefficient=float(4*L*L*(1-b)**2*abs(r)**2/np.pi**2),
                extraction=end,terminal=B,scope='Local logarithmic equation; not full lattice at exponentially large time.')

@lru_cache(None)
def coordinate(T,u,n=33,full=False):
    k=2*np.pi*np.arange(n)/n
    energies=4-2*np.cos(k[:,None])-2*np.cos(k[None,:])
    eta=brentq(lambda a:4*np.mean(1/(energies+a))-1,1e-15,20,xtol=5e-15)
    b=np.fft.ifft2(1/(energies+eta)).real;b=(b/np.linalg.norm(b)).ravel()
    def rhs(t,y):
        p=y.reshape(n,n)
        h=4*p-np.roll(p,1,0)-np.roll(p,-1,0)-np.roll(p,1,1)-np.roll(p,-1,1)
        h[0,0]-=(u+(4-u)*(t/T)**2)*p[0,0]
        return -1j*h.ravel()
    end=T if full else 0.
    sol=solve_ivp(rhs,(-T,end),b.astype(complex),method='DOP853',rtol=1e-11,atol=1e-14,t_eval=[end])
    if not sol.success:raise RuntimeError(sol.message)
    z=sol.y[:,-1];amp=np.vdot(b,z) if full else z@z
    return dict(T=T,minimum=u,side=n,full_cycle=full,probability=float(abs(amp)**2),norm=float(np.vdot(z,z).real))

def barrier_per_time(u):
    """Exact auxiliary forbidden-region action divided by T; not an exact loss law."""
    eta=binding(u)
    def part(v):
        e=eta*np.exp(-v)
        G=2*ellipkm1(e*(e+8)/(e+4)**2)/(np.pi*(e+4))
        return np.exp(-v)*np.sqrt(max(0.,u-1/G))
    val,error=quad(part,0.,80.,epsabs=1e-12,epsrel=2e-11,limit=300)
    exact=eta*val/np.sqrt(4-u)
    asym=eta*u/(4*np.sqrt(4-u))
    return dict(minimum=u,binding=eta,action_per_T=exact,weak_binding_action_per_T=asym,ratio=exact/asym,
                inverse_action_time=1/exact,quadrature_error=error,omitted_integral_bound=float(np.sqrt(u)*np.exp(-80)))
