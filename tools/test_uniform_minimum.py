#!/usr/bin/env python3
"""Small Gate C diagnostics; finite sampling is not a uniformity proof.

No original scientific script or saved result is rewritten. Optional JSON output
is exclusive-create. Run: python tools/test_uniform_minimum.py --output NEW.json
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
from scipy.special import sici

from test_reflection_matching import negative_green, complex_quad

REPORT: dict[str, object] = {}
RHO = 1/(4*np.pi)


def local_data(x: float, L: float, b: float):
    """F, q, h and Omega, only at nonzero x where this basis is used."""
    if x == 0:
        raise ValueError('Wave data are undefined at the central turning point.')
    D = complex(L-np.log(abs(x)), np.pi if x > 0 else 0.)
    F = L/D-b
    F1 = L/(x*D*D)
    F2 = L*(2-D)/(x*x*D**3)
    q = np.sqrt(F)
    return F, q, F1/(2*F), 5*F1*F1/(16*F*F)-F2/(4*F)


def wave_matrix(x: float, L: float, b: float):
    _, q, h, _ = local_data(x, L, b)
    k = np.sqrt(1-b)
    w = q**(-.5)*np.exp(np.array([-1j*k*x, 1j*k*x]))
    return np.vstack((w, np.array([-h/2-1j*q, -h/2+1j*q])*w))


def defect(eps: float, u: float):
    """Exact shifted physical-energy defect before its sqrt(alpha) factor."""
    G, G1, G2 = negative_green(eps)
    kappa = 1-u*G
    if kappa <= 0:
        raise ValueError('Negative-tail integration entered the forbidden region.')
    term1 = 5*G1*G1/(16*G**1.5)
    term2 = (G*G2-2*G1*G1)/(4*G**1.5)
    return term1/kappa**2.5+term2/kappa**1.5


class UniformMinimumTests(unittest.TestCase):
    def test_symbolic_offset_frame_and_shifted_defect(self):
        x, k = sp.symbols('x k', real=True, positive=True)
        v, t = sp.symbols('v t', real=True)
        q = sp.sqrt(k*k+t*v)
        phase = sp.diag(sp.exp(-sp.I*k*x), sp.exp(sp.I*k*x))
        plane = sp.Matrix([[1, 1], [-sp.I*k, sp.I*k]])*phase/sp.sqrt(k)
        wave = sp.Matrix([[1, 1], [-sp.I*q, sp.I*q]])*phase/sp.sqrt(q)
        derivative = (plane.inv()*wave).diff(t).subs(t, 0)
        target = -v/(4*k*k)*sp.Matrix([[0, sp.exp(2*sp.I*k*x)],
                                       [sp.exp(-2*sp.I*k*x), 0]])
        self.assertEqual((derivative-target).applyfunc(sp.simplify), sp.zeros(2))
        F, b = sp.symbols('F b')
        self.assertEqual(sp.expand((F-b)-(1-b)-(F-1)), 0)
        G, G1, G2, u = sp.symbols('G G1 G2 u', real=True)
        W1, W2 = -G1/G**2, (2*G1**2-G*G2)/G**3
        # Verify the polynomial numerators after multiplying out positive roots.
        lhs = 5*W1**2*G**4/16-W2*G**3*(1-u*G)/4
        rhs = 5*G1**2/16+(G*G2-2*G1**2)*(1-u*G)/4
        self.assertEqual(sp.factor(lhs-rhs), 0)
        REPORT['symbolic_identities'] = 'offset, endpoint frame, shifted defect numerator'

    def test_integrated_central_remainder_including_core(self):
        rows = []
        for L in (16., 64., 256.):
            R = L**.25
            # x=exp(-t): the full central core t in [0,infinity) is included.
            small, outer = 0., 0.
            for jump in (0., np.pi):
                small += quad(lambda t: np.exp(-t)*abs(complex(-t, -jump)**2
                                  /(L*complex(L+t, jump))), 0., np.inf,
                              epsabs=2e-12, epsrel=2e-11)[0]
                outer += quad(lambda x: abs(complex(np.log(x), -jump)**2
                                  /(L*complex(L-np.log(x), jump))), 1., R,
                              epsabs=2e-12, epsrel=2e-11)[0]
            scale = (1+R*(1+np.log(R))**2)/L**2
            self.assertLess((small+outer)/scale, 20.)
            for b in (0., .4, .8):
                for x in (-.03, -.5, 1.2, R):
                    V = complex(np.log(abs(x)), np.pi*-float(x > 0))
                    exact_remainder = (L/(L-V)-b)-(1-b)-V/L
                    self.assertLess(abs(exact_remainder-V*V/(L*(L-V))), 1e-14)
            delta = .2
            xc = np.exp(-delta*L/2)
            e_star = 32*np.exp(-L)
            exact_at_cut = RHO*L/negative_green(e_star*xc)[0]
            self.assertGreater(exact_at_cut, 1-delta)
            # Local turning points are never used as integration cutoffs.
            for b in (.2, .5, .8):
                log_xt = -L*(1/b-1)
                value_at_turn = L/(L-log_xt)-b
                self.assertLess(abs(value_at_turn), 1e-14)
                self.assertLess(log_xt, -delta*L/2)
            rows.append(dict(L=L, full_core_remainder=small, outer_remainder=outer,
                             integral_over_declared_scale=(small+outer)/scale,
                             exact_coefficient_at_uniform_core_cut=exact_at_cut))
        REPORT['central_integrals_no_deleted_core'] = rows

    def test_finite_central_transfers_with_varying_b(self):
        rows = []
        for L in (64., 256., 1024.):
            R = L**.25
            for label, b in (('zero', 0.), ('interior', .4), ('margin', .8),
                             ('varying', .8*(1-1/np.sqrt(L)))):
                k = np.sqrt(1-b)
                y = wave_matrix(R, L, b)[:, 0]
                def rhs(x, state):
                    F = -b+0j if x == 0 else local_data(x, L, b)[0]
                    return np.array([state[1], -F*state[0]])
                for lo, hi in ((R, 0.), (0., -R)):
                    sol = solve_ivp(rhs, (lo, hi), y, method='DOP853',
                                    rtol=2e-12, atol=2e-13)
                    self.assertTrue(sol.success, sol.message)
                    y = sol.y[:, -1]
                coeff = np.linalg.solve(wave_matrix(-R, L, b), y)
                r = coeff[1]/coeff[0]
                leading = 1j*(2*sici(2*k*R)[0]+np.pi)/(4*L*k*k)
                scale = 1/(L*R)+R*R*(1+np.log(R))**2/L**2
                scaled = abs(r-leading)/scale
                self.assertLess(scaled, 4/(k**4))
                # Check the boundary cancellation without a distribution solver.
                integral = (complex_quad(lambda x: np.log(-x)*np.exp(-2j*k*x), -R, 0.)
                          +complex_quad(lambda x: (np.log(x)-1j*np.pi)*np.exp(-2j*k*x), 0., R))
                boundary = (np.log(R)-1j*np.pi)*np.exp(-2j*k*R)-np.log(R)*np.exp(2j*k*R)
                self.assertLess(abs(-1j*integral/(2*k*L)-boundary/(4*L*k*k)-leading), 2e-11)
                rows.append(dict(L=L, b=b, family=label, reflection=[float(r.real), float(r.imag)],
                                 finite_window_leading=[0., float(leading.imag)],
                                 discrepancy_over_scale=float(scaled)))
        REPORT['finite_transfer_not_exponential_time_simulation'] = rows

    def test_passive_bound_without_imaginary_h_sign(self):
        rows, reversed_signs = [], 0
        L = 16.
        R, B = L**.25, L*L
        for b in (0., .6, .8):
            grid = np.geomspace(R, B, 120)
            data = [local_data(float(x), L, b) for x in grid]
            reversed_signs += sum(h.imag > 0 for _, _, h, _ in data)
            self.assertTrue(all(q.real > 0 and abs(h) <= q.real for _, q, h, _ in data))
            A = quad(lambda x: -local_data(x, L, b)[1].imag, R, B, epsabs=1e-10)[0]
            I = quad(lambda x: abs(local_data(x, L, b)[3]/local_data(x, L, b)[1]),
                     R, B, epsabs=2e-12)[0]
            bound = 7*np.exp(-2*A)+32*I
            for label, m in (('real', 0j), ('passive', 2-3j), ('dirichlet', None)):
                _, q, h, _ = local_data(B, L, b)
                terminal = -1+0j if m is None else (m+h/2+1j*q)/(1j*q-m-h/2)
                if m is not None:
                    self.assertGreaterEqual(abs(1j*q-m-h/2), q.real-abs(h)/2-1e-14)
                self.assertLess(abs(terminal), 7.)
                def rhs(x, z):
                    _, qx, _, omega = local_data(x, L, b)
                    return 2j*qx*z+1j*omega*(1+z)**2/(2*qx)
                sol = solve_ivp(rhs, (B, R), np.array([terminal]), method='DOP853',
                                rtol=2e-10, atol=2e-12)
                self.assertTrue(sol.success, sol.message)
                r = abs(sol.y[0, -1])
                self.assertLess(r, bound+1e-8)
                self.assertLess(np.max(abs(sol.y[0])), 7.)
                rows.append(dict(L=L, b=b, termination=label, attenuation=A,
                                 integrated_defect=I, passive_bound=bound, observed=float(r)))
        self.assertGreater(reversed_signs, 0)
        REPORT['positive_h_imaginary_part_samples'] = reversed_signs
        REPORT['finite_passive_examples_not_physical_far_band'] = rows

    def test_exact_shifted_negative_tail_domination(self):
        rows = []
        for L in (16., 32., 64.):
            R = L**.25; e_star = 32*np.exp(-L)
            root_alpha, a = e_star/np.sqrt(RHO*L), e_star*R
            def integral(u):
                middle = quad(lambda z: root_alpha*defect(a*np.exp(z), u)*a*np.exp(z),
                              0., np.log(128/a), epsabs=2e-12, epsrel=2e-10, limit=200)[0]
                far = root_alpha*quad(lambda eps: defect(eps, u), 128., np.inf,
                                      epsabs=2e-10, epsrel=2e-10, limit=200)[0]
                return middle+far
            I0 = integral(0.)
            for b in (0., .4, .8, .8*(1-1/L)):
                u = b/(RHO*L); kappa = 1-u*negative_green(a)[0]
                self.assertGreaterEqual(kappa, .1)
                Ib = integral(u)
                bound = kappa**(-2.5)*I0
                self.assertGreater(Ib, 0.)
                self.assertLessEqual(Ib, bound+1e-11)
                for eps in np.geomspace(a, 128., 25):
                    G, G1, G2 = negative_green(float(eps))
                    self.assertGreaterEqual(1-u*G, kappa-1e-12)
                    self.assertGreaterEqual(G*G2-2*G1*G1, -1e-10*max(G*G2, 1.))
                rows.append(dict(L=L, b=b, margin_at_cutoff=kappa, defect_integral=Ib,
                                 exact_margin_domination_bound=bound,
                                 L_R_times_defect=L*R*Ib))
        REPORT['exact_shifted_negative_tail_integrals'] = rows

    def test_shifted_exact_lattice_root_and_derivative_control(self):
        rows = []
        with mp.workdps(80):
            for L0 in (16, 32):
                L = mp.mpf(L0); e_star = 32*mp.exp(-L)
                for x in (L**mp.mpf('.25'), L*L):
                    def unshifted(t):
                        E = e_star*t
                        a = (E-4)**2/16
                        G = -(mp.ellipk(a)+1j*mp.ellipk(1-a))/(2*mp.pi)
                        return -L/(4*mp.pi*G)
                    exact0 = [mp.diff(unshifted, x, j) for j in range(3)]
                    D = L-mp.log(x)+1j*mp.pi
                    loc0 = [L/D, L/(x*D**2), L*(2-D)/(x*x*D**3)]
                    for b0 in (0, .4, .8):
                        b = mp.mpf(str(b0))
                        def basis(dat):
                            F, F1, F2 = dat[0]-b, dat[1], dat[2]
                            q = mp.sqrt(F); h = F1/(2*F)
                            omega = 5*F1**2/(16*F**2)-F2/(4*F)
                            return q, h, omega/q
                        exact, local = basis(exact0), basis(loc0)
                        ratios = [abs(exact[0]-local[0])/(e_star*x),
                                  abs(exact[1]-local[1])/e_star,
                                  abs(exact[2]-local[2])/(e_star/x+e_star**2)]
                        self.assertLess(max(ratios), 100.)
                        rows.append(dict(L=L0, x=float(x), b=b0,
                                         scaled_root_h_defect_differences=[float(v) for v in ratios]))
        REPORT['shifted_exact_lattice_derivative_diagnostics'] = rows

    def test_parameter_identity_and_uniform_endpoint_scale(self):
        rows = []
        for L in (16., 64., 256.):
            for b in (0., .4, .8, .8*(1-1/np.sqrt(L))):
                u = b/(RHO*L)
                log_T = .5*np.log((4-u)*RHO*L)-np.log(32)+L
                implicit = log_T+np.log(32)-.5*np.log((4-u)*RHO)
                self.assertLess(abs(implicit-L-.5*np.log(L)), 2e-13)
                self.assertLess(u, 1.)
                relative_tail_scale = L**1.25*np.exp(-log_T)
                self.assertLess(relative_tail_scale, 1e-4)
                rows.append(dict(L=L, b=b, u=u, log_T=log_T,
                                 L_to_five_fourths_over_T=relative_tail_scale))
        REPORT['physical_parameter_and_endpoint_identities'] = rows


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error('Output exists; choose a fresh path.')
    result = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(UniformMinimumTests))
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',
                  tests_run=result.testsRun, failures=len(result.failures), errors=len(result.errors),
                  scope='Finite Gate C checks; not a uniform proof, device claim or original-suite extension.')
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8') as f:
            json.dump(REPORT, f, indent=2, allow_nan=False); f.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
