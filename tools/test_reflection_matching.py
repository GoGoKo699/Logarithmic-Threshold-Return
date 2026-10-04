#!/usr/bin/env python3
"""Small Gate B identities and finite diagnostics, not all-L proof or peer review.

Run with an optional --output NEW_PATH.json. Output is exclusively created; no
preserved scientific script or reference is read as an update target.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import unittest

import mpmath as mp
import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.special import ellipe, ellipkm1, sici

REPORT: dict[str, object] = {}


def log_data(x: float, L: float) -> tuple[complex, complex, complex, complex]:
    if x == 0:
        raise ValueError('The wave basis is only used away from the origin.')
    d = complex(L-np.log(abs(x)), np.pi if x > 0 else 0.)
    q = np.sqrt(L/d)
    h = 1/(2*x*d)
    omega = 1/(4*x*x*d)-3/(16*x*x*d*d)
    return L/d, q, h, omega


def wave_matrix(x: float, L: float) -> np.ndarray:
    _, q, h, _ = log_data(x, L)
    waves = q**(-.5)*np.exp(np.array([-1j*x, 1j*x]))
    return np.vstack((waves, np.array([-h/2-1j*q, -h/2+1j*q])*waves))


def complex_quad(f, lo: float, hi: float) -> complex:
    return (quad(lambda x: float(np.real(f(x))), lo, hi, epsabs=2e-11,
                 epsrel=2e-11, limit=200)[0]
            +1j*quad(lambda x: float(np.imag(f(x))), lo, hi, epsabs=2e-11,
                     epsrel=2e-11, limit=200)[0])


def negative_green(eps: float) -> tuple[float, float, float]:
    """G, dG/deps, d2G/deps2, with stable complementary elliptic parameter."""
    z, d = 4+eps, eps*(8+eps)
    k = ellipkm1(d/(z*z))
    e = ellipe(16/(z*z))
    return (2*k/(np.pi*z), -2*e/(np.pi*d),
            2/np.pi*(2*z*e/(d*d)-(k-e)/(z*d)))


class ReflectionMatchingTests(unittest.TestCase):
    def test_endpoint_and_reflection_algebra(self) -> None:
        x, v, eta = sp.symbols('x v eta', real=True)
        q = sp.symbols('q', positive=True)
        h, m, hp = sp.symbols('h m hp')
        pmat = sp.Matrix([[sp.exp(-sp.I*x), sp.exp(sp.I*x)],
                          [-sp.I*sp.exp(-sp.I*x), sp.I*sp.exp(sp.I*x)]])
        wmat = sp.Matrix([[sp.exp(-sp.I*x), sp.exp(sp.I*x)],
                          [(-h/2-sp.I*q)*sp.exp(-sp.I*x),
                           (-h/2+sp.I*q)*sp.exp(sp.I*x)]])/sp.sqrt(q)
        conversion = sp.simplify(pmat.inv()*wmat)
        # At fixed endpoints h is separately of order 1/(L R).
        linear = conversion.subs(h, 0).subs(q, sp.sqrt(1+eta*v))
        derivative = linear.diff(eta).subs(eta, 0)
        target = -v/4*sp.Matrix([[0, sp.exp(2*sp.I*x)],
                                 [sp.exp(-2*sp.I*x), 0]])
        self.assertEqual(sp.simplify(derivative-target), sp.zeros(2))
        r = (m+h/2+sp.I*q)/(sp.I*q-m-h/2)
        rp = sp.diff(r, m)*(-q*q-m*m)+sp.diff(r, h)*hp+sp.diff(r, q)*h*q
        omega = h*h/4-hp/2
        self.assertEqual(sp.simplify(sp.factor(
            rp-2*sp.I*q*r-sp.I*omega*(1+r)**2/(2*q))), 0)
        self.assertEqual(sp.limit(r, m, sp.oo), -1)
        # Exact negative-tail integrand after energy-coordinate conversion.
        G, G1, G2 = sp.symbols('G G1 G2', positive=True)
        W, W1, W2 = 1/G, -G1/G**2, 2*G1**2/G**3-G2/G**2
        transformed = 5*W1**2/(16*W**sp.Rational(5, 2))-W2/(4*W**sp.Rational(3, 2))
        self.assertEqual(sp.simplify(transformed-G2/(4*sp.sqrt(G))
                                     +3*G1**2/(16*G**sp.Rational(3, 2))), 0)

    def test_distribution_and_boundary_cancellation(self) -> None:
        rows = []
        for R in (1.7, 3.2, 7.1, 13.):
            integral = (complex_quad(lambda x: np.log(-x)*np.exp(-2j*x), -R, 0.)
                        +complex_quad(lambda x: (np.log(x)-1j*np.pi)*np.exp(-2j*x), 0., R))
            boundary = (np.log(R)-1j*np.pi)*np.exp(-2j*R)-np.log(R)*np.exp(2j*R)
            pv = -2j*sici(2*R)[0]
            causal = -1j*np.pi
            self.assertLess(abs(boundary+2j*integral-pv-causal), 2e-10)
            bulk, basis = -1j*integral/2, -boundary/4
            combined = -(pv+causal)/4
            self.assertLess(abs(bulk+basis-combined), 1e-10)
            rows.append(dict(R=R, bulk=[bulk.real, bulk.imag],
                             endpoint=[basis.real, basis.imag],
                             combined=[combined.real, combined.imag],
                             pv_contribution=[0., float(sici(2*R)[0]/2)],
                             causal_contribution=[0., float(np.pi/4)]))
        REPORT['finite_window_first_order_amplitudes_times_L'] = rows

    def test_central_transfer_in_local_bases(self) -> None:
        rows = []
        for L in (32., 128., 512., 2048.):
            R = L**.25
            y = wave_matrix(R, L)[:, 0]
            def rhs(x: float, state: np.ndarray) -> np.ndarray:
                f = 0j if x == 0 else log_data(x, L)[0]
                return np.array([state[1], -f*state[0]])
            for start, end in ((R, 0.), (0., -R)):
                sol = solve_ivp(rhs, (start, end), y, method='DOP853',
                                rtol=2e-12, atol=2e-13)
                self.assertTrue(sol.success, sol.message)
                y = sol.y[:, -1]
            coefficients = np.linalg.solve(wave_matrix(-R, L), y)
            r = coefficients[1]/coefficients[0]
            leading = 1j*(2*sici(2*R)[0]+np.pi)/(4*L)
            error_scale = 1/(L*R)+R*R*(1+np.log(R))**2/(L*L)
            ratio = abs(r-leading)/error_scale
            self.assertLess(ratio, 2.)
            rows.append(dict(L=L, R=R, local_reflection=[float(r.real), float(r.imag)],
                             first_order=[float(leading.real), float(leading.imag)],
                             discrepancy=float(abs(r-leading)),
                             discrepancy_over_stated_scale=float(ratio)))
        REPORT['finite_central_transfers_not_full_cycle_predictions'] = rows

    def test_passive_outer_bound_including_dirichlet(self) -> None:
        rows = []
        for L in (10., 20.):
            R, B = L**.25, L*L
            A = quad(lambda x: -log_data(x, L)[1].imag, R, B, epsabs=1e-10)[0]
            I = quad(lambda x: abs(log_data(x, L)[3]/log_data(x, L)[1]),
                     R, B, epsabs=1e-12)[0]
            bound = 4*np.exp(-2*A)+12.5*I
            for name, m in (('real_zero', 0j), ('dissipative', -1j), ('dirichlet', None)):
                _, q, h, _ = log_data(B, L)
                terminal = -1+0j if m is None else (m+h/2+1j*q)/(1j*q-m-h/2)
                def rhs(x: float, z: np.ndarray) -> np.ndarray:
                    _, qx, _, om = log_data(x, L)
                    return 2j*qx*z+1j*om*(1+z)**2/(2*qx)
                sol = solve_ivp(rhs, (B, R), np.array([terminal]), method='DOP853',
                                rtol=2e-10, atol=2e-12)
                self.assertTrue(sol.success, sol.message)
                observed = abs(sol.y[0, -1])
                self.assertLess(observed, bound+1e-8)
                self.assertLess(np.max(abs(sol.y[0])), 4+1e-8)
                rows.append(dict(L=L, termination=name, attenuation=A,
                                 integrated_defect=I, local_bound=bound,
                                 reflection_at_R=float(observed)))
        REPORT['passive_log_region_finite_examples'] = rows

    def test_exact_negative_tail_measure_and_scaling(self) -> None:
        # Derivatives cross-checked from the full positive spectral measure.
        derivative_error = 0.
        for eps in (.03, .4, 2.):
            data = negative_green(eps)
            for j, prefactor in ((0, 1.), (1, -1.), (2, 2.)):
                def f(e: float) -> float:
                    rho = ellipkm1((e-4)**2/16)/(2*np.pi**2)
                    return prefactor*rho/(e+eps)**(j+1)
                integral = sum(quad(f, lo, hi, epsabs=2e-9, epsrel=2e-10,
                                    limit=200)[0] for lo, hi in ((0., 4.), (4., 8.)))
                derivative_error = max(derivative_error, abs(integral-data[j])/max(1., abs(data[j])))
            self.assertGreaterEqual(data[0]*data[2]-2*data[1]**2, -1e-12)
        self.assertLess(derivative_error, 2e-8)
        rows = []
        for L in (12., 24., 48., 96.):
            R = L**.25
            energy = 32*np.exp(-L)
            root_alpha = energy/np.sqrt(L/(4*np.pi))
            low = energy*R
            def physical(eps: float) -> float:
                g, gp, gpp = negative_green(eps)
                return gpp/(4*np.sqrt(g))-3*gp*gp/(16*g**1.5)
            # Log-coordinate integration resolves the shrinking lower limit.
            middle = quad(lambda z: root_alpha*physical(low*np.exp(z))*low*np.exp(z),
                          0., np.log(128/low), epsabs=2e-12, epsrel=2e-10, limit=200)[0]
            tail = root_alpha*quad(physical, 128., np.inf, epsabs=2e-10,
                                   epsrel=2e-10, limit=200)[0]
            I = middle+tail
            scaled = L*R*I
            self.assertGreater(I, 0)
            self.assertLess(scaled, 1.)
            rows.append(dict(L=L, lower_physical_energy=float(low),
                             exact_negative_defect_integral=float(I),
                             L_R_times_integral=float(scaled)))
        REPORT['spectral_derivative_relative_error'] = derivative_error
        REPORT['exact_negative_tail_integrals'] = rows

    def test_exact_lattice_logarithmic_C2_replacement(self) -> None:
        rows = []
        with mp.workdps(80):
            for L0 in (14, 24, 40):
                L = mp.mpf(L0); energy = 32*mp.exp(-L)
                for sign in (-1, 1):
                    for x0 in (L**mp.mpf('.25'), L*L):
                        x = sign*x0
                        def exact(t):
                            e = energy*t
                            if sign < 0:
                                g = -2*mp.ellipk(16/(4-e)**2)/(mp.pi*(4-e))
                            else:
                                a = (e-4)**2/16
                                g = -(mp.ellipk(a)+1j*mp.ellipk(1-a))/(2*mp.pi)
                            return -L/(4*mp.pi*g)
                        def local(t):
                            return L/(L-mp.log(sign*t)+(1j*mp.pi if sign > 0 else 0))
                        residuals = [abs(mp.diff(lambda t: exact(t)-local(t), x, j))
                                     /(energy*x0**(1-j)) for j in (0, 1, 2)]
                        self.assertLess(max(residuals), mp.mpf('2'))
                        rows.append(dict(L=L0, x=float(x),
                                         scaled_C2_errors=[float(v) for v in residuals]))
        REPORT['exact_local_replacement_derivative_checks'] = rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error('Output already exists; choose a fresh path.')
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ReflectionMatchingTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',
                  tests_run=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                  scope='Finite Gate B diagnostics; separate from the preserved 272 controls.')
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8') as stream:
            json.dump(REPORT, stream, indent=2, allow_nan=False); stream.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
