"""Infrastructure checks; not new physics controls."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify import compare, decode, integrity


class VerificationTests(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(compare({'x': [1., 2]}, {'x': [1., 2]}), [])
    def test_metadata(self):
        self.assertTrue(compare({'environment': {'python': 'a'}}, {'environment': {'python': 'b'}})[0]['accepted'])
    def test_small_float(self):
        self.assertTrue(compare(.9, .9 + 1e-14)[0]['accepted'])
    def test_physical_change(self):
        self.assertFalse(compare(.9, .901)[0]['accepted'])
    def test_integer(self):
        self.assertFalse(compare(1000000000, 1000000001)[0]['accepted'])
    def test_type_and_bool(self):
        self.assertFalse(compare(True, 1)[0]['accepted'])
        self.assertFalse(compare(1, 1.)[0]['accepted'])
    def test_structure(self):
        self.assertFalse(compare({'x': 1}, {})[0]['accepted'])
        self.assertFalse(compare([1, 2], [1])[0]['accepted'])
    def test_invalid_json(self):
        for x in [b'{"x":NaN}', b'{"x":1,"x":2}', b'broken']:
            with self.assertRaises(ValueError):
                decode(x)
        self.assertFalse(compare(float('inf'), float('inf'))[0]['accepted'])
    def test_near_zero(self):
        d = compare(0., 1e-14)[0]
        self.assertTrue(d['accepted'])
        self.assertEqual(d['symmetric_relative_difference'], '1')
    def test_repository_inputs(self):
        self.assertEqual(integrity()['suites'], 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
