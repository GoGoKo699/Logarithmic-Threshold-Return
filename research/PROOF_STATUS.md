# Return law and proof map

Read [CORE](CORE.md) for the physical question and [CLAIMS](CLAIMS.md) for the
claim-to-derivation routes. The four components below establish the uniform
return law and its sufficient finite-volume realization.

## The fixed statement and its quantifiers

The protocol uses one particle, a nearest-neighbor square lattice, attraction
$`U(t)=u+(4-u)(t/T)^2`$ for $`-T\le t\le T`$, and unconditional return to the
endpoint bound orbital. For fixed $`0<\delta\le1`$, let

```math
\rho_0=\frac1{4\pi},\quad u(L,b)=\frac b{\rho_0L},\quad
T(L,b)=\frac{e^L}{32}\sqrt{(4-u(L,b))\rho_0L},\quad 0\le b\le1-\delta.
```

The uniform law is

```math
\sup_{0\le b\le1-\delta}
\left|\frac{4L^2(1-b)^2}{\pi^2}P_\infty(T(L,b),u(L,b))-1\right|\to0.
```

The same limit holds for $`P_{n(T)}`$ with the sufficient
$`n(T)=2\lceil4.5T\rceil+1`$. Each finite observable uses its own endpoint
bound vector, not an assumed copy of the infinite one. At $`u=0`$ this yields
$`P\sim\pi^2/(4\ln^2T)`$. Fixed positive depth and fixed volume are different
orders of limits and ultimately have adiabatic return. The margin below $`b=1`$
must stay fixed.

## Dependency chain and error scale

| Component | Derivation | What it supplies | Error or normalization boundary |
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

## Attribution and accuracy

The local power-law tangent in [AUDIT Section 7](AUDIT.md) predicts the full leading
positive-minimum prefactor. [The critical assessment](CRITICAL_ASSESSMENT.md)
works out that comparison and composes the A–D errors. The controlled logarithmic
physical limit and its joint domain are the result supplied by the proof route.
The same assessment attributes the midpoint identity to Sokolovski–Pons (2016),
Eq. (5).

[Limits and accuracy](LIMITS_AND_ACCURACY.md) derives uniform recovery at each
fixed finite size and explains the resolution of the leading remainder. The
inherited power comparator uses its stated $`0<\sigma<1`$ domain.
[Scientific context](../literature/SCIENTIFIC_CONTEXT.md) records primary
attributions; [scope and verification](../STATUS.md) maps the executable evidence.
