# Failed Gate B diagnostic: structural symbolic zero

**4 October 2026. New diagnostic development only.** Five of the six new tests
passed on the first run. The Riccati identity assertion returned the structurally
unevaluated expression `0*I`, which did not compare equal to the integer `0` in
that assertion. Canonicalizing the factored expression with `simplify` yields
exact zero. All six tests then pass. The equation, expected identity and every
numerical tolerance are unchanged; this is not a corrected physical coefficient.

Initial script SHA-256: `9ca98512f74b4d745f3eedd726b7b3598e1fa8925c044935fad56d425a3a765d`.
Corrected script SHA-256: `ef1fb13c39d871d10e630c2e19e0a7a9ff531af068f69b1eabe40aa22c94c9bb`.
First log SHA-256: `641ca3c1ce37a92211c1799617907c4a32f9c0aad008cdc9aed462d9886b4e3f`.
First report SHA-256: `b1edd8154180221d8a4c969a726078e1f05bc4fcdc4436b13298a48f7c16a811`.

The failed script, log and report are retained in the conversation evidence package.
This exact repair patch reconstructs the first script when applied in reverse
with `git apply --reverse --unidiff-zero`. It is not executed by the scientific runner.

```diff
--- initial/tools/test_reflection_matching.py
+++ corrected/tools/test_reflection_matching.py
@@ -75 +75,2 @@
-        self.assertEqual(sp.factor(rp-2*sp.I*q*r-sp.I*omega*(1+r)**2/(2*q)), 0)
+        self.assertEqual(sp.simplify(sp.factor(
+            rp-2*sp.I*q*r-sp.I*omega*(1+r)**2/(2*q))), 0)
```
