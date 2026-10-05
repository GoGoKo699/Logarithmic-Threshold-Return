# Critical assessment of the fixed logarithmic-return argument

**5 October 2026. Author-side assessment, not an independent report or manuscript.**
Assessed base: `5f372c4809973771db78847f773bec61ddce377f`, tree
`56f699c6f336a43998782121382cbde3afc892ba`. The materials were the full A-D
expansions, CORE, the claim/dependency map, the protected asymptotic, audit and
rounding notes, and the scoped predecessor comparisons. This note records a
cross-check of their connections and a sharper novelty challenge, not a Gate E.

## Decision first

No counterexample, coefficient change or domain change was found in the specific
checks below. The conditional author-side law is retained. This is not a certificate
for every sentence of the historical notes or a substitute for separate reading.

The strongest originality objection is now more explicit: the existing power-law
tangent predicts **the entire leading positive-minimum prefactor**, not only the
zero-minimum constant. Therefore neither that constant nor its residual-depth factor
should be sold as a separate discovery. The contribution to assess is the controlled
logarithmic limit for the fixed physical cycle, including its stated joint domain.
A familiar heuristic prediction does not automatically supply its error estimates;
conversely, technical error control alone does not establish broad significance.

## 1. Do the four arguments actually connect?

Use the notation of [PROOF_STATUS](PROOF_STATUS.md) and fix $`0<\delta\le1`$.
The following potential objections were checked against the displayed derivations.

| Objection | Passage checked and outcome | Boundary retained |
|---|---|---|
| A remote-time Fourier asymptotic is being used uniformly in a slow parameter without justification | Gate A Sections 2-5 first reconstruct at fixed $`\alpha,u`$; a different, uniform gapped-tail bound subsequently compares finite cycles. Gate C Section 1 eventually places every allowed $`u`$ in one fixed $`[0,u_*]`$. No joint stationary-phase limit is needed. | The norm reconstruction, including shared reciprocal-log coefficients on both sides of each spectral singularity, remains a load-bearing author-side argument. |
| Unknown phases invalidate composition of A, C and D | A compares amplitude moduli; C determines the auxiliary modulus up to a unit phase; D compares finite/infinite amplitudes in the common positive-real endpoint convention. Reverse triangle inequalities join them without identifying their complex phases. | No theorem for the full complex return amplitude across all representations follows. |
| The narrow positive-minimum turning region or a sign assumption invalidates uniformity | Gate C Section 2 integrates the whole central core with $`k\ge\sqrt\delta`$. Section 3 uses passivity and a denominator bound, not the sign of $`\operatorname{Im}h`$. Section 4 controls $`W-u`$ over the entire negative tail. | $`\delta`$ is fixed. The parameter $`b`$ indexes cycles; it is not varied during a cycle. |
| Finite volume silently changes the initial state or needs a gap during touching | Gate D Sections 2-5 keep distinct binding energies and normalized states, bound their mismatch, and use a seam/propagation estimate whose constants do not involve the minimum instantaneous gap. | The specified increasing torus is sufficient, not necessary, and no fixed-volume slow limit is interchanged. |

The matching radius $`L^{1/4}`$ in B-C and the physical square radius
$`\lceil4.5T\rceil`$ in D are different cutoffs. Their reused local letter $`R`$
is not an equality of scales. Likewise, the local positive-energy cutoff $`L^2`$
is not a physical volume or an implementation resource.

For clarity, the complete error composition can be written in one line. Set

```math
m_{L,b}=\frac{\pi}{2L(1-b)},\qquad
h_{L,b}=C_\delta L^{-5/4}+\frac{C_{u_*}}{T(L,b)}
+2\mathcal B_{1/2}(T(L,b),\lceil4.5T(L,b)\rceil).
```

The cited A, C and D estimates imply, for sufficiently large $`L`$,

