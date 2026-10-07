# Claim-to-proof map

For the specified quadratic local-trap cycle, the logarithmic lower-edge resolvent
produces vanishing slow-cycle return to the endpoint bound orbital. Its uniform
shrinking-minimum and sufficient growing-volume domains form one central result.
[The proof map](PROOF_STATUS.md) states its exact quantifiers and error composition.

## Claims and derivations

| Claim | Derivation | Numerical controls | Scope |
|---|---|---|---|
| Local unitary source and bound-orbital return | [CORE](CORE.md); [A: physical amplitude](AMPLITUDE_IDENTIFICATION.md) | Suite 05 coordinate/spectral and suite 06 time/energy comparisons | Unconditional endpoint orbital projection |
| Leading logarithmic law and coefficient | [B: reflection matching](REFLECTION_MATCHING.md); [ASYMPTOTIC](ASYMPTOTIC.md), Sections 5–7; [AUDIT](AUDIT.md) | Suites 06–07 scalar formulations, physical band and causal boundaries | Exact touching; controlled leading matching |
| Uniform shrinking-minimum law | [C: uniform minimum](UNIFORM_MINIMUM.md); [ROUNDING](ROUNDING.md), Sections 2–4 | Suite 08 joint-coefficient and finite-time checks | Fixed $`0<\delta\le1`$, $`0\le b\le1-\delta`$ |
| Growing finite squares with the same law | [D: finite volume](FINITE_VOLUME.md); [ROUNDING](ROUNDING.md), Section 6 | Suite 08 torus/coordinate and locality controls | Sufficient $`n(T)=2\lceil4.5T\rceil+1`$; each square's own endpoint state |
| Fixed positive unequal hoppings | [SPECTRAL_SCOPE](SPECTRAL_SCOPE.md), Sections 2–4 | Suite 09 resolvent, causality and scalar checks | Supporting result; nonuniform at zero transverse hopping |

The original derivations are [CORE](CORE.md), [ASYMPTOTIC](ASYMPTOTIC.md),
[AUDIT](AUDIT.md) and [ROUNDING](ROUNDING.md). Their local source labels are
resolved in [SOURCES](SOURCES.md).

## Four proof components

1. [A](AMPLITUDE_IDENTIFICATION.md) reconstructs the retarded solution, identifies
   equal bound-channel normalization and controls the finite temporal endpoints.
   The endpoint estimate compares **amplitude moduli** at order $`O(T^{-1})`$.
2. [B](REFLECTION_MATCHING.md) controls the integrated central expansion, causal
   jump and exact-lattice outer matching, including the full physical band.
3. [C](UNIFORM_MINIMUM.md) makes those estimates uniform on the fixed-margin
   residual-depth domain.
4. [D](FINITE_VOLUME.md) bounds the finite/infinite initial-state difference,
   periodic seam and propagated error for the sufficient growing family.

[Limits and accuracy](LIMITS_AND_ACCURACY.md) treats fixed-size recovery,
the leading remainder and the power comparator's domain. [Preparation/readout](PREPARATION_READOUT.md)
and [model residuals](MODEL_RESIDUAL.md) state sufficient operational error conditions.

## Inherited ingredients and contribution

The static resolvent, essential weak binding, threshold-loss phenomenon,
energy-domain method, gapped recovery and localization tools have established
precedents. The local power-law tangent also predicts the leading prefactor.
The proof route controls the logarithmic physical limit and its stated joint domain.

[Scientific context](../literature/SCIENTIFIC_CONTEXT.md), the
[Devdariani construction comparison](../literature/DEVDARIANI_COMPARISON.md) and
[2014 comparison](../literature/SOKOLOVSKI_PONS_MUGA_2014.md) supply precise
attributions and inspected-source boundaries. The detailed comparator algebra is
in [the critical assessment](CRITICAL_ASSESSMENT.md). The lower-edge density is
finite; the logarithm belongs to the local Green function, as explained in
[spectral scope](SPECTRAL_SCOPE.md).
