"""Infrastructure checks; not new physics controls."""
from pathlib import Path
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify import compare, decode, integrity, review_workload


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
    def test_known_workload_preserves_raw_failure(self):
        path = '/groups/full_physical_band/rows/0/values/2/function_evaluations'
        changes = compare(116696, 116672, path)
        result = review_workload('07_threshold_audit', changes)
        self.assertTrue(result['accepted'])
        self.assertEqual(len(result['reviewed_workload']), 1)
        self.assertFalse(changes[0]['accepted'])
    def test_workload_is_suite_and_path_specific(self):
        path = '/groups/full_physical_band/rows/0/values/2/function_evaluations'
        self.assertFalse(review_workload('09_threshold_core', compare(3, 4, path))['accepted'])
        self.assertFalse(review_workload('07_threshold_audit', compare(3, 4, '/case_count'))['accepted'])
    def test_workload_does_not_hide_type_or_invalid_counts(self):
        path = '/groups/full_physical_band/rows/0/values/2/function_evaluations'
        for a, b in [(3, 4.), (3, -1), (True, 4)]:
            self.assertFalse(review_workload('07_threshold_audit', compare(a, b, path))['accepted'])
    def test_ordinary_physical_error_still_rejected(self):
        changes = compare(.9, .901, '/groups/full_physical_band/rows/0/values/2/probability')
        self.assertFalse(review_workload('07_threshold_audit', changes)['accepted'])
    def test_repository_inputs(self):
        self.assertEqual(integrity()['suites'], 5)


if __name__ == '__main__':
    unittest.main(verbosity=2)
