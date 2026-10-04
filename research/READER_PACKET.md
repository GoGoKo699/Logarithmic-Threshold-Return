# Separate-reader packet: try to break the fixed claim

**Prepared 4 October 2026; no separate report received.** This is an author-prepared
review brief, not a review. It neither nominates nor contacts a reader. Manuscript
writing and outreach remain on hold.

## The object under review

The preserved argument is pinned to repository revision
`3604714b9a38da484b3f78828d6d1a7cad35c7d4`; its source hashes are in
[IMPORT_MAP.json](../provenance/IMPORT_MAP.json). Read [CORE](CORE.md), then
[ASYMPTOTIC](ASYMPTOTIC.md), [AUDIT](AUDIT.md) and [ROUNDING](ROUNDING.md).
Read [SPECTRAL_SCOPE](SPECTRAL_SCOPE.md) only for the terminology correction and
fixed-positive-anisotropy corollary. This packet changes none of those files.

The single main statement, in the conventions of CORE, is

```math
P_\infty(T,u(T))=
\frac{\pi^2}{4L^2[1-b(T)]^2}[1+o(1)],\qquad
0\le b(T)\le1-\delta,\quad \delta>0\text{ fixed}.
```

The observable is endpoint bound-state return, not origin occupation. The lattice
is infinite first, or increases along the explicitly sufficient finite family.
A fixed positive minimum and a fixed finite square are not covered by that limit.
The question is whether the full argument proves this exact claim, not whether
some plot looks compatible with it.

## Gate A: physical amplitude, retarded choice and finite endpoints

**Read:** ASYMPTOTIC Sections 2–3; AUDIT Sections 2 and 5; ROUNDING Section 2.

Reconstruct the outgoing Fourier problem with its non-decaying remote-time bound
amplitude. Decide whether an oscillatory-distribution formulation and the absence
of incoming continuum data actually select the stated solution. Derive both
stationary-phase normalization factors using the exact pole residue; check that
no factor of $`L`$, $`2`$ or $`\alpha`$ survives in their ratio.

For the added temporal tails, verify the commutator solution and integrability
of its derivative and comparison-generator terms. The required conclusion is
an $`O(T^{-1})`$ bound on the difference of amplitude moduli, uniformly for the
small residual-depth family. Agreement at two finite durations is insufficient.
A missing wave-operator or endpoint estimate is a mathematical gap to report,
not a detail to assume away.

## Gate B: central reflection and the physical far band

**Read:** ASYMPTOTIC Sections 4–7; AUDIT Sections 3–5.

Check the lower-edge retarded branch and the integrated, rather than pointwise,
central expansion. Derive the endpoint-basis cancellation explicitly, retaining
both $`\operatorname{PV}(1/x)`$ and the causal delta term. Check the leading
amplitude $`i\pi/(2L)`$, including normalization and orientation.

Then reconstruct the exact reflection-coordinate equation, its continuation
through zeros of the solution, and the passive half-plane argument. Show that
the actual boundary beyond the whole lattice band supplies the required sign.
A chosen numerical absorber is not a substitute. On both outer sides, include
the physical-energy-to-scaled-energy change in the defect integral. Every
remaining amplitude error must be $`o(L^{-1})`$; the displayed conservative
outer estimate is $`O(L^{-5/4})`$.

## Gate C: a uniform, positive-minimum family

**Read:** ROUNDING Sections 2–5, alongside Gate B.

Take the supremum over $`0\le b\le1-\delta`$ at each step. In particular, test
the exponentially narrow turning region inside the central interval, the
bound on $`q_0^{-1}`$, and the revised denominator inequality for the passive
reflection coordinate. Do not reuse the zero-minimum sign of $`\operatorname{Im}h`$
without checking it. The asymptotic must remain uniform in the chosen family;
a collection of fixed-$`b`$ calculations does not establish this.

No proof through $`b=1`$, fixed-$`u`$ probability formula, or exact crossover
percentage is requested or implied. Identify any conclusion that accidentally
uses one of those stronger statements.

## Gate D: finite initial states, periodic seam and return

**Read:** ROUNDING Section 6.

Verify the weighted-hopping estimate on the torus and infinite lattice, including
the normalized endpoint states and their energy-dependent resolvents. Check the
seam residual, phase choice, and Duhamel comparison. Derive why real, even-time
evolution gives the midpoint bilinear amplitude $`\psi(0)^T\psi(0)`$ rather than
the norm, and propagate the state-norm error to return amplitude.

For $`\mu=1/2`$ and $`n(T)=2\lceil4.5T\rceil+1`$, the required error is
$`o(L^{-1})`$. Check the endpoint localization condition as well as the sign of
the propagation exponent. A sufficient size is not a lower bound on necessary
size; no optimal-size campaign is part of this brief.

## Report format and decision rule

A genuine separate report should identify its reader, affiliation or relevant
expertise if supplied, date, exact revision, materials actually checked and
whether its derivation was independent of the author-side answers. For each gate,
record **supported**, **repair required**, **counterexample**, or **not checked**,
with the exact passage, reasoning and effect on the main claim. Leave every gate
unrated until that report exists. A fresh assistant session alone is not evidence
of an independent scientific assessment.

A counterexample or a repair that changes the leading coefficient, observable
or uniform domain must be recorded before editing preserved scientific files.
A narrower valid conclusion must be labeled as such. Passing software checks
cannot overrule a mathematical objection. Conversely, an objection to an unclaimed
laboratory implementation is not automatically a counterexample to the conditional
Hamiltonian theorem.

Use the [Devdariani comparison](../literature/DEVDARIANI_COMPARISON.md) together with
the preserved [prior-art register](../literature/PRIOR_ART.md) to challenge attribution.
A supported report would still not establish exhaustive priority or complete the
[physical-premise audit](../literature/ASSUMPTIONS.md).
