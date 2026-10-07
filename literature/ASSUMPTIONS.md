# Physical premises and calibration requirements

The [primary-source register](PHYSICAL_PRECEDENTS.md) records fifteen passage-level primary
comparisons (one caption-limited) and one abstract-only comparator. Source IDs below resolve there.
[Preparation and readout](../research/PREPARATION_READOUT.md) derives the distinction
between site occupation and the bound-state projector, and a sufficient error budget.
The [model-residual bound](../research/MODEL_RESIDUAL.md) makes the dynamical
comparison explicit, including basis motion, higher-band coupling and confinement.
The calibration requirements below connect the component precedents to the fixed
Hamiltonian and bound-state projector.

## Preparation and readout

| Premise | Passage-level component precedents | Calibration requirement |
|---|---|---|
| Prepare the endpoint bound orbital | Y22, W11, K12, T12, N18, Z16: six distinct preparation-related records, including spectroscopy and site selection | Certify the actual extended $`b_4`$, its phases, contamination, yield and preparation cost. An occupied site and a tweezer ground state are not the declared lattice input. |
| Measure unconditional bound-state return | Y22, W11, K12, T12, N18, S10, B22: seven distinct measurement/diagnostic records | Establish the effective orbital-sensitive effect and its errors for the output ensemble, including continuum admixtures. Position, sideband, internal-state and survival measurements are different observables. |

These counts describe preparation and diagnostic components, rather than demonstrations
of the exact state/projector. Y22 is the closest jointly demonstrated subset; the
source register records its model-specific differences.

The static calculation gives $`|\langle0|b_4\rangle|^2\simeq0.72404`$ at endpoint
depth 4. A fixed spatial histogram does not determine its bound-state probability.
Cooling or initial heralding can occur before the declared experiment with costs
reported separately. Filtering on survival after that start changes its denominator.

## Lattice dynamics and control

| Premise/resource | Component evidence | Calibration requirement or scope |
|---|---|---|
| Coherent single-particle lattice dynamics | Y22, W11, P15, WE23 and CH25: five passage-level motion records, including separately identified 1D and 2D walks | Establish the finite coherent window for this protocol. Position readout and survivor postselection are not unconditional orbital return. |
| Calibrated single attractive site, fixed quadratic schedule | Y22, W11, Z16, M17 and WE23: five addressing/shaping/control components with different signs, states or spatial profiles | Certify all projected matrix elements and their time dependence, not just a central light shift or static occupation threshold. |
| Single-band and nearest-neighbor description | J98, W11, Y22, L13 and C18: five framework/diagnostic records, including a PRL reduction audit | Bound in-band errors, higher-band coupling and any moving-basis term. Small leakage alone does not certify phase accuracy. |
| Other confinement and coherent area/time | J98, Y22, S10, Z16, L13 and M17: six records exposing or controlling background potentials | The sources include idealizations and finite-region compensation. Control the residual potential over the evolving state; a uniform density does not certify this. |
| Positive-minimum limit | Preserved ROUNDING proof with $`b\le1-\delta`$ | A joint limit is not immunity to a fixed residual depth. Full crossover remains unclaimed. |
| Fixed positive anisotropy | Preserved SPECTRAL_SCOPE proof and checks | Not uniform at zero transverse hopping; not evidence for arbitrary traps or extra bands. |
| Closed evolution and no incoming continuum population | Conditional source model and the preparation/detection distinction | Certify contamination and environmental channels without relabeling continuum escape as environmental loss or discarding outcomes. |

For a physical local beam, the projected perturbation is generally

```math
\delta h_{ij}=\int w_i^*(\mathbf r)\,V_{\rm loc}(\mathbf r)\,
 w_j(\mathbf r)\,d\mathbf r.
```

The single-site diagonal term is an assumption to test against those matrix elements
and higher-band couplings, not a consequence of the word addressing. J98 supplies
the reduction framework; it does not justify applying its smooth-potential
approximation to every focused beam. This is a calibration criterion, not a new model.

## Sufficient error budgets

The general operational probability bound applies to preparation, dynamics and readout.
Under the additional pure-input,
unitary-evolution and rank-one-readout assumptions, MODEL_RESIDUAL proves the sharper
bound $`|p-P|\le2\sqrt P\,d+d^2`$. A total vector error $`d=o(L^{-1})`$ is
sufficient in the fixed joint domain; the generic absolute-error condition
$`o(L^{-2})`$ remains sufficient without that structure. These are sufficient
analytical conditions, not necessary hardware tolerances. Applying them to an apparatus
requires calibrated orbital identification, matrix elements, phase/error bounds and a
coherent operating window. The pure input, closed evolution and absence of incoming
continuum specify the conditional model to which those calibrations must be compared.
