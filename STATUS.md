# Scope and verification

The result is logarithmically vanishing bound-state return for the specified
quadratic cycle of one attractive site on a square lattice. The
[proof map](research/PROOF_STATUS.md) states the exact uniform law and assembles
its four components. The [reading guide](docs/README.md) connects the selected
book to that argument.

## Scope of the result

| Part of the argument | Derivation | Domain and interpretation |
|---|---|---|
| Energy reflection and physical return | [A: physical amplitude](research/AMPLITUDE_IDENTIFICATION.md) | Retarded norm reconstruction, equal channel normalization and a uniform finite-endpoint amplitude-modulus estimate |
| Logarithmic reflection and outer matching | [B: reflection matching](research/REFLECTION_MATCHING.md) | Exact touching; both causal contributions and exact-lattice tail estimates |
| Shrinking positive minimum | [C: uniform minimum](research/UNIFORM_MINIMUM.md) | Fixed $`0<\delta\le1`$ and $`0\le b\le1-\delta`$ |
| Growing periodic squares | [D: finite volume](research/FINITE_VOLUME.md) | Each square's own endpoint orbital; sufficient side $`n(T)=2\lceil4.5T\rceil+1`$ in the same minimum-depth domain |
| Fixed size or fixed positive minimum | [Limits and accuracy](research/LIMITS_AND_ACCURACY.md) | Ultimate adiabatic return; constants can depend on size and gap |
| Fixed positive hopping anisotropy | [Spectral scope](research/SPECTRAL_SCOPE.md) | Supporting result with a nonuniform zero-transverse-hopping limit |

The proof controls a leading asymptotic. Its remainder and resolution of
subleading logarithms are explained in [limits and accuracy](research/LIMITS_AND_ACCURACY.md).
The finite-size bound is sufficient rather than optimal.

## Attribution and physical assumptions

Static essential binding, threshold loss, the energy-domain method and localization
have established precedents. The local power-law tangent predicts the leading
prefactor; the controlled physical limit and joint domain are developed in the
proof notes. [Scientific context](literature/SCIENTIFIC_CONTEXT.md), the
[Devdariani comparison](literature/DEVDARIANI_COMPARISON.md) and the
[2014 construction comparison](literature/SOKOLOVSKI_PONS_MUGA_2014.md) record the
specific source statements and access depths. [The critical assessment](research/CRITICAL_ASSESSMENT.md)
contains the detailed tangent calculation and cross-component error composition.

The model assumes pure endpoint preparation, closed coherent evolution and
unconditional projection onto the endpoint orbital. [Physical premises](literature/ASSUMPTIONS.md)
maps those conditions to component precedents and calibration requirements.
[Preparation/readout](research/PREPARATION_READOUT.md) and
[model residuals](research/MODEL_RESIDUAL.md) derive sufficient error bounds.

## Verification and preserved evidence

The five scientific suites cover **28 groups and 272 finite controls**. The
**60 supplementary checks** comprise 14 infrastructure, five predecessor,
six operational, seven model-residual, seven amplitude, six reflection,
seven uniform-minimum and eight finite-volume checks.

The runner retains observed outputs and all differences in a fresh directory.
[Verification policy](provenance/README.md) distinguishes scientific assertions,
reference agreement under the recorded policy and exact byte identity. The
[hosted workload review](provenance/HOSTED_IMPORT_REVIEW.json) preserves the
source-derived interpretation of suite 07's ODE work counters.
Workflow runs retain the checked source snapshots, observed outputs and comparisons.

All **27 mapped scientific/history inputs** are preserved according to
[IMPORT_MAP](provenance/IMPORT_MAP.json).
For fresh execution, use the [reproduction commands](README.md#evidence-and-reproduction).
