# Scientific context and inherited ingredients

**5 October 2026. Internal research record, not a manuscript or independent review.**
This bounded source pass accompanies the fixed author-side result assessed at
`88b633f040bb075b6717c6306fe88d541c718924`. It updates access and attribution;
it does not change the model, coefficient, asymptotic domain or numerical policy.
The earlier comparisons remain in [PRIOR_ART](PRIOR_ART.md), with the later
[Devdariani construction reading](DEVDARIANI_COMPARISON.md) and
[critical assessment](../research/CRITICAL_ASSESSMENT.md) taking precedence where
they explicitly update historical access states.

## 1. What is inherited, and what is actually established here

| Ingredient | Primary attribution and actual access | Use and boundary |
|---|---|---|
| Square-lattice Green function | Guttmann, J. Phys. A **43**, 305205 (2010), [preprint](https://arxiv.org/pdf/1004.1435), Section 1, Eqs. (1), (2), (4), (6): parsed full text; PDF p. 2 visually checked | Established Bloch-integral and elliptic evaluation. Translate normalization and elliptic convention explicitly; the rectangular formula is derived in [SPECTRAL_SCOPE](../research/SPECTRAL_SCOPE.md). |
| Essential two-dimensional weak binding | Simon, Ann. Phys. **97**, 279–288 (1976), [DOI](https://doi.org/10.1016/0003-4916(76)90038-5), [author scan](https://math.caltech.edu/SimonPapers/70.pdf), Section 3, Theorem 3.4: printed pp. 279, 286–288 visually inspected | Under its potential hypotheses, the continuum weak-coupling binding scale is exponential. This is historical physical context; it does not supply the lattice constant 32 or a dynamic return law. |
| Fixed-gap adiabatic recovery | Jansen–Ruskai–Seiler, J. Math. Phys. **48**, 102111 (2007), [v3](https://arxiv.org/pdf/quant-ph/0603175), Section II assumptions, Theorem 3, Eq. (6) and following estimate, printed pp. 4–5: parsed full text | A separated spectral sector and bounded Hamiltonian derivatives give a gap-dependent leakage estimate. [LIMITS_AND_ACCURACY](../research/LIMITS_AND_ACCURACY.md) supplies the fixed-size compact-parameter application; constants are not uniform in growing volume. |
| Gapless adiabatic theorem | Avron–Elgart, Commun. Math. Phys. **203**, 445–463 (1999), [v4](https://arxiv.org/pdf/math-ph/9805022), Theorems 1, 3, 4: relevant full-text statements inspected | Smooth finite-rank spectral projections remain required; the piecewise version retains continuity. The infinite-lattice touching state has no norm-continuous bound projection. A closing gap alone is not a universal explanation of failure. |
| Exponential localization methodology | Combes–Thomas, Commun. Math. Phys. **34**, 251–270 (1973), [publisher](https://link.springer.com/article/10.1007/BF01646473): metadata and abstract only | Historical attribution only, not theorem authority for the lattice estimates. [FINITE_VOLUME](../research/FINITE_VOLUME.md) derives the weight, seam, initial-state and Duhamel estimates directly. |
| Density singularity terminology | Van Hove, Phys. Rev. **89**, 1189–1193 (1953), [publisher](https://journals.aps.org/pr/abstract/10.1103/PhysRev.89.1189): metadata and abstract only | Historical saddle-point terminology only. The lower-edge density and middle-band saddle location of this lattice follow from its displayed dispersion, not this abstract. |
| Rank-one impurity algebra | Direct eigenvalue equation, [CORE](../research/CORE.md) and [FINITE_VOLUME Section 2](../research/FINITE_VOLUME.md) | The scalar pole equation and uniqueness need no imported continuum theorem. The energy/Sturmian dynamic method remains credited to the predecessors in [PRIOR_ART](PRIOR_ART.md). |

## 2. Static normalization and the two different logarithms

Use the parameter convention explicitly:

```math
\mathbf K_{\mathrm{par}}(m)=\int_0^{\pi/2}\frac{d\theta}{\sqrt{1-m\sin^2\theta}},
\qquad K_{\mathrm{mod}}(k)=\mathbf K_{\mathrm{par}}(k^2).
```

With $`z=4/(4+\eta)`$, the square-lattice random-walk Green function translates as

```math
G(\eta)=\frac{P(0;z)}{4+\eta}
=\frac{2}{\pi(4+\eta)}K_{\rm mod}(z)
=\frac{2}{\pi(4+\eta)}\mathbf K_{\rm par}\!\left(\frac{16}{(4+\eta)^2}\right).
```

The modulus-to-parameter conversion is essential when using Guttmann's Eq. (4).
The conversion above is fixed by the Bloch integral and its even
small-$`z`$ expansion; it agrees with the repository's existing parameter formula.
[NIST DLMF 19.12.1, 19.12.3](https://dlmf.nist.gov/19.12), including
$`d(0)=2\ln2`$, gives the elliptic logarithm. These reference formulas were read
directly; DLMF is a formula reference, not an additional physical-precedent paper.
The resulting lattice normalization is

```math
G(\eta)=\frac1{4\pi}\ln\frac{32}{\eta}+O(\eta\ln(1/\eta)),
\qquad U G(\eta)=1,\qquad \eta(U)\sim32e^{-4\pi/U}.
```

The dispersion $`E(k)=4-2\cos k_x-2\cos k_y`$ is quadratic at its minimum,
so the edge density tends to $`1/(4\pi)`$. Integrating this finite density against
the resolvent denominator produces the threshold logarithm. The saddle points
$`(\pi,0)`$ and $`(0,\pi)`$ instead lie at energy 4 and produce the middle-band
density divergence. They are distinct singularities. The full retarded expansion
and fixed-anisotropy checks remain in [SPECTRAL_SCOPE](../research/SPECTRAL_SCOPE.md).

## 3. Tolstikhin 2008: the scoped full-text comparison

O. I. Tolstikhin, *Siegert-state expansion for nonstationary systems. III.
Generalized Born-Fock equations and adiabatic approximation for transitions to
the continuum*, Phys. Rev. A **77**, 032711 (2008):
[publisher](https://doi.org/10.1103/PhysRevA.77.032711),
[public author copy](https://www.researchgate.net/publication/235451669_Siegert-state_expansion_for_nonstationary_systems_III_Generalized_Born-Fock_equations_and_adiabatic_approximation_for_transitions_to_the_continuum).

The host identifies an author upload on 30 July 2015. Parsed full text was read:
Section II A, Eqs. (1)–(12); Section IV, Eqs. (42)–(43), (67); Section V,
Eqs. (76)–(87). PDF retrieval failed; no visual equation check is claimed.
The half-line model has a free exterior and common remote endpoint potential.
Its underbarrier analysis uses simple complex momentum zeros and separation;
its overbarrier analysis uses separated real zeros and an antibound interval.
Equation (86) includes initial-state survival, making this a recapture predecessor.

**Comparison inference:** the present touching scale
$`\sqrt{\eta(s)}\sim\sqrt{32}\exp[-\pi/(2s^2)]`$, $`s=t/T`$, is flat to every
finite power and cannot meet a simple-zero expansion. Those formulas therefore
do not supply this lattice result by substitution, or its shrinking-minimum
uniformity. This does not exclude an extension of the method. The access gap is
closed for this scoped comparison, not for an independent audit of that paper.

## 4. The 2014 construction comparison: targeted gap closed

Sokolovski–Pons–Muga, *Adiabaticity near a continuum threshold: An exactly solvable
model*, Phys. Rev. A **89**, 042125 (2014):
[publisher](https://link.aps.org/doi/10.1103/PhysRevA.89.042125),
[author-institution record](https://ekoizpen-zientifikoa.ehu.eus/documentos/5ed32bdf2999526aa7417480).
The user supplied the seven-page primary paper. Full text was read and decisive
pp. 2–6 were visually checked. The
[passage-level comparison](SOKOLOVSKI_PONS_MUGA_2014.md) supersedes the earlier
abstract-only status; failed retrievals remain historical evidence.

The protocol approaches a one-dimensional threshold monotonically with a linear
delta attraction, starting at remote past and stopping below threshold. Equation (26)
projects onto the normalized final bound state. The first-order energy equation (22)
and quadratures (24)–(28) establish inherited method and observable precedents.
Equation (29) takes the slow limit at fixed final binding. Criterion (31) concerns
stationary-phase separation for the amplitude, not a universal necessary condition
for high return probability; Eqs. (6), (32) are small-loss formulas. Section VII's
box analysis, Eqs. (36), (38)–(40), already supplies a finite-box/continuum contrast;
its Sturmian pole $`\omega_1`$ is not the final perturbed energy $`E_1(t_f)`$.

**Comparison inference:** these results do not supply the two-leg quadratic
logarithmic return law or its required joint uniform estimate. The specific
source-access/comparison task is closed, with stronger inherited attribution and
no central coefficient, model, domain or proof correction. This is not exhaustive
novelty clearance or a separate expert review. No outside contact was made.

## 5. What this preparation does and does not settle

The strongest local-power objection remains in [CRITICAL_ASSESSMENT](../research/CRITICAL_ASSESSMENT.md):
the frozen tangent predicts the full leading coefficient, including its residual-depth
factor. Controlled physical matching and the joint domain remain the contribution
to assess. [LIMITS_AND_ACCURACY](../research/LIMITS_AND_ACCURACY.md) records the
fixed-size recovery, remainder limits and comparator domain without adding a model.

Targeted searches through 5 October 2026 did not retrieve a directly matching
logarithmic-return theorem; irrelevant hits and failed searches have no exclusion
value. This record is not exhaustive priority clearance or a separate reader report.
It does not close the preparation, readout or apparatus gaps in
[ASSUMPTIONS](ASSUMPTIONS.md), and does not count mathematical citations as device
evidence. No third-party PDF, figure or full text is redistributed here.
