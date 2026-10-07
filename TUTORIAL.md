# Tutorial route: Demkov–Ostrovskii to logarithmic return

[Project overview](README.md) · [Reading guide](docs/README.md) · [Local bridge](research/TUTORIAL_BRIDGE.md)

This is the selected single-book route to the lattice model and its return law.

Yu. N. Demkov and V. N. Ostrovskii, *Zero-Range Potentials and Their Applications
in Atomic Physics*, translated by A. M. Ermolaev, Plenum Press (1988),
Physics of Atoms and Molecules.
[Publisher book page](https://link.springer.com/book/10.1007/978-1-4684-5451-2);
[DOI: 10.1007/978-1-4684-5451-2](https://doi.org/10.1007/978-1-4684-5451-2).

Use the book with the repository's [tutorial bridge](research/TUTORIAL_BRIDGE.md).
The book provides the learning route; the bridge identifies the steps specific to
this lattice problem. Research-paper citations elsewhere remain provenance and
comparison evidence, not a second required tutorial syllabus.

## Preparation

The route assumes working knowledge of single-particle quantum mechanics:
normalization, bound and continuum states, unitary evolution, and scattering.
For the technical bridge, be comfortable with resolvents, Fourier transforms,
complex logarithms, contour integration, ordinary differential equations,
stationary phase and asymptotic error estimates. These are expectations for this
route, not a claim about the book's own stated prerequisites.

Start by reading the [fixed question](README.md#the-fixed-question) and
[CORE](research/CORE.md). Write down the Hamiltonian, the endpoint bound vector,
and the return projector before beginning the external reading.

## Focused reading route

Page numbers below are printed pages. Subsection numbers and their starting
pages come from the publisher's [contents](https://link.springer.com/content/pdf/bfm:978-1-4684-5451-2/1).
They locate a proposed reading assignment; only the preview pages in the access
ledger below were checked in main text. Topic labels here are paraphrased.

| Stage | Assignment | Focus |
|---|---|---|
| 1 | Chapter 1, pp. 1–21: §§1.2, 1.3, 1.4 begin on pp. 4, 8, 14 | Local interactions and separable potentials |
| 2 | Chapter 2, pp. 23–41: §§2.2, 2.4, 2.5 begin on pp. 25, 35, 39 | Pole motion and weak binding near a continuum |
| 3 | Chapter 8, pp. 181–207: prioritize §§8.1–8.2, starting pp. 181, 186 | Time dependence and linear detachment models |
| 4 | Chapter 9, pp. 209–233: prioritize §§9.1–9.2, starting pp. 209, 220 | Contour constructions and adiabatic pole motion |
| 5 | Chapter 10, pp. 235–255: §§10.1–10.3 begin on pp. 235, 239, 249 | Nonlinear schedules and quadratic approximations |

The inspected Chapter 8 opening distinguishes continuum transitions from
isolated two-state crossings. The Chapter 9 preview constructs an energy-contour
solution for a linearly driven separable perturbation. The Chapter 10 preview
motivates time-symmetric quadratic schedules. These are reasons for the route;
they do not establish the contents or conclusions of uninspected sections.

## Checkpoints in this repository

Complete each checkpoint by explaining the argument and locating its assumptions.
The links identify the existing account to check, rather than additional
experiments or a new numerical campaign.

1. **Fix the observable.** Explain why a population measurement on the addressed
   site is not the declared bound-state return. Identify the two finite endpoints
   and the meaning of the half-cycle time in [CORE](research/CORE.md) and
   [preparation/readout](research/PREPARATION_READOUT.md).

2. **Translate the local interaction.** Starting from the rank-one lattice
   perturbation, reconstruct its pole equation and bound-state normalization
   using [the bridge](research/TUTORIAL_BRIDGE.md) and [CORE](research/CORE.md).
   Keep the continuum point-interaction construction and the lattice operator
   distinct; their parameters and Green functions require an explicit map.

3. **Identify the threshold.** Explain how a finite nonzero lower-edge density
   produces the local Green-function logarithm and exponentially shallow binding.
   Locate the separate middle-band van Hove feature in
   [spectral scope](research/SPECTRAL_SCOPE.md). Do not replace the exact lattice
   Green function by a continuum analogy without stating the approximation.

4. **Recover the physical amplitude.** Follow [Gate A](research/AMPLITUDE_IDENTIFICATION.md)
   from the time equation to the scalar energy equation. Track the Fourier sign,
   causal boundary value, outgoing condition, channel normalization and finite
   endpoints. Explain which comparisons concern amplitudes and which concern
   their moduli; a reflection coefficient alone is not the physical identification.

5. **Control the logarithmic matching.** In [Gate B](research/REFLECTION_MATCHING.md),
   identify both causal contributions and the outer error estimate. In
   [Gate C](research/UNIFORM_MINIMUM.md), locate the fixed margin
   $`0\le b\le1-\delta`$ and explain why the estimate is uniform there.
   Use [limits and accuracy](research/LIMITS_AND_ACCURACY.md) to distinguish the
   leading law from a justified subleading expansion.

6. **State the order of limits.** Follow [Gate D](research/FINITE_VOLUME.md)
   with the finite torus's own endpoint state. Explain why the increasing-volume
   result and ultimate return at each fixed finite volume are compatible.
   Give the analogous distinction between fixed positive minimum depth and
   a minimum shrinking within the stated joint domain.

7. **Reassemble the result.** Use [PROOF_STATUS](research/PROOF_STATUS.md) to
   state the quantifiers and compose A–D. Then distinguish the inherited method,
   a prefactor heuristic, and the controlled physical limit using
   [the critical assessment](research/CRITICAL_ASSESSMENT.md).

## Access ledger and stopping point

The source access for this selection was checked on 6 October 2026:

| Material | Access actually used |
|---|---|
| Publisher record and linked front matter | Bibliography and full contents inspected |
| [Chapter 8 preview](https://page-one.springer.com/pdf/preview/10.1007/978-1-4684-5451-2_8) | Main text pp. 181–182 only |
| [Chapter 9 preview](https://page-one.springer.com/pdf/preview/10.1007/978-1-4684-5451-2_9) | Main text pp. 209–210 only |
| [Chapter 10 preview](https://page-one.springer.com/pdf/preview/10.1007/978-1-4684-5451-2_10) | Main text pp. 235–236 only |
| Other assigned main-text pages | Located from contents; not read in this selection pass |

The publisher presents the full text as subscription content. No complete book
or chapter reading is claimed, and no third-party PDF is stored in this repository.
The available pages neither prove nor exclude the repository's specific theorem;
this pedagogical selection is not an exhaustive priority comparison.

The learning goal is the ability to reconstruct and question the fixed proof
route, including its residual-depth and finite-size restrictions. For the
repository's role and discussion details, see [Purpose and contact](README.md#purpose-and-contact).
