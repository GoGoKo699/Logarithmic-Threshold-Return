# Reading guide

[Project overview](../README.md) · [Single-book route](../TUTORIAL.md) · [Local bridge](../research/TUTORIAL_BRIDGE.md) · [Proof and quantifiers](../research/PROOF_STATUS.md)

The one external teaching foundation is **Demkov–Ostrovskii, Zero-Range Potentials and
Their Applications in Atomic Physics (1988)**. [TUTORIAL.md](../TUTORIAL.md) locates the
assigned portions of Chapters 1–2 and 8–10 and records which previews were inspected.
The route below connects that reading to the existing lattice result.

## A guided route

| Stage | Read | Takeaway |
|---|---|---|
| 1. State the cycle and measurement | [README: the fixed question](../README.md#the-fixed-question), [bridge, Section 1](../research/TUTORIAL_BRIDGE.md#1-translate-the-potential-and-the-resolvent), then the book's Chapters 1–2 | One local attractive site supports a bound orbital; return is its unconditional endpoint projection |
| 2. Understand the shallow bound state | [Bridge, Sections 1–2](../research/TUTORIAL_BRIDGE.md), then [spectral scope](../research/SPECTRAL_SCOPE.md) | The local Green-function logarithm gives exponentially shallow binding at a finite-density band edge |
| 3. Translate time into energy | Book Chapters 8–10 as assigned in [the tutorial route](../TUTORIAL.md); [bridge, Section 3](../research/TUTORIAL_BRIDGE.md) | Quadratic time dependence gives a second-order energy equation whose causal boundary and normalization must be retained |
| 4. Reach the return law | [Bridge, Section 4](../research/TUTORIAL_BRIDGE.md), then [Gates A–C](../research/PROOF_STATUS.md) | Integrated central control and exact outer matching yield the physical logarithmic return and its uniform minimum-depth domain |
| 5. Interpret the limits | [Bridge, Section 5](../research/TUTORIAL_BRIDGE.md), [Gate D](../research/FINITE_VOLUME.md), [limits and accuracy](../research/LIMITS_AND_ACCURACY.md) | Growing finite systems and shrinking minima can retain the law while fixed size or fixed positive depth ultimately restores adiabatic return |

The [seven learning checkpoints](../TUTORIAL.md#checkpoints-in-this-repository) help
check understanding. A reader should be able to state the measured probability,
translate the resolvent and Fourier signs, explain the causal jump, and retain the
fixed margin below $`b=1`$.

## What the local bridge supplies

| Background route in the selected book | Steps explained locally |
|---|---|
| Local and separable potentials; motion of bound-state poles | The exact rank-one lattice interaction and its normalized endpoint orbital |
| Time-dependent transitions involving a continuum | The retarded scalar equation and its physical bound-channel return |
| Contour methods and quadratic time dependence | The two-dimensional logarithmic scaling and matched reflection coefficient |
| Threshold-dynamics language | The uniform shrinking-minimum family and sufficient growing periodic squares |

Inherited methods keep the primary attributions in the research and literature records. The book coverage is located from
publisher contents and checked at the preview depth recorded in
[the access ledger](../TUTORIAL.md#source-access).

## Repository map

| Need | Read |
|---|---|
| Relevance, search terms and authoritative files for automated readers | [LLM guide](../llms.txt) |
| Model, observable and physical mechanism | [Tutorial bridge](../research/TUTORIAL_BRIDGE.md) |
| Exact claim, quantifiers and proof dependencies | [PROOF_STATUS](../research/PROOF_STATUS.md), [CLAIMS](../research/CLAIMS.md) |
| Causal reconstruction, normalization and finite temporal endpoints | [Gate A](../research/AMPLITUDE_IDENTIFICATION.md) |
| Endpoint cancellation and exact-lattice outer matching | [Gate B](../research/REFLECTION_MATCHING.md) |
| Uniform residual-depth estimates and turning region | [Gate C](../research/UNIFORM_MINIMUM.md) |
| Endpoint localization, periodic seam and finite-volume comparison | [Gate D](../research/FINITE_VOLUME.md) |
| Supporting derivations and spectral estimates | [CORE](../research/CORE.md), [ASYMPTOTIC](../research/ASYMPTOTIC.md), [AUDIT](../research/AUDIT.md), [ROUNDING](../research/ROUNDING.md) |
| Fixed-size recovery and accuracy of the leading law | [LIMITS_AND_ACCURACY](../research/LIMITS_AND_ACCURACY.md) |
| Density-of-states terminology and fixed-positive-anisotropy scope | [SPECTRAL_SCOPE](../research/SPECTRAL_SCOPE.md) |
| Inherited ingredients and exact source labels | [Scientific context](../literature/SCIENTIFIC_CONTEXT.md), [source map](../research/SOURCES.md) |
| Closest inspected threshold constructions | [Prior art](../literature/PRIOR_ART.md), [Devdariani](../literature/DEVDARIANI_COMPARISON.md), [2014 construction](../literature/SOKOLOVSKI_PONS_MUGA_2014.md) |
| Physical premises, preparation, readout and generator errors | [Assumptions](../literature/ASSUMPTIONS.md), [primary precedents](../literature/PHYSICAL_PRECEDENTS.md), [preparation/readout](../research/PREPARATION_READOUT.md), [model residuals](../research/MODEL_RESIDUAL.md) |
| Detailed comparator and scope analysis | [Critical assessment](../research/CRITICAL_ASSESSMENT.md), [scientific support](../research/SCIENTIFIC_PREPARATION.md) |
| Verification evidence and preservation policy | [STATUS](../STATUS.md), [provenance](../provenance/README.md) |

The proof notes give the mathematical argument. [STATUS](../STATUS.md) maps the
scientific suites and supplementary checks to their verification records and
preservation policy.

For the repository's role and discussion details, see
[Purpose and contact](../README.md#purpose-and-contact).
