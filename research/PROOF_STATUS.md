# Consolidated proof status: one claim, four author-side gates

**5 October 2026. Internal research map, not a manuscript or independent report.**
Read [CORE](CORE.md) for the physical question and [CLAIMS](CLAIMS.md) for the
original-source routes. This map records what the bounded A-D scrutiny supplied,
what it did not establish, and where further work should stop.

## The fixed statement and its quantifiers

The protocol remains one particle, a nearest-neighbor square lattice, attraction
$`U(t)=u+(4-u)(t/T)^2`$ for $`-T\le t\le T`$, and unconditional return to the
endpoint bound orbital. For fixed $`\delta>0`$, let

```math
\rho_0=\frac1{4\pi},\quad u(L,b)=\frac b{\rho_0L},\quad
T(L,b)=\frac{e^L}{32}\sqrt{(4-u(L,b))\rho_0L},\quad 0\le b\le1-\delta.
```

The author-side claim is the uniform law

```math
\sup_{0\le b\le1-\delta}
\left|\frac{4L^2(1-b)^2}{\pi^2}P_\infty(T(L,b),u(L,b))-1\right|\to0.
```

The same limit holds for $`P_{n(T)}`$ with the already specified sufficient
$`n(T)=2\lceil4.5T\rceil+1`$. Each finite observable uses its own endpoint
bound vector, not an assumed copy of the infinite one. At $`u=0`$ this yields
$`P\sim\pi^2/(4\ln^2T)`$. Fixed positive depth and fixed volume are different
orders of limits and ultimately have adiabatic return. The margin below $`b=1`$
must stay fixed; no full crossover is claimed.

## Dependency chain and error scale

| Gate | Author-side expansion | What it supplies | Error or normalization boundary |
|---|---|---|---|
| A | [Physical amplitude](AMPLITUDE_IDENTIFICATION.md) | Retarded norm reconstruction, no incoming continuum, equal bound-leg normalization, finite endpoints | Remote time first at fixed parameters; endpoint modulus error $`O(T^{-1})`$ uniformly for small $`u`$ |
| B | [Reflection matching](REFLECTION_MATCHING.md) | Both causal contributions, explicit endpoint cancellation, exact-lattice passive and negative-tail matching | Zero minimum; phase-adjusted amplitude $`i\pi/(2L)+O(L^{-5/4})`$ |
| C | [Uniform minimum](UNIFORM_MINIMUM.md) | Full central core, sign-independent passive denominator, exact shifted-tail domination | Supremum over $`b\le1-\delta`$; amplitude error $`O_\delta(L^{-5/4})`$ |
| D | [Finite volume](FINITE_VOLUME.md) | Endpoint normalization/energy/phase, bounded-weight limit, seam, midpoint transpose | State error $`\mathcal B\le K(1+T)e^{-\gamma T}`$, $`\gamma>0`$; amplitude error at most $`2\mathcal B`$ |

The proof order is A plus B, then the uniform extension C, then D. A phase is not
silently set equal across different representations: B-C give a phase-adjusted
amplitude; A compares physical amplitude moduli; D compares finite and infinite
amplitudes in their common real endpoint convention. These distinctions suffice
for the probability statement without inventing a phase-identification theorem.

For D, $`\eta_\infty\ge2\sqrt2-2`$ proves the weight choice admissible
analytically. The finite-volume constants are independent of the residual depth,
so the small instantaneous gap does not enter that comparison. The additional
relative probability error is $`O_\delta(L\mathcal B+L^2\mathcal B^2)`$.
This is negligible compared with the existing conservative matched remainder.

The original protected notes remain byte-preserved. The four expansions add
explicit arguments; they do not erase their earlier wording or certify every
sentence in the historical source. No coefficient, Hamiltonian or domain
correction was found in these bounded author-side passes. This is an author-side
assessment, not evidence of an independent reader's agreement.

## Consolidated author-side assessment

[CRITICAL_ASSESSMENT](CRITICAL_ASSESSMENT.md) checks the A-D interfaces and combines
their amplitude errors explicitly. No coefficient or domain correction was found in
those checks. It also sharpens the originality objection: the local power-law tangent
predicts the full positive-minimum prefactor, not only the zero-minimum constant.
The controlled physical limit, not those prefactors in isolation, is the contribution
under assessment. The assessment adds direct attribution of the midpoint identity to the 2016
predecessor. No independent reader rating is supplied by this pass.

## What remains genuinely unresolved

**Separate critical reading.** All four reader gates remain unrated by an external
reader. [READER_PACKET](READER_PACKET.md) is still a brief, not a received report.
An assessor must specify the revision, passages checked, reasoning, and the effect
of any objection on the central claim. Another assistant session does not establish
independence merely by repeating the calculation.

**Priority and significance.** [The scoped comparison](../literature/DEVDARIANI_COMPARISON.md)
resolves the identified predecessor construction but is not exhaustive priority.
The static logarithm, threshold-loss phenomenon, energy-domain method, power-law
connection formula and localization tools are inherited. The contribution under
assessment is this controlled logarithmic return law and its finite joint domain,
not the number of auxiliary lemmas or successful tests. The familiar small-power
tangent in [AUDIT Section 7](AUDIT.md) remains a serious comparator, not a result to
hide or automatically equate with a proof of the present limit.

**Implementation.** [ASSUMPTIONS](../literature/ASSUMPTIONS.md) records component
support and exact-model mismatches. The endpoint preparation, unconditional orbital
projector, calibrated generator and joint coherent operating window are not
established as a device. The error inequalities in [PREPARATION_READOUT](PREPARATION_READOUT.md)
and [MODEL_RESIDUAL](MODEL_RESIDUAL.md) are sufficient conditional guarantees, not
achieved specifications. Some precedent-count targets remain unmet. They are not
fixed by adding unrelated platform or imaging citations.

The full residual-depth crossover, optimal lattice size, arbitrary trap universality,
many-body extensions, dimensional crossover and application superiority are outside
the claim. They are not required repairs unless a concrete objection makes one
necessary. Fixed positive anisotropy remains a supporting scope check, not a fifth
central proof gate or a substitute for significance.

## Completion boundary for this phase

The bounded author-side A-D expansion is complete as a route for critical reading.
Do not start an automatic Gate E or another numerical campaign. The consolidated author-side assessment is now recorded. Further work must
respond to an exact objection, a directly matching predecessor, or a genuinely
separate critical reading; routine internal proof expansion stops here. Reopen a physical premise only for directly model-matched evidence.
Manuscript drafting, release and all outside contact remain on hold.

Numerical execution, byte reproduction, symbolic diagnostics and scientific proof
review remain distinct. The original suite is still 5 suites / 28 groups / 272
controls; the eight D diagnostics are supplementary. Actual verification outcomes
belong in their retained reports and PR comments, not in claims inferred from badges.