```math
\left|\sqrt{P_{n(T)}}-m_{L,b}\right|\le h_{L,b},\qquad
\left|\frac{P_{n(T)}}{m_{L,b}^2}-1\right|
\le2\frac{h_{L,b}}{m_{L,b}}+
\left(\frac{h_{L,b}}{m_{L,b}}\right)^2.
```

Since $`m_{L,b}\ge\pi/(2L)`$, $`T^{-1}=O(e^{-L}/\sqrt L)`$ uniformly,
and $`\mathcal B\le K(1+T)e^{-\gamma T}`$, the ratio $`h/m`$ is
$`O_\delta(L^{-1/4})`$. Dropping the last term in $`h`$ gives the infinite-lattice
case. This is just composition of the existing estimates, not a new remainder
optimization or a finite-time confidence interval. None of these implications
uses numerical norm conservation as proof of scattering boundary conditions.

## 2. The sharper power-law objection

[AUDIT Section 7](AUDIT.md) already contains the standard-Bessel comparator

```math
P_\sigma=4\cos^2\!\left(\frac{\pi}{2+\sigma}\right),\quad 0<\sigma<1,\qquad
P_\sigma=\frac{\pi^2\sigma^2}{4}+O(\sigma^3),\quad \sigma\downarrow0.
```

It belongs to the second-order **energy-coordinate** power problem, not directly
to a well with arbitrary time-ramp exponent. This formula is inherited comparison
material, not a new physical law or an identity attributed here to an unread paper.
The relevant Bessel connection formulas are standard [R3].

The following algebra makes the objection cover positive minimum as well. Use only
the local logarithmic approximation on the negative axis:

```math
W_{\log}(\eta)=\frac1{\rho_0\ln(32/\eta)},\qquad
K_{\log}(\eta)=W_{\log}(\eta)-u,\qquad
\eta=e_*=32e^{-L},\quad u=\frac b{\rho_0L}.
```

At this scale the logarithmic slope is exactly

```math
\sigma_{\rm eff}
=\left.\frac{d\ln K_{\log}}{d\ln\eta}\right|_{\eta=e_*}
=\frac1{L(1-b)}.
```

The comparator's domain is satisfied uniformly once $`L>\delta^{-1}`$, since
$`\sigma_{\rm eff}\le1/(\delta L)`$. Freezing this slope formally predicts

```math
\frac{\pi^2\sigma_{\rm eff}^2}{4}
=\frac{\pi^2}{4L^2(1-b)^2}.
```

Thus the entire leading prefactor is understandable from the old local tangent.
This is a heuristic explanation, not a globally equivalent Hamiltonian or proof.
One can see the failure of global equivalence directly. With the same retarded
$`V=\ln|x|-i\pi\mathbf1_{x>0}`$ as B-C, compare

```math
\frac{L/(L-V)-b}{1-b}
\quad\hbox{and}\quad
\exp\!\left[\frac{V}{L(1-b)}\right].
```

They agree through first order, but their second-order difference is
$`(1-2b)V^2/[2L^2(1-b)^2]`$. Its vanishing at the particular value $`b=1/2`$
does not make the two functions identical. More importantly, this expansion is
not uniform at the singular core or through the remote physical band. The
logarithmic local approximation itself is not the full lattice resolvent.
A slope substitution supplies none of A's norm reconstruction, B-C's causal and
far-band error control, or D's finite-volume comparison. Those remain the actual
work needed for the conditional physical statement.

Three one-off exact symbolic checks verify the slope, the small-power coefficient,
and this second-order difference. Their code and output are retained in the
conversation evidence, not installed as another scientific suite or CI gate.

## 3. Exact scope of the closest fixed-power predecessor

Sokolovski-Pons 2015 supplies the Sturmian/reflection framework [R1]. In the 2016
paper, Section VII Eq. (24) assumes $`E_n(vt)\approx-C|vt|^{2\nu}`$ with a fixed
finite power; Eqs. (25)-(27) use it to obtain the limiting return [R2].

Our zero-minimum gap, expressed in the original slow coordinate $`s=t/T`$, is

