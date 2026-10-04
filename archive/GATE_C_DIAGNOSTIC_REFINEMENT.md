# Gate C diagnostic refinement: keep the central equation off a singular wave chart

**4 October 2026. Test implementation only; no physical equation or tolerance change.**
The first seven-test Gate C candidate passed. An additional exact-turning-point probe
then exposed an avoidable issue in its diagnostic RHS: it called `local_data(...)[0]`
to obtain the regular scalar coefficient, but that helper also evaluated unused
wave-basis quantities proportional to inverse powers of the coefficient. At a zero
of the coefficient those unused quantities are singular.

With NumPy floating-point warnings raised as exceptions, the actual probe was:

```python
with np.errstate(all='raise'):
    local_data(-np.exp(-16.), 16., .5)[0]
# FloatingPointError: divide by zero encountered in scalar divide
```

The central ODE coefficient itself is zero there and has no singularity. This is
not a failure of an original 272-control suite, not a defect of the integrated
central estimate, and not evidence for cutting out the turning region.

The repair gives the central ODE a coefficient-only evaluator, including the exact
origin limit. Wave data remain confined to their outer-basis use. A new assertion
inside the existing central-remainder test checks both the exact turning point and
the origin with floating warnings promoted to errors. The seven-test count is
unchanged. No equation, integration tolerance, reference or protected source changed.

The pre-refinement script, raw probe log and forward/reverse patch are retained in
the conversation evidence package. The original candidate is also Git commit
`52bc319675c2d77c894580059745f010a9fd2794`; its scientific report is not relabeled
as failed. The exact diagnostic code change is:

```diff
--- a/tools/test_uniform_minimum.py
+++ b/tools/test_uniform_minimum.py
@@ -22,0 +23,8 @@
+
+
+def local_coefficient(x: float, L: float, b: float):
+    """The central equation is regular even where a wave basis is singular."""
+    if x == 0:
+        return complex(-b)
+    D = complex(L-np.log(abs(x)), np.pi if x > 0 else 0.)
+    return L/D-b
@@ -78,0 +87,3 @@
+        with np.errstate(all='raise'):
+            self.assertEqual(local_coefficient(-np.exp(-16.), 16., .5), 0j)
+            self.assertEqual(local_coefficient(0., 16., .5), -.5+0j)
@@ -122 +133 @@
-                    F = -b+0j if x == 0 else local_data(x, L, b)[0]
+                    F = local_coefficient(x, L, b)
```

The refined frozen tree and hosted runs require their own completed reports. Do not
infer them from the initial pass or confuse this auxiliary probe with an interrupted
scientific verification.
