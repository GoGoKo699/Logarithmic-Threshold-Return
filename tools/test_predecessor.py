"""Algebra checks for the predecessor comparison, not new dynamics controls.

Run: python tools/test_predecessor.py
No saved scientific reference is read or rewritten. These checks cannot certify
primary-source interpretation or independently validate the logarithmic proof.
"""
import unittest
import sympy as sp


class PredecessorComparisonTests(unittest.TestCase):
    def test_energy_coordinate_bridge(self):
        z, a = sp.symbols("z a", positive=True)
        beta = sp.symbols("beta", real=True)
        phi = sp.Function("phi")(z)
        B = sp.sqrt(z) * phi
        # E=-z^2/2: d/dE=-(1/z)d/dz. Multiply the energy ODE by z^2.
        transformed = (sp.diff(B, z, 2) - sp.diff(B, z) / z
                       + (z**3 + beta * z**2) * B / a) / sp.sqrt(z)
        target = sp.diff(phi, z, 2) + ((z**3 + beta * z**2) / a
                                     - sp.Rational(3, 4) / z**2) * phi
        self.assertEqual(sp.simplify(transformed - target), 0)

    def test_exact_scale_elimination(self):
        a = sp.symbols("a", positive=True)
        tau, lam = sp.symbols("tau lam", real=True)
        t_scale, r_scale = a**(-sp.Rational(2, 5)), a**(-sp.Rational(1, 5))
        self.assertEqual(sp.simplify(1 / t_scale - 1 / r_scale**2), 0)
        scaled_robin = r_scale * (-a * (t_scale * tau)**2 + lam / r_scale)
        self.assertEqual(sp.simplify(scaled_robin - (lam - tau**2)), 0)

    def test_normalized_bound_state_and_quartic_touch(self):
        r, kappa, a = sp.symbols("r kappa a", positive=True)
        t = sp.symbols("t", real=True)
        psi = sp.sqrt(2 * kappa) * sp.exp(-kappa * r)
        self.assertEqual(sp.integrate(psi**2, (r, 0, sp.oo)), 1)
        self.assertEqual(sp.simplify(sp.diff(psi, r) / psi), -kappa)
        energy = sp.simplify(-sp.diff(psi, r, 2) / (2 * psi))
        self.assertEqual(energy, -kappa**2 / 2)
        self.assertEqual(energy.subs(kappa, a * t**2), -a**2 * t**4 / 2)

    def test_probability_labels_are_complementary(self):
        ionization = 2 * sp.cos(2 * sp.pi / 5)
        recapture = sp.simplify(ionization**2)
        self.assertEqual(sp.simplify(ionization + recapture), 1)
        self.assertEqual(sp.simplify(recapture - (3 - sp.sqrt(5)) / 2), 0)
        sigma = sp.Rational(1, 2)
        power_comparator = 4 * sp.cos(sp.pi / (2 + sigma))**2
        self.assertEqual(sp.simplify(power_comparator - recapture), 0)

    def test_distinct_threshold_scaling_ratios(self):
        L, s = sp.symbols("L s", positive=True)
        # epsilon=32 exp(-L); a fixed energy dilation changes L to L-log(s).
        logarithmic_ratio = L / (L - sp.log(s))
        self.assertEqual(sp.limit(logarithmic_ratio, L, sp.oo), 1)
        root_ratio = sp.sqrt(s)
        self.assertEqual(root_ratio.subs(s, 4), 2)
        self.assertNotEqual(root_ratio.subs(s, 4), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