```math
\eta(s)\sim32e^{-\pi/s^2},\qquad
\frac{\eta(s)}{|s|^{2\nu}}\longrightarrow0
\quad\text{for every fixed finite }\nu>0.
```

The limit follows by taking its logarithm: $`-\pi/s^2`$ dominates
$`-2\nu\ln|s|`$. No finite nonzero coefficient $`C`$ gives the displayed
predecessor hypothesis. Taking a duration-dependent effective exponent and then
exchanging limits is an additional problem, not a direct application of that
fixed-power result. This checks a precise possible subsumption; it does not
exclude other predecessors or establish exhaustive priority.

There is also a direct attribution addition: Eq. (5) of [R2] already expresses
return using the midpoint integral $`|\int\Psi(x,0)^2dx|^2`$. Gate D's transpose
identity is its lattice/operator counterpart, not a new return-measurement idea.
This assessment adds the direct attribution; Gate D's proof is unchanged.

## 4. What remains after the objections

The defensible central statement is a **controlled marginal, logarithmic-threshold
return law for the specified single-particle cycle, with its stated positive-minimum
and finite-volume joint limits**. Threshold loss, the spectral logarithm, the energy
transform, the midpoint identity, the local power-law heuristic and generic
localization/error inequalities are not separate originality claims.

This remains a potentially useful theoretical result: it distinguishes vanishing
logarithmic return from the fixed-power comparator's duration-independent return,
while keeping the exact observable and order of limits explicit. Whether that
extension changes enough physical understanding for a broad-audience paper is
still a significance judgment. No count of lemmas, controls or component citations
settles it. The current evidence supports neither a new experimental capability
nor a demonstrated application advantage.

**Phase decision:** retain the fixed core and stop routine proof expansion. The
assessed connections need no repair found in this pass. The next substantive input
should be an exact mathematical objection, a directly matching predecessor, or a
genuinely separate reader's reasoned assessment. Do not start an automatic new gate,
new model or numerical campaign merely to maintain activity. All four external
reader ratings remain unfilled. This assessment cannot serve as its own independent
review. Manuscript drafting, release and outside contact remain on hold.

## 5. Bounded significance follow-up

**5 October 2026, at `eb2ff9823e5c742ceb92e1625d857780141a4101`, tree
`7471a6fb06b072abe8f12bbf6047db7e76e940e7`.** This follow-up tests the physical
increment, not the proofs again. The additional internal readings are not separate
expert reports. The earlier assessed revision and its findings remain as recorded.

The strongest physical statement survives two idealization objections. Choose a
fixed $`0<b_0<1`$, set $`u=b_0/(\rho_0L)`$ and use the existing $`T(L,b_0)`$
and sufficient finite squares $`n(T)=2\lceil4.5T\rceil+1`$. Then
$`P_{n(T)}\sim\pi^2/[4L^2(1-b_0)^2]\to0`$. Every member is finite and has
strictly positive attraction throughout; its ground state remains isolated.
Exact threshold touching is therefore unnecessary along this specified family.
Depth and volume change with duration. The statement does not contradict return
to one for a fixed positive minimum or a fixed finite square in its slow limit.

There is a useful physical reading of the residual-depth factor. The
**infinite-lattice** minimum binding energy obeys
$`\eta(u)\sim32e^{-L/b_0}`$, while $`e_*=32e^{-L}`$. Consequently

```math
\frac{\eta(u)}{e_*}\sim e^{-L(1/b_0-1)}\longrightarrow0,
\qquad
\frac{P_\infty(T,u(T))}{P_\infty(T,0)}\longrightarrow\frac1{(1-b_0)^2}.
```

