# Logarithmic Threshold Return

**A trap driven toward its binding threshold can lose almost all bound-state return as its cycle becomes arbitrarily slow.**

One particle starts bound to a single attractive site on a two-dimensional square lattice.
The attraction is weakened and restored along the same quadratic schedule. The question
is how much returns to the original bound orbital after this coherent, closed cycle.

| Read next | Purpose |
|---|---|
| [Reading guide](docs/README.md) · [Single-book route](TUTORIAL.md) · [Tutorial bridge](research/TUTORIAL_BRIDGE.md) | Learn the model and mechanism from one external book |
| [Proof and quantifiers](research/PROOF_STATUS.md) · [Claim map](research/CLAIMS.md) | Follow the return law and its proof dependencies |
| [Limits and accuracy](research/LIMITS_AND_ACCURACY.md) · [Assumptions](literature/ASSUMPTIONS.md) · [Prior-work comparison](literature/SCIENTIFIC_CONTEXT.md) | Check the asymptotic domain, physical premises and attribution |
| [Evidence and reproduction](#evidence-and-reproduction) · [Scope and evidence](STATUS.md) | Inspect the checks and their interpretation |
| [LLM guide](llms.txt) | Identify relevant questions and authoritative files |

## The fixed question

Measure energy in $`J`$ and time in $`\hbar/J`$. The Hamiltonian and return probability are

```math
\begin{aligned}
H(t)&=H_0-\left[u+(4-u)(t/T)^2\right]\lvert0\rangle\langle0\rvert,
\qquad -T\le t\le T,\\
P_\infty(T,u)&=\left|\langle b_4\rvert\mathcal U(T,-T)\lvert b_4\rangle\right|^2.
\end{aligned}
```

Here $`H_0`$ is the nearest-neighbor square-lattice Laplacian with band $`[0,8]`$,
$`\lvert b_4\rangle`$ is the normalized endpoint bound orbital, and $`T`$ is the
**half-cycle duration**. The endpoint attraction is 4 for every $`0\le u<4`$.
The measurement projects onto that orbital. Site occupation is a different observable.
The probability is unconditional; population that escapes remains in continuum states.

## The logarithmic return law

The leading slow-cycle law at exact touching is

```math
\boxed{P_\infty(T,0)\sim\frac{\pi^2}{4\ln^2T}\longrightarrow0.}
```

With units restored, the logarithm is
$`\ln(T_{\rm physical}J/\hbar)`$. [The proof map](research/PROOF_STATUS.md) gives the
exact quantifiers, and [limits and accuracy](research/LIMITS_AND_ACCURACY.md) explains
the remainder and finite-duration interpretation.

A trap with a shrinking positive minimum also retains the effect. Define

```math
\rho_0=\frac1{4\pi},\qquad
L+\tfrac12\ln L=\ln\frac{32T}{\sqrt{(4-u)\rho_0}},\qquad b=\rho_0uL.
```

For $`0\le b(T)\le1-\delta`$ with fixed $`0<\delta\le1`$, the uniform law is

```math
P_\infty(T,u(T))=
\frac{\pi^2}{4L^2[1-b(T)]^2}[1+o(1)].
```

A strictly positive minimum $`u=o(1/\ln T)`$ keeps the zero-minimum coefficient.
Along the sufficient periodic-square family $`n(T)=2\lceil4.5T\rceil+1`$, in the same
residual-depth domain, the law also holds using each lattice's own endpoint bound state.
The size is sufficient, not optimal, and the expansion does not apply at $`b=1`$.

| Limit | Return behavior |
|---|---|
| Infinite lattice, exact touching, then slow cycle | Vanishes as an inverse square logarithm |
| Shrinking minimum within the fixed-margin domain | Vanishes with the displayed minimum-dependent coefficient |
| Sufficient growing periodic squares in that same domain | Retains the logarithmic law |
| Fixed positive minimum or fixed finite square | Ultimately approaches adiabatic return |

These are different orders of limits. [Limits and accuracy](research/LIMITS_AND_ACCURACY.md)
explains why the joint family and fixed-gap recovery are compatible.

## Why a logarithm changes return

The lower-edge local Green function and weak binding obey

```math
G(\eta)=\rho_0\ln(32/\eta)+O\!\left(\eta\ln(1/\eta)\right),\qquad
\eta(U)\sim32e^{-4\pi/U}.
```

The gap becomes exponentially small at weak attraction. The lower-edge density of states
is finite and nonzero; the logarithm belongs to the local Green function. The middle-band
van Hove singularity is a separate feature. See [spectral scope](research/SPECTRAL_SCOPE.md).

Fourier transformation turns the quadratic rank-one drive into a scalar energy equation.
Its bound-channel reflection becomes weak in the logarithmic threshold limit. Retarded
reconstruction, equal channel normalization and controlled outer matching connect that
reflection to the physical return probability. The [local bridge](research/TUTORIAL_BRIDGE.md)
explains the steps; the [documentation map](docs/README.md#repository-map) locates their proofs.

## One tutorial, then this result

The selected learning foundation is:

> Yu. N. Demkov and V. N. Ostrovskii, **Zero-Range Potentials and Their Applications in Atomic Physics**, Plenum Press (1988).
>
> [Publisher record](https://link.springer.com/book/10.1007/978-1-4684-5451-2) · [DOI](https://doi.org/10.1007/978-1-4684-5451-2)

The [single-book route](TUTORIAL.md) focuses on Chapters 1–2 and 8–10, with precise
section locations, checkpoints and an access ledger covering the publisher contents
and inspected previews. The [tutorial bridge](research/TUTORIAL_BRIDGE.md) supplies
the lattice threshold, normalization, matching and joint-limit steps locally.

## Boundaries and prior work

The claim concerns one particle, one local square-lattice trap, the specified quadratic
cycle and unconditional orbital return. A bath, free waiting interval or postselection
changes the task. The [assumption map](literature/ASSUMPTIONS.md) and
[readout audit](research/PREPARATION_READOUT.md) distinguish the ideal Hamiltonian and
observable from an implemented device. Fixed positive anisotropy has a supporting
[scope check](research/SPECTRAL_SCOPE.md); its zero-hopping limit is not uniform.

Threshold-touching loss, static essential binding and the energy-domain method have
predecessors. A local power-law tangent predicts the leading prefactor; the contribution
is the controlled logarithmic physical limit and its joint domain.
[Scientific context](literature/SCIENTIFIC_CONTEXT.md), the
[Devdariani comparison](literature/DEVDARIANI_COMPARISON.md) and the
[2014 construction comparison](literature/SOKOLOVSKI_PONS_MUGA_2014.md) give the attributions.
[Scope and evidence](STATUS.md) connects the result to its supporting records.

## Evidence and reproduction

```sh
python -m pip install -r requirements.txt
python verify.py --integrity-only
python verify.py --output-dir verification-artifacts
```

The five preserved scientific suites cover **28 groups and 272 finite controls**.
The **60 supplementary checks** are counted separately. The runner writes to a fresh
directory, retains observed outputs and complete differences, and preserves saved references.
[Verification policy](provenance/README.md) distinguishes assertions, numerical agreement
and exact bytes.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

The [LLM guide](llms.txt) gives relevant questions, search terms and an authoritative
reading order. Code is available under the [MIT license](LICENSE).
