#!/usr/bin/env python3
"""Small Gate A checks, not a proof or additions to the 272 original controls.

Optional output is exclusive-create. No saved scientific reference is modified.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import unittest

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import airy, ellipkm1

REPORT: dict[str, object] = {}


def opnorm(a: np.ndarray) -> float:
    return float(np.linalg.norm(a, 2))


def torus(n: int) -> np.ndarray:
    shift = np.roll(np.eye(n), 1, axis=0)
    hopping = shift + shift.T
    return 4*np.eye(n*n) - np.kron(hopping, np.eye(n)) - np.kron(np.eye(n), hopping)


def reciprocal_green(e: float) -> complex:
    """Exact square-lattice boundary value; special points use the reciprocal limit."""
    if e in (0., 4., 8.):
        return 0j
    if e < 0:
        z = 4-e
        return complex(-np.pi*z/(2*ellipkm1((-e)*(8-e)/z**2)))
    if e > 8:
        z = e-4
        return complex(np.pi*z/(2*ellipkm1((e-8)*e/z**2)))
    a = (e-4)**2/16
    g = (np.sign(e-4)*ellipkm1(e*(8-e)/16)/(2*np.pi)
         - 1j*ellipkm1(a)/(2*np.pi))
    return 1/g


def tail_data(s: float, u: float, h0: np.ndarray) -> dict[str, np.ndarray | float]:
    q = np.zeros_like(h0); q[0, 0] = 1
    h = h0-(u+(4-u)*s*s)*q
    hp, hpp = -2*(4-u)*s*q, -2*(4-u)*q
    ev, v = np.linalg.eigh(h)
    b = v[:, 0]
    if b[0] < 0:
        b = -b
    p = np.outer(b, b)
    r = (v[:, 1:]/(ev[1:]-ev[0]))@v[:, 1:].T
    bp = -r@hp@b
    pp = np.outer(bp, b)+np.outer(b, bp)
    ep = b@hp@b
    rp = -r@(hp-ep*np.eye(len(b)))@r - r@pp - pp@r
    bpp = -rp@hp@b-r@hpp@b-r@hp@bp
    ppp = np.outer(bpp, b)+np.outer(b, bpp)+2*np.outer(bp, bp)
    k = pp@p-p@pp
    x = r@pp@p+p@pp@r
    xp = rp@pp@p+r@ppp@p+r@pp@pp+pp@pp@r+p@ppp@r+p@pp@rp
    return dict(h=h, p=p, pp=pp, ppp=ppp, r=r, rp=rp, k=k, x=x, xp=xp)


class AmplitudeIdentificationTests(unittest.TestCase):
    def test_normalization_with_residual_minimum(self) -> None:
        e, alpha, u = sp.symbols('e alpha u', real=True)
        g = sp.Function('g')(e)
        p2 = (-1/g-u)/alpha
        # p>0 and p'<0 on the remote negative leg: p|p'|=-(p^2)'/2.
        product = -sp.diff(p2, e)/2
        weight = g**2/(-sp.diff(g, e))
        self.assertEqual(sp.simplify(1/(2*sp.pi*product)-alpha*weight/sp.pi), 0)
        self.assertEqual(sp.diff(sp.diff(p2, e), u), 0)

    def test_exact_airy_fourier_normalization(self) -> None:
        rows = []
        # One-state H0 benchmark; no continuum or threshold-law claim.
        for alpha in (.3, 2.):
            x = 160.
            a, ap, _, _ = airy(-x)
            c = 2*np.pi*alpha**(-1/3)*a
            cp = 2*np.pi*alpha**(-2/3)*ap
            p = alpha**(-1/3)*np.sqrt(x)
            pp = -alpha**(-2/3)/(2*np.sqrt(x))
            z = np.sqrt(p)*c
            dz = np.sqrt(p)*(cp+pp*c/(2*p))
            plus, minus = (z+dz/(1j*p))/2, (z-dz/(1j*p))/2
            predicted = alpha/np.pi*abs(minus)**2
            self.assertLess(abs(predicted-1), 2e-7)
            self.assertAlmostEqual(abs(plus/minus)**2, 1., places=13)
            rows.append(dict(alpha=alpha, normalized_incident_probability=float(predicted),
                             reflected_ratio=float(abs(plus/minus)**2)))
        REPORT['airy_benchmark'] = rows

    def test_retarded_source_has_no_incoming_wave(self) -> None:
        # f(t)=exp(-|t|), q(E)=2/(1+E^2). Exact source convolution, not the trap.
        max_error = 0.
        for e in (.3, 2., 6.):
            for t in (-6., -1., 0., 2., 7.):
                if t <= 0:
                    expected = -1j*np.exp(t)/(1+1j*e)
                else:
                    expected = -1j*np.exp(-1j*e*t)*(1/(1+1j*e)
                        +(1-np.exp((-1+1j*e)*t))/(1-1j*e))
                integrand = lambda s: np.exp(-1j*e*(t-s)-abs(s))
                parts = [(-np.inf, min(t, 0.))] + ([(0., t)] if t > 0 else [])
                integral = sum(quad(lambda s: integrand(s).real, lo, hi, epsabs=2e-11)[0]
                               +1j*quad(lambda s: integrand(s).imag, lo, hi, epsabs=2e-11)[0]
                               for lo, hi in parts)
                max_error = max(max_error, abs(-1j*integral-expected))
            past = abs(-1j*np.exp(-20)/(1+1j*e))
            future_error = abs(np.exp(-20)/(1-1j*e))
            self.assertLess(past, 2.1e-9)
            self.assertLess(future_error, 2.1e-9)
        self.assertLess(max_error, 2e-9)
        REPORT['retarded_convolution_max_error'] = float(max_error)

    def test_lattice_current_and_continuum_weight(self) -> None:
        rows = []
        for u in (0., .4):
            alpha = 1.3
            y = np.array([1.+0j, -.7+0j])
            segments = []
            for high, low in ((10., 8.), (8., 4.), (4., 0.), (0., -2.)):
                def rhs(e: float, state: np.ndarray) -> np.ndarray:
                    p2 = (-reciprocal_green(float(e))-u)/alpha
                    return np.array([state[1], -p2*state[0]])
                sol = solve_ivp(rhs, (high, low), y, method='DOP853',
                                rtol=3e-11, atol=2e-12, dense_output=True)
                self.assertTrue(sol.success, sol.message)
                segments.append((high, low, sol))
                y = sol.y[:, -1]
            # Independently quadrature-evaluate the spectral density times |q|^2.
            integral = 0.
            for high, low, sol in segments:
                if low >= 0 and high <= 8:
                    def weight(e: float) -> float:
                        a = (e-4)**2/16
                        rho = ellipkm1(a)/(2*np.pi**2)
                        source = reciprocal_green(e)*sol.sol(e)[0]
                        return float(rho*abs(source)**2)
                    integral += quad(weight, low, high, epsabs=1e-7, epsrel=2e-10, limit=200)[0]
            current = float(np.imag(np.conj(y[0])*y[1]))
            balance = current+np.pi/alpha*integral
            relative = abs(balance)/max(1., abs(current))
            self.assertLess(current, 0)
            self.assertLess(relative, 2e-8)
            rows.append(dict(minimum=u, current_at_negative_endpoint=current,
                             continuum_weight=integral, relative_flux_defect=relative))
        REPORT['finite_energy_current_check'] = rows

    def test_reciprocal_log_annulus_scaling(self) -> None:
        rows = []
        # The leading coefficient is shared across the cut; the jump is subleading.
        for n in (8, 16, 32, 64):
            maximum = 0.
            for sign in (-1, 1):
                for y in (.55, 1., 1.9):
                    z = sign*y
                    d = 1+n*np.log(2)-np.log(abs(z))+(1j*np.pi if sign > 0 else 0j)
                    f = 1/d
                    f1 = 1/(z*d*d)
                    f2 = -1/(z*z*d*d)+2/(z*z*d**3)
                    scaled = n*n*max(abs(f-1/(n*np.log(2))), abs(f1), abs(f2))
                    maximum = max(maximum, scaled)
            self.assertLess(maximum, 12.)
            rows.append(dict(annulus=n, rescaled_c2_remainder=maximum))
        REPORT['reciprocal_log_annuli'] = rows

    def test_tail_commutator_and_analytic_derivatives(self) -> None:
        h0 = torus(3)
        rows = []
        for u in (0., .4, 1.):
            for s in (1., 2., 4., 8.):
                d = tail_data(s, u, h0)
                defect = opnorm(d['h']@d['x']-d['x']@d['h']-d['k'])
                self.assertLess(defect, 2e-13)
                delta = 2e-5
                plus, minus = tail_data(s+delta, u, h0), tail_data(s-delta, u, h0)
                derivative_error = opnorm((plus['x']-minus['x'])/(2*delta)-d['xp'])
                self.assertLess(derivative_error, 2e-8)
                self.assertLess(opnorm((plus['p']-minus['p'])/(2*delta)-d['pp']), 2e-8)
                rows.append(dict(minimum=u, s=s, commutator_defect=defect,
                                 derivative_error=derivative_error,
                                 scaled_projector_derivative=s**3*opnorm(d['pp']),
                                 scaled_commutator_solution=s**5*opnorm(d['x'])))
        REPORT['finite_tail_algebra'] = rows

    def test_finite_tail_propagator_bound(self) -> None:
        h0 = torus(3)
        u, start, end = .3, 1., 2.
        dstart, dend = tail_data(start, u, h0), tail_data(end, u, h0)
        def integrand(s: float) -> float:
            d = tail_data(s, u, h0)
            return opnorm(d['xp'])+opnorm(d['k'])*opnorm(d['x'])
        integral, qerror = quad(integrand, start, end, epsabs=2e-10, epsrel=2e-10)
        constant = opnorm(dstart['x'])+opnorm(dend['x'])+integral
        rows = []
        for duration in (2., 5.):
            def rhs(s: float, flat: np.ndarray) -> np.ndarray:
                exact, adi = flat.reshape(2, 9, 9)
                d = tail_data(s, u, h0)
                return np.stack((-1j*duration*d['h']@exact,
                    (-1j*duration*d['h']+d['k'])@adi)).ravel()
            initial = np.stack((np.eye(9), np.eye(9))).astype(complex).ravel()
            sol = solve_ivp(rhs, (start, end), initial, method='DOP853',
                            rtol=3e-11, atol=2e-12)
            self.assertTrue(sol.success, sol.message)
            exact, adi = sol.y[:, -1].reshape(2, 9, 9)
            error = opnorm(exact-adi)
            bound = constant/duration
            self.assertLess(error, bound+1e-8)
            self.assertLess(opnorm(adi@dstart['p']-dend['p']@adi), 2e-9)
            self.assertLess(opnorm(exact.conj().T@exact-np.eye(9)), 2e-9)
            rows.append(dict(half_time=duration, propagator_difference=error,
                             commutator_bound=bound, quadrature_error=qerror))
        REPORT['finite_tail_comparison'] = rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error(f'Refusing to overwrite {args.output}')
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(AmplitudeIdentificationTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    REPORT['tests_run'] = result.testsRun
    REPORT['status'] = 'PASS' if result.wasSuccessful() else 'FAIL'
    REPORT['scope'] = 'Algebra and finite diagnostics only; not an all-time scattering proof.'
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8') as stream:
            json.dump(REPORT, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
