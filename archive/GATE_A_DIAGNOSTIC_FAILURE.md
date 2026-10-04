# Failed Gate A diagnostic: elliptic-parameter cancellation

**4 October 2026. New diagnostic development only.** The protected scientific
scripts, references and tolerance policy were not changed.

The first `test_lattice_current_and_continuum_weight` run failed with
`Required step size is less than spacing between numbers`, preceded by invalid
complex-division warnings. The other six new tests passed. In the new diagnostic,
forming `1-a` close to the middle-band singularity rounded it to one, turning the
elliptic integral into infinity before the exact reciprocal limit was reached.
The repaired evaluator uses `ellipkm1` and algebraically stable complementary
parameters at the band edges and middle. The equation and every assertion
tolerance are unchanged. The corrected seven-test run passes.

Initial script SHA-256: `3e572522e03c79fdecdf8147128bfa9f1294aa8b6db30784381cde846f6a0cbb`.
Corrected script SHA-256: `b77ed21d19b0524a8609dc0a07575c912ebb25a008d83cbbe13989de9a7a9ca7`.

This exact patch reconstructs the initial attempt by applying it in reverse (`git apply --reverse --unidiff-zero`) to
the corrected script in this revision. Full initial/corrected logs and JSON reports
are retained in the conversation evidence package. This archive is not imported
by the active verification route.

```diff
--- initial/tools/test_amplitude_identification.py
+++ corrected/tools/test_amplitude_identification.py
@@ -16 +16 @@
-from scipy.special import airy, ellipk
+from scipy.special import airy, ellipkm1
@@ -37 +37 @@
-        return complex(-np.pi*z/(2*ellipk(16/z**2)))
+        return complex(-np.pi*z/(2*ellipkm1((-e)*(8-e)/z**2)))
@@ -40 +40 @@
-        return complex(np.pi*z/(2*ellipk(16/z**2)))
+        return complex(np.pi*z/(2*ellipkm1((e-8)*e/z**2)))
@@ -42 +42,2 @@
-    g = np.sign(e-4)*ellipk(a)/(2*np.pi) - 1j*ellipk(1-a)/(2*np.pi)
+    g = (np.sign(e-4)*ellipkm1(e*(8-e)/16)/(2*np.pi)
+         - 1j*ellipkm1(a)/(2*np.pi))
@@ -143 +144 @@
-                        rho = ellipk(1-a)/(2*np.pi**2)
+                        rho = ellipkm1(a)/(2*np.pi**2)
```