The probabilities in the ratio have the same half-duration; their implicit
logarithmic scales have ratio tending to one. A binding energy exponentially
below the dynamical energy scale can thus change the leading return by a finite
relative factor. Both probabilities still vanish. This is a corollary of the
existing law and static weak binding, also predicted by the frozen-slope
heuristic; it is not another mechanism or an application advantage. The
finite-volume comparison does not equate $`\eta(u)`$ with the torus's minimum
instantaneous gap. The excluded boundary $`b=1`$ is not a proved crossover.

A concrete general-theorem check also leaves the result intact. Avron-Elgart's
Theorem 4 [R4] assumes a finite-rank spectral projection with piecewise second
derivatives and continuity everywhere in operator norm. At zero attraction the
infinite lattice has no normalizable threshold eigenstate to continue the bound
projection. Hence that theorem does not subsume this touching cycle. Applying a
fixed-family theorem separately at each positive $`u`$ also supplies no uniform
shrinking-minimum estimate. This is a hypothesis comparison, not a claim about
every gapless adiabatic theorem. Tolstikhin's broader method paper [R5] was
available only at abstract depth; construction-level exclusion remains unwarranted.

**Assessment unchanged:** the controlled marginal return and its joint domain are
the defensible contribution. They establish when an anticipated asymptotic is a
physical return law. The leading prediction itself remains available from the
local power tangent. This pass found no additional conceptual consequence that
resolves the broad-significance objection, and no concrete defect requiring repair.
Preserve the fixed result and the existing stop boundary. A genuinely separate
reader's reasoned assessment could change the judgment; more internal controls or
rewordings do not. No manuscript, release or outside contact was initiated.

## Primary sources and actual access depth

[R1] D. Sokolovski and M. Pons, PRA **92**, 042121 (2015),
[arXiv:1506.04019](https://arxiv.org/pdf/1506.04019). Parsed full text retrieved;
this pass does not upgrade the earlier detailed comparison or its access record.

[R2] D. Sokolovski and M. Pons, PRA **94**, 013410 (2016),
[arXiv:1603.08718](https://arxiv.org/pdf/1603.08718). Parsed passages around
Eq. (5), Eqs. (18)-(20), and Eqs. (24)-(27) checked. Screenshot requests failed
with cache misses; no successful visual rereading is claimed. The parsed PDF has
an inconsistent generated date line; attribution follows its arXiv identifier and
published record, not that line. These source-specific observations are scoped.

[R3] NIST DLMF [Section 10.4](https://dlmf.nist.gov/10.4), connection formulas:
HTML accessed for the inherited special-function identities, not a new physical
predecessor or selected tutorial. The comparator itself is the retained author-side
calculation in AUDIT Section 7.

[R4] J. E. Avron and A. Elgart, *Adiabatic Theorem without a Gap Condition*,
[arXiv:math-ph/9805022](https://arxiv.org/pdf/math-ph/9805022), version 4.
Parsed PDF retrieved in the follow-up; Theorems 1, 3 and 4 and the opening of
Section 6 checked. Theorem 4 is on printed p. 16. This is a targeted hypothesis
check, not a complete reproof or a new rate result.

[R5] O. I. Tolstikhin, PRA **77**, 032711 (2008),
[publisher abstract](https://journals.aps.org/pra/abstract/10.1103/PhysRevA.77.032711).
Only the abstract was accessible in the follow-up. It describes generalized
Born-Fock equations and leading ejected-particle spectra for underbarrier and
overbarrier evolution. Exact applicability to essential-threshold recapture was
not established from this access. The bounded search found no direct match but
does not exclude one or improve the priority assessment.

**Later access update:** [SCIENTIFIC_CONTEXT](../literature/SCIENTIFIC_CONTEXT.md)
records the subsequent parsed author-uploaded full text and its scoped turning-point
comparison. The abstract-only R5 description above records this assessment's earlier
access, not the current reading state. The 2014 predecessor remains access-limited.

Targeted searches beyond these records did not identify a directly matching
logarithmic-return theorem, but also produced irrelevant results. This is not
evidence of absence. No third-party PDF is stored or redistributed, no external
contact was made, and no protected source or saved numerical value was changed.
