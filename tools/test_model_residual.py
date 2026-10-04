#!/usr/bin/env python3
"""Small residual/calibration checks, separate from the 272 preserved controls.

No scientific reference is changed. Optional --output refuses an existing path.
The short lattice example checks an inequality, not the asymptotic return law.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import unittest

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

REPORT: dict[str, object] = {}


def norm(x: np.ndarray) -> float:
    return float(np.linalg.norm(x))


def phase_distance(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.sqrt(max(0.0, 2 - 2 * abs(np.vdot(a, b)))))


def torus(side: int) -> np.ndarray:
    if side < 3:
        raise ValueError('The periodic side must be at least three.')
    shift = np.roll(np.eye(side), 1, axis=0)
    hop = shift + shift.T
    return 4 * np.eye(side**2) - np.kron(hop, np.eye(side)) - np.kron(np.eye(side), hop)


class ModelResidualTests(unittest.TestCase):
    def test_orthogonal_residual_blocks(self) -> None:
        rng = np.random.default_rng(481)
        b, _ = np.linalg.qr(rng.normal(size=(6, 3)) + 1j*rng.normal(size=(6, 3)))
        raw = rng.normal(size=(6, 6)) + 1j*rng.normal(size=(6, 6))
        h = (raw + raw.conj().T)/2
        ref = np.diag([.1, -.4, 1.2])
        c = .73
        d = h@b - b@(ref+c*np.eye(3))
        k = b.conj().T@h@b - ref-c*np.eye(3)
        coupling = (np.eye(6)-b@b.conj().T)@h@b
        psi = np.array([1, 1j, -2], dtype=complex)/np.sqrt(6)
        self.assertLess(norm(d-b@k-coupling), 4e-14)
        self.assertLess(norm(b.conj().T@coupling), 4e-14)
        self.assertAlmostEqual(norm(d@psi)**2, norm(k@psi)**2+norm(coupling@psi)**2, places=12)

    def test_common_shift_is_not_a_relative_error(self) -> None:
        ref = np.array([[.1, -.4], [-.4, .2]])
        c, duration = 13., .8
        psi = np.array([1., 0.], dtype=complex)
        actual = expm(-1j*(ref+c*np.eye(2))*duration)@psi
        ideal = np.exp(-1j*c*duration)*expm(-1j*ref*duration)@psi
        self.assertLess(norm(actual-ideal), 4e-14)
        self.assertLess(norm(ref+c*np.eye(2)-ref-c*np.eye(2)), 4e-14)
        self.assertGreater(norm(c*np.eye(2)@psi), 10)

    def test_moving_embedding_connection_sign(self) -> None:
        g = np.array([[0, .2, .1], [.2, .4, -.3], [.1, -.3, -.1]], dtype=complex)
        b = expm(-1j*g*.7)[:, :2]
        bdot = -1j*g@b
        ref = np.array([[.2, -.5], [-.5, -.4]])
        h = g+b@ref@b.conj().T
        self.assertLess(norm(h@b-b@ref-1j*bdot), 4e-14)
        self.assertGreater(norm(h@b-b@ref), .1)

    def test_small_leakage_does_not_bound_return_error(self) -> None:
        rows = []
        psi = np.array([1., 1., 0.], dtype=complex)/np.sqrt(2)
        for n in (10, 40, 100):
            omega = n/(n-1)
            g = .5*np.sqrt(omega**2-1)
            h = np.array([[0, 0, 0], [0, 0, g], [0, g, 1.]], dtype=complex)
            tau = 2*np.pi*(n-1)
            final = expm(-1j*h*tau)@psi
            expected = np.array([1., -1., 0.])/np.sqrt(2)
            leakage_max = 1/n-1/(2*n*n)
            at_max = expm(-1j*h*np.pi/omega)@psi
            self.assertLess(norm(final-expected), 2e-12)
            self.assertLess(abs(abs(at_max[2])**2-leakage_max), 2e-13)
            self.assertLess(abs(final[2])**2, 1e-24)
            self.assertLess(abs(np.vdot(psi, final))**2, 1e-24)
            rows.append(dict(n=n,maximum_leakage=leakage_max,
                             final_leakage=float(abs(final[2])**2),
                             actual_return=float(abs(np.vdot(psi,final))**2)))
        REPORT['leakage_counterexample'] = rows

    def test_short_fixed_cycle_duhamel_bound(self) -> None:
        side, half_time, minimum = 5, 1.5, .15
        size = side**2
        h0 = torus(side)
        q = np.zeros((size,size)); q[0,0] = 1
        _, vecs = np.linalg.eigh(h0-4*q)
        bound = vecs[:,0].astype(complex)
        other = np.eye(size)[1].astype(complex)
        other -= bound*np.vdot(bound,other)
        other /= norm(other)
        prepared = np.cos(.015)*bound+np.sin(.015)*other
        measured = np.cos(.012)*bound-np.sin(.012)*other
        defect = np.zeros((size,size)); defect[1,1]=.017; defect[2,2]=-.011
        defect[0,1]=defect[1,0]=.006
        def rhs(t: float, state: np.ndarray) -> np.ndarray:
            ref = h0-(minimum+(4-minimum)*(t/half_time)**2)*q
            ideal, actual = state[:size],state[size:2*size]
            change = (1+.2*np.cos(t))*defect
            return np.concatenate((-1j*ref@ideal,-1j*(ref+change)@actual,
                                   np.array([norm(change@ideal)],dtype=complex)))
        initial = np.concatenate((bound,prepared,np.array([0j])))
        result = solve_ivp(rhs,(-half_time,half_time),initial,method='DOP853',
                           rtol=2e-12,atol=2e-14)
        self.assertTrue(result.success,result.message)
        ideal,actual = result.y[:size,-1],result.y[size:2*size,-1]
        residual = float(result.y[-1,-1].real)
        dp,dm = phase_distance(prepared,bound),phase_distance(measured,bound)
        d = dp+residual+dm
        target = float(abs(np.vdot(bound,ideal))**2)
        observed = float(abs(np.vdot(measured,actual))**2)
        bound_probability = 2*np.sqrt(target)*d+d*d
        self.assertLess(abs(norm(ideal)-1),2e-10)
        self.assertLess(abs(norm(actual)-1),2e-10)
        self.assertLessEqual(norm(actual-ideal),dp+residual+2e-10)
        self.assertLessEqual(abs(np.sqrt(observed)-np.sqrt(target)),d+2e-10)
        self.assertLessEqual(abs(observed-target),bound_probability+2e-10)
        REPORT['short_cycle'] = dict(side=side,half_duration=half_time,
            ideal_return=target,actual_return=observed,integrated_residual=residual,
            total_vector_budget=d,probability_error=abs(observed-target),
            probability_error_bound=bound_probability)

    def test_near_dark_amplitude_and_incoherent_contamination(self) -> None:
        for scale in (10.,100.,1000.):
            amplitude = 1/scale
            psi = np.array([amplitude,np.sqrt(1-amplitude**2)])
            perpendicular = np.array([psi[1],-psi[0]])
            angle = .3/scale**1.2
            actual = np.cos(angle)*psi+np.sin(angle)*perpendicular
            d = norm(actual-psi)
            p = amplitude**2
            self.assertLessEqual(abs(actual[0]**2-p),2*np.sqrt(p)*d+d*d+1e-14)
            rate = .01
            contaminated = (1-rate)*p+rate
            self.assertAlmostEqual(contaminated-p,rate*(1-p))
            self.assertGreater(contaminated-p,.009)

    def test_confinement_moment_and_row_sum(self) -> None:
        sites = np.arange(-3,4)
        psi = np.exp(-sites**2/5).astype(complex); psi /= norm(psi)
        curvature = .031
        diagonal = curvature*sites**2
        expected = abs(curvature)*np.sqrt(np.sum(sites**4*abs(psi)**2))
        self.assertAlmostEqual(norm(diagonal*psi),expected,places=14)
        k = np.diag(diagonal)+.021*(np.eye(7,k=1)+np.eye(7,k=-1))
        v = float(np.max(abs(np.diag(k))))
        j = float(np.max(np.sum(abs(k-np.diag(np.diag(k))),axis=1)))
        self.assertLessEqual(np.linalg.norm(k,ord=2),v+j+1e-14)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args = parser.parse_args()
    if args.output is not None and args.output.exists():
        parser.error(f'Output already exists: {args.output}')
    tests = unittest.defaultTestLoader.loadTestsFromTestCase(ModelResidualTests)
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    REPORT.update(status='PASS' if result.wasSuccessful() else 'FAIL',
                  tests_run=result.testsRun,original_272_controls=False)
    if args.output is not None:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open('x',encoding='utf-8') as handle:
            json.dump(REPORT,handle,indent=2,sort_keys=True,allow_nan=False)
            handle.write('\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)


if __name__ == '__main__':
    main()
