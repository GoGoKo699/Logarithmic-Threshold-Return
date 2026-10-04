#!/usr/bin/env python3
"""Small preparation/readout checks; not new threshold-dynamics controls.

Run directly. Optional --output writes a new static diagnostic JSON and refuses
an existing path. No preserved scientific module or reference is modified.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import unittest
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ellipe, ellipk


def endpoint() -> dict[str, float]:
    """Exact square-lattice Green function at attraction 4, in J=1 units."""
    def integral1(eta: float) -> float:
        z = eta + 4.0
        return float(2 * ellipk(16 / z**2) / (np.pi * z))
    eta = brentq(lambda x: 4 * integral1(x) - 1, 1e-4, 10, xtol=1e-14)
    z = eta + 4.0
    integral2 = float(2 * ellipe(16 / z**2) / (np.pi * (z*z - 16)))
    origin_weight = 1 / (16 * integral2)
    return dict(eta=eta, integral1=integral1(eta), integral2=integral2,
                origin_weight=origin_weight,
                projector_distance=float(np.sqrt(1-origin_weight)),
                phase_flipped_overlap=(1-2*origin_weight)**2)


def torus(n: int) -> dict[str, float]:
    if n < 3 or n % 2 == 0:
        raise ValueError("Use an odd periodic square of side at least three.")
    k = 2*np.pi*np.arange(n)/n
    energies = 4-2*np.cos(k[:, None])-2*np.cos(k[None, :])
    eta = brentq(lambda x: 4*np.mean(1/(energies+x))-1, 1e-4, 10, xtol=1e-14)
    state_k = 1/(n*(energies+eta))
    state_k /= np.linalg.norm(state_k)
    state = np.fft.ifft2(state_k, norm='ortho')
    hstate = 4*state - sum(np.roll(state, s, ax) for ax in (0, 1) for s in (-1, 1))
    hstate[0, 0] -= 4*state[0, 0]
    return dict(n=n, eta=eta, origin_weight=float(abs(state[0, 0])**2),
                normalization_error=float(abs(np.vdot(state, state)-1)),
                eigenstate_residual=float(np.linalg.norm(hstate+eta*state)))


def projector(vector: np.ndarray) -> np.ndarray:
    return np.outer(vector, vector.conj())


def distance(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sum(np.abs(np.linalg.eigvalsh(a-b)))/2)


class OperationalContractTests(unittest.TestCase):
    def test_endpoint_integrals_independently(self):
        d = endpoint()
        z = d['eta']+4
        i1 = quad(lambda k: 1/np.sqrt((z-2*np.cos(k))**2-4),
                  0, np.pi, epsabs=1e-13, epsrel=1e-13)[0]/np.pi
        i2 = quad(lambda k: (z-2*np.cos(k))/((z-2*np.cos(k))**2-4)**1.5,
                  0, np.pi, epsabs=1e-13, epsrel=1e-13)[0]/np.pi
        self.assertLess(abs(4*i1-1), 2e-12)
        self.assertLess(abs(i2-d['integral2']), 2e-12)
        self.assertTrue(0.72 < d['origin_weight'] < 0.73)

    def test_finite_endpoint_state_not_dynamics(self):
        d = endpoint()
        for n, tolerance in ((17, 1e-6), (33, 1e-10), (65, 1e-10)):
            with self.subTest(n=n):
                r = torus(n)
                self.assertLess(abs(r['eta']-d['eta']), tolerance)
                self.assertLess(abs(r['origin_weight']-d['origin_weight']), tolerance)
                self.assertLess(r['normalization_error'], 1e-12)
                self.assertLess(r['eigenstate_residual'], 2e-12)

    def test_exact_projector_distance_and_witness(self):
        w = endpoint()['origin_weight']
        b = np.array([np.sqrt(w), np.sqrt(1-w)])
        p, q = projector(b), np.diag([1., 0.])
        values, vectors = np.linalg.eigh(q-p)
        expected = np.sqrt(1-w)
        self.assertLess(abs(np.max(np.abs(values))-expected), 2e-14)
        witness = vectors[:, -1]
        self.assertLess(abs(np.vdot(witness, (q-p)@witness)-expected), 2e-14)

    def test_identical_position_histograms_do_not_fix_overlap(self):
        w = endpoint()['origin_weight']
        b = np.array([np.sqrt(w), np.sqrt(1-w)])
        flipped = np.diag([-1., 1.])@b
        np.testing.assert_array_equal(abs(b)**2, abs(flipped)**2)
        self.assertLess(abs(abs(np.vdot(b, flipped))**2-(1-2*w)**2), 1e-14)
        self.assertGreater(1-abs(np.vdot(b, flipped))**2, .79)

    def test_trace_distance_error_contract(self):
        # Deterministic small examples, including an erasure state orthogonal
        # to the two-dimensional single-particle sector. No postselection.
        b = np.array([np.sqrt(.7), np.sqrt(.3), 0.], dtype=complex)
        p = projector(b)
        theta = .4
        u = np.array([[np.cos(theta), -np.sin(theta), 0],
                      [np.sin(theta), np.cos(theta), 0], [0, 0, 1.]])
        ideal = u@p@u.conj().T
        vacuum = np.diag([0., 0., 1.])
        for prep_error, loss, inefficiency in ((0, 0, 0), (.03, .04, .05), (.2, .1, .3)):
            rho = (1-prep_error)*p+prep_error*np.diag([1., 0., 0.])
            coherent = u@rho@u.conj().T
            actual = (1-loss)*coherent+loss*vacuum
            effect = (1-inefficiency)*p
            self.assertLess(abs(np.trace(actual)-1), 1e-14)
            errors = distance(rho, p)+distance(actual, coherent)+np.linalg.norm(effect-p, ord=2)
            difference = abs(np.trace(effect@actual)-np.trace(p@ideal))
            self.assertLessEqual(difference, errors+1e-14)

    def test_survival_denominator_and_pure_state_error(self):
        p_cond, loss = .04, .15
        state = np.diag([(1-loss)*p_cond, (1-loss)*(1-p_cond), loss])
        raw = float(np.trace(np.diag([1., 0., 0.])@state))
        survival = float(np.trace(np.diag([1., 1., 0.])@state))
        self.assertAlmostEqual(raw, (1-loss)*p_cond)
        self.assertAlmostEqual(raw/survival, p_cond)
        self.assertNotEqual(raw, p_cond)
        for infidelity in (.001, .1, .5):
            a = np.array([1., 0.])
            b = np.array([np.sqrt(1-infidelity), np.sqrt(infidelity)])
            self.assertAlmostEqual(distance(projector(a), projector(b)), np.sqrt(infidelity))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.output and args.output.exists():
        raise FileExistsError('Use a new output path; diagnostics are not overwritten.')
    result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(OperationalContractTests))
    if not result.wasSuccessful():
        raise SystemExit(1)
    if args.output:
        report = dict(scope='Static endpoint and elementary operational checks, not time evolution, independent review, or laboratory calibration.',
                      tests=result.testsRun, status='PASS', endpoint=endpoint(),
                      finite_endpoint_checks=[torus(n) for n in (17, 33, 65)])
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open('x', encoding='utf-8') as out:
            json.dump(report, out, indent=2, allow_nan=False)
            out.write('\n')


if __name__ == '__main__':
    main()
