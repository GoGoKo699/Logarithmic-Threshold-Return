# From microscopic control to the fixed Hamiltonian: a residual test

**4 October 2026. Author-side calibration argument, not a new threshold law.**
The Hamiltonian, endpoint orbital and observable in [CORE](CORE.md) are unchanged.
This note supplies an explicit way to bound the dynamical error left abstract in
[PREPARATION_READOUT](PREPARATION_READOUT.md). It neither specifies hardware nor
claims that any cited experiment meets the bound. All norms below use $`\hbar=J=1`$.

## 1. Compare generators, not just populations or light profiles

Let $`H(t)`$ be the fixed lattice Hamiltonian and $`\psi(t)`$ its normalized ideal
solution, with $`\psi(-T)=b_4`$. Let $`h(t)`$ generate the actual unitary dynamics
on a physical Hilbert space. An explicitly chosen isometry $`B(t)`$ identifies
lattice orbitals with physical states, so $`B(t)^\dagger B(t)=I`$. The usual fixed
Wannier basis has $`\dot B=0`$; a moving basis must retain its derivative.

Assume the physical propagator exists, $`B(t)\psi(t)`$ lies in the required
operator domains and is absolutely continuous, and the residual below is integrable.
These hypotheses are automatic for the smooth finite matrices used in the tests;
they are not silently assumed for an arbitrary unbounded continuum Hamiltonian.
For any integrable real scalar $`c(t)`$, define

```math
D_c(t)=h(t)B(t)-B(t)[H(t)+c(t)I]-i\dot B(t),\qquad
\mathcal E_c=\int_{-T}^{T}\|D_c(t)\psi(t)\|\,dt.
```

The phase-adjusted reference $`\phi(t)=e^{-i\int_{-T}^t c(s)ds}B(t)\psi(t)`$
satisfies $`h\phi-i\dot\phi=e^{-i\int c}D_c\psi`$. Variation of constants and
unitarity give the exact sufficient bound

```math
\|U_h(T,-T)B(-T)b_4-e^{-i\int_{-T}^{T}c(s)ds}B(T)\psi(T)\|
\le\mathcal E_c.
```

Indeed, the difference solves an inhomogeneous Schrödinger equation with zero
initial value and forcing of norm $`\|D_c\psi\|`$; integrate its unitary propagator.
For the corresponding pure-state density matrices, trace distance is no larger
than this phase-adjusted vector distance. Thus $`\mathcal E_c`$ supplies a bound
for the earlier dynamical error when the input and Hilbert-space identification
match. Preparation error is added separately, not counted twice.

Subtracting $`c(t)I`$ removes a physically irrelevant common energy shift. It does
not remove gradients, site-dependent shifts, hopping changes or relative phases.
A large constant background is therefore not automatically a large control error.

## 2. Separate intra-band mismatch from coupling out of the chosen subspace

With $`P(t)=B(t)B(t)^\dagger`$, set

```math
K_c=B^\dagger hB-H-cI-iB^\dagger\dot B,\qquad
C=(I-P)(hB-i\dot B).
```

Then $`D_c=BK_c+C`$, with orthogonal ranges, and hence

```math
\|D_c\psi\|^2=\|K_c\psi\|^2+\|C\psi\|^2.
```

Here $`K_c`$ is Hermitian under the stated conditions. In a fixed Wannier basis,
the local-beam contribution to its matrix elements is

```math
\delta h_{ij}(t)=\langle w_i|V_{\rm loc}(t)|w_j\rangle
+U(t)\delta_{i0}\delta_{j0},\qquad U(t)=u+(4-u)(t/T)^2.
```

Background-potential matrix elements and deviations of the unperturbed band from
the assumed nearest-neighbor dispersion must also be included. The central
matrix element alone does not determine $`K_c`$. The off-subspace term $`C`$
contains higher-band couplings; in a moving basis both terms also include basis
motion. The reduction conditions in J98 and the time-dependent-basis correction
in L13 are recorded in [PHYSICAL_PRECEDENTS](../literature/PHYSICAL_PRECEDENTS.md).
L13's particular parity-symmetric single-band correction vanishes; this does not
justify deleting higher-band couplings or an arbitrary moving-basis term here.

For a Hermitian matrix with bounded absolute row sums, define
$`v=\sup_i|(K_c)_{ii}|`$ and $`j=\sup_i\sum_{k\ne i}|(K_c)_{ik}|`$.
The Schur bound gives $`\|K_c\|\le v+j`$. If $`\|C\|\le q`$, then

```math
\mathcal E_c\le\int_{-T}^{T}\sqrt{[v(t)+j(t)]^2+q(t)^2}\,dt.
```

