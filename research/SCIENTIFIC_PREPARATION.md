# Scientific support for logarithmic return

The result is controlled logarithmic bound-state return for the specified quadratic
cycle, with the residual-depth and finite-volume domain stated in
[PROOF_STATUS](PROOF_STATUS.md). This map connects the physical observable,
asymptotic estimates and source comparisons.

## Claim and support map

| Claim or ingredient | Supporting argument | Scope |
|---|---|---|
| Physical bound-to-bound observable and normalization | [Gate A](AMPLITUDE_IDENTIFICATION.md); [CORE](CORE.md) and [ASYMPTOTIC](ASYMPTOTIC.md) | No incoming continuum; unconditional endpoint projector |
| Leading logarithmic return and uniform positive minimum | [Gates B](REFLECTION_MATCHING.md) and [C](UNIFORM_MINIMUM.md); [assessment](CRITICAL_ASSESSMENT.md) | Fixed margin below $`b=1`$; power comparator restricted to $`0<\sigma<1`$ |
| A sufficient increasing finite family | [Gate D](FINITE_VOLUME.md) | Own endpoint states and seam estimates; sufficient rather than optimal size |
| Fixed finite geometry, including $`u=u(T)\to0`$ | [Limits and accuracy, Section 1](LIMITS_AND_ACCURACY.md) | Uniform recovery with an $`n`$-dependent bound; growing $`n`$ requires a separate comparison |
| Meaning of implicit $`L`$ and the matched remainder | [Limits and accuracy, Section 2](LIMITS_AND_ACCURACY.md) | Leading coefficient controlled; subleading logarithmic coefficients, finite-time precision and eventual monotonicity are not resolved by this remainder |
| Static logarithm, essential binding, adiabatic and localization tools | [Scientific context](../literature/SCIENTIFIC_CONTEXT.md); [source map](SOURCES.md) | Inherited ingredients attributed; exact lattice conventions separated from continuum analogies |
| Threshold-dynamics constructions | [Prior art](../literature/PRIOR_ART.md), [Devdariani](../literature/DEVDARIANI_COMPARISON.md), [context](../literature/SCIENTIFIC_CONTEXT.md), [2014 construction](../literature/SOKOLOVSKI_PONS_MUGA_2014.md) | Comparisons track the schedule, observable, binding law and asymptotic hypotheses |
| Physical model conventions | [Physical precedents](../literature/PHYSICAL_PRECEDENTS.md) and [assumptions](../literature/ASSUMPTIONS.md) | Source-specific support and model differences for local trapping, motion and control |
| Preparation, readout and generator errors | [Preparation/readout](PREPARATION_READOUT.md), [generator residual](MODEL_RESIDUAL.md) | Sufficient conditional bounds on changes to the declared return probability |

Uniformity requires $`0\le b\le1-\delta`$ with fixed $`0<\delta\le1`$.
The fixed-positive-anisotropy check in [SPECTRAL_SCOPE](SPECTRAL_SCOPE.md)
is likewise restricted to positive transverse hopping; it is not uniform in
the dimensional-crossover limit.

## Power-tangent comparison

The local power tangent predicts the full leading prefactor, including its
residual-depth factor. The [critical assessment](CRITICAL_ASSESSMENT.md) compares
this prediction with the controlled logarithmic limit. The contribution is the
identification and uniform control of the declared physical return, including
finite endpoints and a sufficient growing-volume family. The inherited
threshold-loss phenomenon and prefactor prediction are part of that comparison.

## Linear threshold approach and finite confinement

Sokolovski–Pons–Muga (2014) solves a monotone linear approach stopped below
threshold, measures the final normalized bound-state population, and has algebraic
binding. Its exact integral and fixed-final-energy slow limit do not supply the
two-leg logarithmic return or its joint uniform estimates. Its energy method and
finite-box contrast are direct precedents.

The [passage-level comparison](../literature/SOKOLOVSKI_PONS_MUGA_2014.md)
uses the supplied seven-page primary text, read in full with decisive equations
on pp. 2–6 visually checked. It tracks the schedule and endpoints, observable,
binding law and asymptotic hypotheses.

## Source provenance

[Preparation provenance](../provenance/SCIENTIFIC_PREPARATION_2026-10-05.json)
records the assessed revision and source-access history.
[2014 source provenance](../provenance/SOURCE_COMPARISON_2014_2026-10-05.json)
records the supplied PDF hash and the full-text comparison that supersedes the
earlier access-limited entry. The [source map](SOURCES.md) explains local citation
labels and links each reading to its applicable access depth.
