# Logarithmic Threshold Return

**A slowly weakened two-dimensional trap can recapture less, not more, in the slow-cycle limit.**

One particle starts bound to a single attractive lattice site. The attraction is weakened
and restored along the same quadratic schedule. We study return to the original bound
state, not merely the population of the addressed site. The dynamics are coherent and
closed: probability not recaptured remains in continuum states.

Threshold-touching loss is established physics. The result developed here is the
**inverse-square-logarithmic return law** at a logarithmic local-resolvent threshold,
together with a controlled finite-volume and positive-minimum domain.

## The fixed question

Use energies in $`J`$ and time in $`\hbar/J`$. On the square lattice,

```math
\begin{aligned}
H(t)&=H_0-\left[u+(4-u)(t/T)^2\right]|0\rangle\langle0|,\qquad -T\le t\le T,\\
P_\infty(T,u)&=|\langle b_4|\mathcal U(T,-T)|b_4\rangle|^2.
\end{aligned}
```

Here $`H_0`$ is the nearest-neighbor lattice Laplacian with band $`[0,8]`$, $`|b_4\rangle`$
is the endpoint bound state, and $`T`$ is the **half-cycle duration**. There is no bath,
finite interval of free waiting, or postselection. The endpoints have attraction 4
for every $`0\le u<4`$.

At exact touching, the recorded author-side asymptotic is

```math
\boxed{P_\infty(T,0)\sim\frac{\pi^2}{4\ln^2 T}\longrightarrow0.}
```

The dimensional logarithm means $`\ln(T_{\rm physical}J/\hbar)`$. It is a limiting law,
not a precision percentage formula at every finite duration.

## A trap that stays attractive can retain the effect

Define $`\rho_0=1/(4\pi)`$ and the scale $`L`$ by

```math
L+\tfrac12\ln L=\ln\frac{32T}{\sqrt{(4-u)\rho_0}},
\qquad b=\rho_0uL.
```

For $`0\le b(T)\le1-\delta`$ with fixed $`\delta>0`$, the current derivation gives

```math
P_\infty(T,u(T))=
\frac{\pi^2}{4L^2[1-b(T)]^2}[1+o(1)].
```

A strictly positive minimum $`u=o(1/\ln T)`$ keeps the original leading coefficient.
A sufficient sequence of finite periodic squares also retains the law. This is a
**joint limit**: fixed positive minimum or fixed finite size eventually restores
ordinary adiabatic return. The expansion does not apply at $`b=1`$.

| Limit | Recorded outcome | Boundary |
|---|---|---|
| Exact touching, infinite lattice before slow limit | Return vanishes logarithmically | Not a fitted finite-time plateau |
| Minimum depth shrinks within the stated joint domain | Same form with a changed coefficient | Not robustness to every fixed residual depth |
| Explicit increasing finite squares | Same law along a sufficient family | Size bound is conservative, not optimal |
| Fixed positive minimum or fixed finite square | Ultimate near-complete return | Different order of limits |

The logarithm belongs to the **local Green function**. The lower-edge density of states
is finite and nonzero; the middle-band van Hove singularity is a different feature.
The [spectral scope note](research/SPECTRAL_SCOPE.md) records this terminology correction
and the fixed-positive-anisotropy check. It does not claim a dimensional crossover.

## Read in three passes

| Pass | Document | Purpose |
|---|---|---|
| Physical account | [Consolidated core](research/CORE.md) | Model, observable, mechanism and boundaries |
| Claim-to-proof route | [Claim map](research/CLAIMS.md) | Which derivation and numerical controls support each claim |
| Full technical audit | [Asymptotic](research/ASYMPTOTIC.md), [boundary audit](research/AUDIT.md), [rounding](research/ROUNDING.md) | Check the matching, normalization and finite physical window |

[Prior art](literature/PRIOR_ART.md) identifies the close threshold predecessors;
the [Devdariani comparison](literature/DEVDARIANI_COMPARISON.md) updates its historical
primary-access gap without rewriting the preserved register. A
[separate-reader packet](research/READER_PACKET.md) exposes the four proof obligations;
it is not a completed review.
The [physical-amplitude lemma chain](research/AMPLITUDE_IDENTIFICATION.md) now supplies
an author-side retarded reconstruction, channel normalization and uniform tail comparison.
[Source labels](research/SOURCES.md) map the preserved notes' local reference numbers.
[Assumptions](literature/ASSUMPTIONS.md) distinguishes ideal model premises from a joint
apparatus, with a [primary-source register](literature/PHYSICAL_PRECEDENTS.md) and
[preparation/readout audit](research/PREPARATION_READOUT.md). The latter quantifies why
site occupation cannot simply replace the declared bound-state projector. The
[model-residual test](research/MODEL_RESIDUAL.md) distinguishes generator errors,
higher-band population and coherent return-amplitude errors. [Status](STATUS.md) and the [work order](work_orders/CURRENT.md) identify what
remains open. No external tutorial has been selected for this project.

## Reproduce without rewriting evidence

```sh
python -m pip install -r requirements.txt
python verify.py --integrity-only
python verify.py --output-dir verification-artifacts
```

There are five preserved scientific suites, with **28 groups and 272 finite controls**.
The runner writes to a new directory, retains observed outputs and complete comparisons,
and never replaces a saved reference. [Verification policy](provenance/README.md)
separates source integrity, assertion success, exact bytes and numerical agreement.
Neither code execution nor an author-side audit is independent proof review.

The [discrete archive](archive/README.md) preserves failed quadrature work and original
source/provenance records without putting obsolete code in the active test route.
The five core research notes and all original scientific scripts/results are imported
unchanged; this workspace integration adds navigation and verification, not a new theorem.

**Manuscript writing is on hold.** Collaboration inquiries are welcome; contact Ruge Lin.
The repository retains its [MIT license](LICENSE).