This is a conservative, state-independent fallback. The state-dependent residual
can be much smaller. An unbounded harmonic envelope on the infinite lattice does
not satisfy the uniform row-sum premise. For a diagonal residual $`W_i-c`$ use
its actual weighted norm instead:

```math
\|(W-c)\psi\|^2=\sum_i|W_i-c|^2|\psi_i|^2.
```

For $`W_i=\kappa |i|^2`$ and $`c=0`$, this is
$`\kappa^2\langle |i|^4\rangle_\psi`$. A finite support bound is valid only for
a genuinely finite state or with the omitted tail separately controlled. A flat
image or a nearly uniform equilibrium density is not this dynamical certificate.

## 3. Small higher-band population does not certify the ideal return

The following elementary three-level example tests a purported calibration
criterion; it is not a new physical model for this project. Let $`N\ge2`$ be an integer,
$`\Omega=N/(N-1)`$, $`g=\tfrac12\sqrt{\Omega^2-1}`$, and use

```math
H_{\rm ref}=0\quad\text{on }\operatorname{span}\{|0\rangle,|1\rangle\},\qquad
h=\begin{pmatrix}0&0&0\\0&0&g\\0&g&1\end{pmatrix},\qquad
|s\rangle=(|0\rangle+|1\rangle)/\sqrt2.
```

The third state is outside the reference subspace. The coupled two-level block
has splitting $`\Omega`$, so its leakage probability is

```math
p_{\rm out}(t)=\frac12\left(1-\frac{1}{\Omega^2}\right)
\sin^2(\Omega t/2)\le\frac1N-\frac1{2N^2}.
```

At $`\tau=2\pi(N-1)`$ that leakage is exactly zero. The amplitude on $`|1\rangle`$
is multiplied by $`e^{-i\tau/2}(-1)^N=-1`$, while $`|0\rangle`$ is unchanged.
Thus actual return to $`s`$ is zero, although the reference predicts one and the
maximum population outside the subspace tends to zero as $`N\to\infty`$.
A coherent relative phase has accumulated. This disproves inference from leakage
alone, even when leakage is bounded throughout the interval. It does not preclude
a justified effective Hamiltonian that accounts for the accumulated phase.

## 4. A sharper sufficient budget when preparation and readout are coherent

The general density-matrix/effect bound in PREPARATION_READOUT remains valid.
A sharper bound is available under **additional structural assumptions**: pure
input $`a`$, unitary physical evolution, and a normalized rank-one detected orbital
$`m`$. Define the phase-minimized vector errors

```math
d_{\rm p}=\min_\theta\|a-e^{i\theta}B(-T)b_4\|,\qquad
d_{\rm m}=\min_\theta\|m-e^{i\theta}B(T)b_4\|,\qquad
d=d_{\rm p}+\mathcal E_c+d_{\rm m}.
```

Add and subtract the ideally embedded input/output amplitudes, use the residual
bound above and Cauchy--Schwarz, and remove their irrelevant endpoint phases. Then

```math
\left|\,|\langle m|U_h|a\rangle|-\sqrt{P_\infty(T,u)}\,\right|\le d,
\qquad
|p_{\rm actual}-P_\infty(T,u)|\le2\sqrt{P_\infty(T,u)}\,d+d^2.
```

The same proof applies first to the declared finite model; a finite-to-infinite
amplitude error from ROUNDING must be added explicitly before claiming $`P_\infty`$.
Uniformly for the existing $`b\le1-\delta`$ domain, $`d=o(L^{-1})`$ is sufficient
to preserve the leading relative coefficient. This is less restrictive than
using the general absolute-probability budget blindly, not a necessary accuracy
threshold or a laboratory feasibility result. A uniform residual bound $`\eta`$
would give $`\mathcal E_c\le2T\eta`$; it is not evidence that such a bound is attained.

Mixed preparation, unknown detector effects, dissipative evolution and additive
false positives still require the general error contract. For example, a fraction
$`r`$ of perfectly accepted incoherent contamination changes a signal $`P`$ to
$`(1-r)P+r`$. Small coherent-amplitude errors and small additive probabilities are
different guarantees. No detector, ramp, platform or postselection is introduced.

## Evidence and stop boundary

`python tools/test_model_residual.py --output NEW_PATH.json` checks seven small
identities/inequalities, including a short 5-by-5 fixed-cycle Duhamel check and the
analytic three-level counterexample. It does not perform an asymptotic campaign,
validate a microscopic apparatus or add members to the preserved 272 controls.

The missing experimental evidence is now specific: a common-space orbital
identification, in-band residual matrix elements, out-of-subspace coupling or an
error-controlled effective generator, and the background potential on the occupied
region. No checked source supplies those together for this exact protocol. The
conditional logarithmic claim and the separate-reader obligations are unchanged.
