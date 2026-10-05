# Claim-to-proof map

**5 October 2026.** This is a navigation layer over the preserved source notes. It does
not strengthen a claim, remove a hypothesis, or replace the full derivations.

## The single central statement

For the stated quadratic local-trap cycle, a logarithmic lower-edge resolvent gives
vanishing slow-cycle recapture with a calculated inverse-square-logarithmic law. Its
positive-minimum and finite-volume domain are supporting parts of that statement.

| Claim | Exact route | Numerical controls | What is not inferred |
|---|---|---|---|
| Local unitary source and bound-state return | CORE, model; ASYMPTOTIC Sections 2–4 | Suite 05 coordinate/spectral comparison, suite 06 time/energy comparison | Site occupation is not the return projector |
| Leading logarithmic law and coefficient | ASYMPTOTIC Sections 5–7, read together with AUDIT | Suites 06–07 scalar formulations, physical-band and boundary checks | Numerical convergence is not the matching proof |
| Positive-minimum law for b below one | ROUNDING Sections 2–4; UNIFORM_MINIMUM | Suite 08 joint-coefficient and finite-time checks | No formula through b=1 or every fixed residual depth |
| A finite-system family with the same limit | ROUNDING Section 6; FINITE_VOLUME | Suite 08 finite torus/coordinate and locality controls | Sufficient size is not necessary or optimized size |
| Fixed positive unequal hoppings | SPECTRAL_SCOPE Sections 2–4 | Suite 09 resolvent, causality and scalar checks | Not uniform as transverse hopping vanishes |

Read [CORE.md](CORE.md) first, then [ASYMPTOTIC.md](ASYMPTOTIC.md),
[AUDIT.md](AUDIT.md), [ROUNDING.md](ROUNDING.md), and
[SPECTRAL_SCOPE.md](SPECTRAL_SCOPE.md). The local source labels differ between the
preserved notes; [SOURCES.md](SOURCES.md) resolves them.

## Four proof obligations for a separate reader

1. Does the retarded Fourier equation and its stationary-phase normalization identify
   auxiliary reflection with the physical bound-to-bound amplitude, with the finite
   gapped tails controlled at the stated order?
2. Do the integrated central expansion, branch discontinuity and outer current bound
   control all matching errors, including the van Hove region without an artificial sink?
3. Is the positive-minimum estimate uniform on the stated b domain, without extrapolating
   its apparent pole into the unresolved crossover?
4. Does the finite-volume estimate include the initial-state difference and periodic
   seam, making the stated order of limits sufficient without asserting an optimal size?

These are questions for the exact argument, not a claim that the software has proved it.
The earlier audit answers are author-side answers. A separate report is not yet present.

[Gate A](AMPLITUDE_IDENTIFICATION.md) now expands the physical-channel identification.
[Gate B](REFLECTION_MATCHING.md) expands the endpoint cancellation and exact-lattice
outer estimates for zero minimum. [Gate C](UNIFORM_MINIMUM.md) supplies the uniform
positive-minimum expansion and [Gate D](FINITE_VOLUME.md) the finite-volume chain.
The [consolidated proof status](PROOF_STATUS.md) records the dependencies and remaining
obligations. All four are author-side arguments; no separate report is present.

[Limits and accuracy](LIMITS_AND_ACCURACY.md) now makes fixed-size recovery uniform
in minimum depth and states the resolution limit of the existing remainder. The
[scientific preparation record](SCIENTIFIC_PREPARATION.md) connects these clarifications
to the updated primary-source context and the completed
[2014 construction comparison](../literature/SOKOLOVSKI_PONS_MUGA_2014.md).

## What is inherited and what remains open

The static resolvent, essential weak binding, threshold-loss problem, energy-domain
method, gapped recovery and locality tools are established ingredients. Read
[PRIOR_ART.md](../literature/PRIOR_ART.md) before framing originality.
The 2014 comparison also makes explicit that a finite-box/continuum contrast is
inherited; the controlled logarithmic law and stated joint domain remain the claim.

The [Devdariani construction comparison](../literature/DEVDARIANI_COMPARISON.md)
now closes the specifically recorded primary-access gap while preserving the narrow
core and strengthening attribution. Exact physical implementation and a separate
reader report remain open; the [reader packet](READER_PACKET.md) is preparation only.
Full crossover, general trap universality, optimal volume, experimental superiority
and a joint apparatus are not claimed. The known terminology
correction is in SPECTRAL_SCOPE: the lower-edge density is finite; the Green function
is logarithmic. The original older wording is preserved, not silently rewritten.

[Gate C](UNIFORM_MINIMUM.md) makes the positive-minimum quantifiers and shifted
negative-tail domination explicit. Its seven finite diagnostics are separate from
the preserved scientific suites and do not constitute an independent report.
