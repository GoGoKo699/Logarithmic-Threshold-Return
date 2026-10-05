#!/usr/bin/env python3
"""Eight small Gate D diagnostics, not an all-size proof or new asymptotic suite.

Run: python tools/test_finite_volume.py --output NEW.json
The optional report is exclusive-create. No original reference is read or changed.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import brentq
from scipy.special import ellipe, ellipkm1, ive

REPORT: dict[str, object] = {}
GAP = 2*np.sqrt(2.)-2
MU = .5
C = 12/(GAP-4*(np.cosh(MU)-1))
D = 4*np.sqrt(2.)*C/GAP
VELOCITY = 4*np.sinh(MU)


def geometry(side: int, periodic: bool) -> tuple[np.ndarray, np.ndarray, int]:
    if side < 3 or side % 2 != 1:
        raise ValueError('Require an odd side of at least three.')
    R = side//2
    sites = [(x,y) for x in range(-R,R+1) for y in range(-R,R+1)]
    indices = {site:i for i,site in enumerate(sites)}
    H = 4*np.eye(side*side)
    for site,i in indices.items():
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            neighbor = (site[0]+dx,site[1]+dy)
            if periodic:
                neighbor = tuple((q+R)%side-R for q in neighbor)
            if neighbor in indices:
                H[i,indices[neighbor]] -= 1
    distances = np.array([abs(x)+abs(y) for x,y in sites])
    return H, distances, indices[(0,0)]


def embedding(n: int, m: int) -> np.ndarray:
    if m < n or m % 2 != 1 or n % 2 != 1:
        raise ValueError('Centered odd squares required.')
    offset = (m-n)//2
    E = np.zeros((m*m,n*n))
    for i in range(n):
        for j in range(n):
            E[(i+offset)*m+j+offset,i*n+j] = 1
    return E


def finite_endpoint(n: int) -> tuple[float, np.ndarray, np.ndarray]:
    k = 2*np.pi*np.arange(n)/n
    energies = 4-2*np.cos(k[:,None])-2*np.cos(k[None,:])
    eta = brentq(lambda x:4*np.mean(1/(energies+x))-1, GAP, 4., xtol=1e-14)
    b = np.fft.fftshift(np.fft.ifft2(1/(energies+eta))).real.ravel()
    return float(eta), b/np.linalg.norm(b), energies


def infinite_data() -> tuple[float, float]:
    def green(eta: float) -> float:
        z = eta+4
        return 2*ellipkm1(eta*(eta+8)/(z*z))/(np.pi*z)
    eta = brentq(lambda a:4*green(a)-1, GAP, 4., xtol=1e-14)
    z = eta+4
    I2 = 2*ellipe(16/(z*z))/(np.pi*eta*(eta+8))
    return float(eta),float(I2)


def infinite_samples(n: int, order: int) -> np.ndarray:
    """Static trapezoidal Fourier quadrature, not a finite-time propagation."""
    eta,I2 = infinite_data()
    k = 2*np.pi*np.arange(order)/order
    energies = 4-2*np.cos(k[:,None])-2*np.cos(k[None,:])
    v = np.fft.fftshift(np.fft.ifft2(1/(energies+eta))).real/np.sqrt(I2)
    center,R = order//2,n//2
    return v[center-R:center+R+1,center-R:center+R+1].ravel()


def state_derivative(H: np.ndarray, origin: int, T: float, u: float,
                     t: float, y: np.ndarray) -> np.ndarray:
    z = H@y
    z[origin] -= (u+(4-u)*(t/T)**2)*y[origin]
    return -1j*z


class FiniteVolumeTests(unittest.TestCase):
    def test_analytic_localization_and_size_margins(self):
        matrix = sp.Matrix([[0,-2],[-2,4]])
        e = 2-2*sp.sqrt(2)
        self.assertEqual(sp.simplify((matrix-e*sp.eye(2)).det()),0)
        cosh_upper = 1+sp.Rational(1,8)+sp.Rational(1,384)/(1-sp.Rational(1,120))
        sinh_upper = sp.Rational(1,2)+sp.Rational(1,48)+sp.Rational(1,3840)/(1-sp.Rational(1,168))
        self.assertLess(cosh_upper,sp.Rational(113,100))
        self.assertLess(sinh_upper,sp.Rational(209,400))
        self.assertLess(sp.Rational(7,5)**2,2)
        self.assertGreater(GAP, .8)
        self.assertLess(4*(np.cosh(.5)-1), .52)
        self.assertGreater(2.25-VELOCITY, .16)
        REPORT['analytic_margins'] = dict(gap_lower_bound=GAP,
            weight_real_part_penalty=4*(np.cosh(.5)-1),
            decay_exponent=2.25-VELOCITY,C_mu=C,D_mu=D,
            basis='two-state Rayleigh bound and rational Taylor-tail majorants')

    def test_weighted_hopping_on_open_and_periodic_geometries(self):
        rows=[]
        for n in (3,5,9):
            for periodic in (False,True):
                H,d,origin=geometry(n,periodic)
                edge = (H==-1)
                self.assertLessEqual(np.max(np.abs(d[:,None]-d[None,:])[edge]),1)
                for mu in (.2,.5,.8):
                    for cap in (1,2*n):
                        w = np.exp(mu*np.minimum(d,cap))
                        K = w[:,None]*H/w[None,:]
                        real = (K+K.T)/2
                        anti = (K-K.T)/(2j)
                        lower = float(np.linalg.eigvalsh(real).min())
                        upper = float(np.max(abs(np.linalg.eigvalsh(anti))))
                        self.assertGreaterEqual(lower,-4*(np.cosh(mu)-1)-2e-13)
                        self.assertLessEqual(upper,4*np.sinh(mu)+2e-13)
                        for U in (0.,4.,-3.):
                            shifted=K.copy();shifted[origin,origin]-=U
                            self.assertTrue(np.array_equal(shifted-shifted.T,K-K.T))
                        rows.append(dict(side=n,periodic=periodic,mu=mu,cap=cap,
                                         real_min=lower,anti_norm=upper))
                if periodic:
                    R=n//2
                    # The wrap edge (R,0) <-> (-R,0) must have equal distance.
                    self.assertEqual(d[(n-1)*n+R],d[R])
        REPORT['weight_matrices']=rows

    def test_heat_kernel_order_and_endpoint_normalization(self):
        eta0,I2=infinite_data()
        self.assertGreaterEqual(eta0,GAP)
        rows=[]
        for n in (3,5,9,17):
            eta,b,energies=finite_endpoint(n)
            H,d,origin=geometry(n,True)
            h=H.copy(); h[origin,origin]-=4
            self.assertLess(np.linalg.norm(h@b+eta*b),2e-13)
            self.assertGreaterEqual(eta,eta0-2e-14)
            self.assertLessEqual(eta,4)
            self.assertGreater(float(b.min()),0.)
            self.assertAlmostEqual(float(np.linalg.norm(b)),1.,places=14)
            self.assertLessEqual(np.linalg.norm(np.exp(MU*d)*b),C)
            kernels=[]
            for t in (.1,1.,5.):
                finite=float(np.mean(np.exp(-t*energies)))
                infinite=float(ive(0,2*t)**2)
                self.assertGreaterEqual(finite,infinite-2e-15)
                kernels.append(dict(time=t,torus=finite,infinite=infinite))
            rows.append(dict(side=n,binding=eta,weighted_norm=float(np.linalg.norm(np.exp(MU*d)*b)),kernels=kernels))
        REPORT['heat_kernel_and_endpoints']=dict(infinite_binding=eta0,I2=I2,finite=rows)

    def test_seam_operator_support_and_corners(self):
        rows=[]
        for n in (3,5,9):
            H,d,_=geometry(n,True); K,_,_=geometry(n+2,False)
            E=embedding(n,n+2); S=K@E-E@H
            R=n//2
            boundary=np.array([abs(x)==R or abs(y)==R for x in range(-R,R+1) for y in range(-R,R+1)])
            self.assertTrue(np.array_equal(S[:,~boundary],np.zeros_like(S[:,~boundary])))
            self.assertTrue(np.array_equal(E.T@E,np.eye(n*n)))
            row=float(np.max(np.sum(abs(S),axis=1)))
            col=float(np.max(np.sum(abs(S),axis=0)))
            self.assertLessEqual(row,4);self.assertLessEqual(col,4)
            weighted=float(np.linalg.norm(S*np.exp(-MU*d)[None,:],2))
            self.assertLessEqual(weighted,4*np.exp(-MU*R)+1e-14)
            rows.append(dict(side=n,row_sum=row,column_sum=col,
                weighted_seam_norm=weighted,bound=4*np.exp(-MU*R)))
        REPORT['one_collar_exact_seam']=rows

    def test_static_energy_shift_and_phase_aligned_state_error(self):
        rows=[]; eta0,_=infinite_data()
        for n in (3,5,9,13):
            eta,b,_=finite_endpoint(n)
            x=infinite_samples(n,128);x2=infinite_samples(n,256)
            refinement=float(np.linalg.norm(x-x2))
            self.assertLess(refinement,3e-14)
            overlap=float(x2@b)
            self.assertGreater(overlap,0)
            self.assertLessEqual(overlap,1+2e-14)
            # The exact infinite norm is one; only the overlap is quadrature.
            err=float(np.sqrt(max(0.,2*(1-overlap))))
            qnorm=float(np.sqrt(max(0.,1-overlap*overlap)))
            H,_,_=geometry(n,True);K,_,_=geometry(n+2,False)
            E=embedding(n,n+2);f=(K@E-E@H)@b
            residual=float(np.linalg.norm(f))
            self.assertLessEqual(qnorm,residual/GAP+2e-11)
            self.assertLessEqual(err,np.sqrt(2)*residual/GAP+2e-11)
            self.assertLessEqual(eta-eta0,residual+2e-13)
            self.assertLessEqual(err,D*np.exp(-MU*(n//2))+2e-11)
            rows.append(dict(side=n,positive_overlap=overlap,state_error=err,
                complement_norm=qnorm,seam_residual=residual,energy_difference=eta-eta0,
                overlap_quadrature_refinement=refinement,
                scope='static infinite Fourier integral sampled at 128 and 256; no time simulation'))
        REPORT['static_state_comparison']=rows

    def test_midpoint_dynamics_and_integrated_seam(self):
        rows=[]
        for n,T,u in ((5,1.,0.),(5,2.,.4),(9,2.,2.)):
            m=n+4
            H,d,o=geometry(n,True);K,_,om=geometry(m,False);E=embedding(n,m)
            _,b,_=finite_endpoint(n)
            end=K.copy();end[om,om]-=4
            vals,vecs=np.linalg.eigh(end);other=vecs[:,0]
            if other[om]<0:other=-other
            S=K@E-E@H
            y0=np.r_[b.astype(complex),other.astype(complex),0j]
            def rhs(t,y):
                small=y[:n*n];large=y[n*n:n*n+m*m]
                return np.r_[state_derivative(H,o,T,u,t,small),state_derivative(K,om,T,u,t,large),np.linalg.norm(S@small)]
            sol=solve_ivp(rhs,(-T,0),y0,method='DOP853',rtol=2e-11,atol=2e-13,dense_output=True)
            self.assertTrue(sol.success,sol.message)
            y=sol.y[:,-1];small=y[:n*n];large=y[n*n:n*n+m*m]
            initial=float(np.linalg.norm(E@b-other));integrated=float(y[-1].real)
            error=float(np.linalg.norm(E@small-large))
            self.assertLessEqual(error,initial+integrated+2e-10)
            self.assertLess(abs(np.linalg.norm(small)-1),2e-10)
            self.assertLess(abs(np.linalg.norm(large)-1),2e-10)
            weighted0=float(np.linalg.norm(np.exp(MU*d)*b))
            for t in np.linspace(-T,0,7):
                norm=float(np.linalg.norm(np.exp(MU*d)*sol.sol(t)[:n*n]))
                self.assertLessEqual(norm,weighted0*np.exp(VELOCITY*(t+T))+2e-9)
            self.assertLessEqual(integrated,4*weighted0*np.expm1(VELOCITY*T)/VELOCITY*np.exp(-MU*(n//2))+2e-10)
            rows.append(dict(torus_side=n,open_comparison_side=m,half_duration=T,minimum=u,
                initial_error=initial,integrated_seam=integrated,midpoint_error=error,
                scope='two finite geometries; open comparison is not an exact infinite propagation'))
        REPORT['short_finite_duhamel_checks']=rows

    def test_transpose_return_with_noncommuting_and_failure_controls(self):
        rows=[]
        for T,u in ((.6,0.),(1.3,.4),(1.3,2.5)):
            H,_,o=geometry(5,True);_,b,_=finite_endpoint(5)
            sol=solve_ivp(lambda t,y:state_derivative(H,o,T,u,t,y),(-T,T),b.astype(complex),
                method='DOP853',rtol=2e-11,atol=2e-13,t_eval=[0,T])
            self.assertTrue(sol.success,sol.message)
            midpoint=complex(sol.y[:,0]@sol.y[:,0]);full=complex(np.vdot(b,sol.y[:,1]))
            self.assertLess(abs(midpoint-full),2e-10)
            rows.append(dict(half_duration=T,minimum=u,midpoint_amplitude=[midpoint.real,midpoint.imag],
                             full_amplitude=[full.real,full.imag],difference=abs(full-midpoint)))
        H,_,o=geometry(3,True);T=.7;u=.2;I=np.eye(9,dtype=complex)
        def h(t):
            z=H.copy();z[o,o]-=u+(4-u)*(t/T)**2;return z
        self.assertGreater(np.linalg.norm(h(-.7)@h(-.2)-h(-.2)@h(-.7)),1.)
        def matrix_rhs(t,y):return (-1j*h(t)@y.reshape(9,9)).ravel()
        left=solve_ivp(matrix_rhs,(-T,0),I.ravel(),method='DOP853',rtol=2e-12,atol=2e-14)
        right=solve_ivp(matrix_rhs,(0,T),I.ravel(),method='DOP853',rtol=2e-12,atol=2e-14)
        self.assertTrue(left.success and right.success)
        V=left.y[:,-1].reshape(9,9);Vp=right.y[:,-1].reshape(9,9)
        self.assertLess(np.linalg.norm(Vp-V.T),3e-11)
        self.assertGreater(np.linalg.norm(Vp-V.conj().T),.1)
        b=np.array([1.,0.]);sx=np.array([[0.,1.],[1.,0.]]);sz=np.diag([1.,-1.]);sy=np.array([[0,-1j],[1j,0]])
        Vm=expm(-.4j*sx);Vp_wrong=expm(-.4j*sz)
        non_even_gap=abs(b@Vp_wrong@Vm@b-(Vm@b)@(Vm@b))
        even_complex_gap=abs(b@expm(-.8j*sy)@b-(expm(-.4j*sy)@b)@(expm(-.4j*sy)@b))
        self.assertGreater(non_even_gap,.1);self.assertGreater(even_complex_gap,.1)
        REPORT['transpose_not_adjoint']=dict(cycles=rows,matrix_transpose_error=float(np.linalg.norm(Vp-V.T)),
            real_but_not_even_failure=float(non_even_gap),even_but_not_real_failure=float(even_complex_gap))

    def test_amplitude_probability_and_uniform_size_assembly(self):
        rng=np.random.default_rng(184)
        for _ in range(20):
            x=rng.normal(size=7)+1j*rng.normal(size=7);x/=np.linalg.norm(x)
            y=rng.normal(size=7)+1j*rng.normal(size=7);y/=np.linalg.norm(y)
            A,B=x@x,y@y;error=np.linalg.norm(x-y)
            self.assertLessEqual(abs(A-B),2*error+1e-14)
            self.assertLessEqual(abs(abs(A)**2-abs(B)**2),4*abs(B)*error+4*error*error+1e-13)
        rho=1/(4*np.pi);gamma=2.25-VELOCITY;rows=[]
        for L in (16.,24.,32.):
            for label,b in (('zero',0.),('interior',.4),('margin',.8),('varying',.8*(1-1/np.sqrt(L)))):
                u=b/(rho*L);T=np.exp(L)*np.sqrt((4-u)*rho*L)/32
                R=int(np.ceil(4.5*T))
                self.assertLessEqual(u,2.)
                self.assertGreaterEqual(T,np.exp(L)*np.sqrt(2*rho*L)/32)
                self.assertGreaterEqual(R,4.5*T)
                # Logarithmic envelope only: do not report underflow as measured zero.
                log_L_error=np.log(L)+np.log(D+4*C)+np.log1p(T)-gamma*T
                self.assertLess(log_L_error,-100)
                rows.append(dict(L=L,b=b,family=label,T=float(T),side=2*R+1,
                    log_upper_bound_on_L_times_state_error=float(log_L_error),
                    scope='evaluation of analytic envelope, not propagation at this duration or size'))
        REPORT['uniform_family_analytic_envelope']=rows


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.output is not None and args.output.exists():parser.error(f'Output already exists: {args.output}')
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(FiniteVolumeTests))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',tests_run=result.testsRun,original_272_controls=False)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as handle:
            json.dump(REPORT,handle,indent=2,sort_keys=True,allow_nan=False);handle.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)

if __name__=='__main__':main()
