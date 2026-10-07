# Preparation and readout of bound-state return

This note derives calibration requirements for the bound-state projector in
[CORE](CORE.md). The [physical precedents](../literature/PHYSICAL_PRECEDENTS.md)
support individual components; applying them to the complete threshold cycle
requires the preparation, dynamics and readout bounds below.

## 1. An occupied site is not the endpoint bound orbital

Write $`P_b=|b_4\rangle\langle b_4|`$ and $`Q_0=|0\rangle\langle0|`$.
The rank-one bound-state equation already used in ASYMPTOTIC gives, with normalized
Brillouin-zone measure $`d\mu=d^2k/(2\pi)^2`$ and
$`\varepsilon(k)=4-2\cos k_x-2\cos k_y`$,

```math
I_j(\eta)=\int\frac{d\mu(k)}{[\varepsilon(k)+\eta]^j},\qquad
4 I_1(\eta_4)=1,\qquad
w=|\langle0|b_4\rangle|^2=\frac{I_1(\eta_4)^2}{I_2(\eta_4)}.
```

For $`z=4+\eta`$, the exact elliptic integrals are

```math
I_1=\frac{2K(16/z^2)}{\pi z},\qquad
I_2=-\frac{dI_1}{d\eta}=\frac{2E(16/z^2)}{\pi(z^2-16)}.
```

Here $`K`$ and $`E`$ use the parameter, not the elliptic modulus, convention.
The static calculation gives

```math
\eta_4\simeq1.045878167,\qquad w\simeq0.724043782,\qquad
\|Q_0-P_b\|=\sqrt{1-w}\simeq0.525315351.
```

The first two expressions follow by normalizing the resolvent vector. For the last,
write $`b_4=\sqrt w\,|0\rangle+\sqrt{1-w}\,|v\rangle`$ with
$`\langle0|v\rangle=0`$. In that two-dimensional span, $`Q_0-P_b`$ has trace zero
and determinant $`-(1-w)`$, hence eigenvalues $`\pm\sqrt{1-w}`$.

Thus even the exact endpoint bound state has only about 72.4% occupation at the
addressed site. A site-prepared state has the same bound-state fidelity, not unit
fidelity. The 0.525 figure is a **worst-case measurement discrepancy over arbitrary
states**, not an error predicted for the state reached by our quadratic cycle.
It does not bound the error of a properly calibrated orbital-sensitive measurement.

A stronger obstruction concerns the entire position histogram. The normalized states
$`b_4`$ and $`D_0b_4`$, where $`D_0=I-2Q_0`$, have identical probabilities at
every site, but their probabilities under $`P_b`$ are respectively

```math
1\quad\hbox{and}\quad |\langle b_4|D_0b_4\rangle|^2=(1-2w)^2\simeq0.20078.
```

This is an elementary counterexample to certification from a single spatial
histogram, not a claim that both states occur in the fixed cycle. Dividing the
origin count by $`w`$ does not repair the ambiguity for arbitrary continuum admixtures.

## 2. A sufficient error contract, with an explicit proof

All states and effects below use a specified common Hilbert space. A finite-volume
or higher-band embedding is part of an implementation comparison, not automatic.
Let $`\rho_{\rm p}`$ be the normalized prepared input and $`\rho_{\rm a}`$ the
normalized actual output before detection. Include a vacuum/lost-particle sector
when needed, extending $`P_b`$ by zero and the ideal unitary arbitrarily on that
sector. Let $`0\le M\le I`$ be the effective binary detector effect on the output.
The following quantities refer to the actual preparation, dynamics and effective
measurement, for which error bounds must be certified. A separate inverse-calibration
estimator needs its own error and statistical analysis; it is not automatically a
binary effect between zero and identity.

```math
\begin{aligned}
\epsilon_{\rm p}&=\tfrac12\|\rho_{\rm p}-P_b\|_1,\\
\epsilon_{\rm d}&=\tfrac12\|\rho_{\rm a}-\mathcal U\rho_{\rm p}\mathcal U^\dagger\|_1,\\
\epsilon_{\rm m}&=\|M-P_b\|,\\
|\operatorname{Tr}(M\rho_{\rm a})-P_\infty(T,u)|
&\le\epsilon_{\rm p}+\epsilon_{\rm d}+\epsilon_{\rm m}.
\end{aligned}
```

To prove the inequality, insert $`\operatorname{Tr}(P_b\rho_{\rm a})`$ and
$`\operatorname{Tr}(P_b\mathcal U\rho_{\rm p}\mathcal U^\dagger)`$ between the
two probabilities. The detector term is bounded by its operator norm. For either
state term, a traceless Hermitian difference has positive and negative parts with
equal trace $`\|\Delta\|_1/2`$; an effect between zero and identity therefore has
expectation difference no larger than that trace. Unitary conjugation preserves
trace norm. These observations give the three terms without an extra factor of two.
For pure preparations, infidelity $`f=1-|\langle\psi|b_4\rangle|^2`$ corresponds
to trace distance $`\sqrt f`$, not $`f`$.

Uniformly within the fixed $`b\le1-\delta`$ domain, the claimed return is of order
$`L^{-2}`$. Consequently

```math
\epsilon_{\rm p}+\epsilon_{\rm d}+\epsilon_{\rm m}=o(L^{-2})
```

is a **sufficient worst-case condition** for those uncertainties not to change its
leading relative coefficient. It is not a necessary laboratory precision bound:
state-specific estimates or structured calibrated errors can be much sharper.
A fixed absolute error budget alone cannot certify an indefinitely shrinking signal;
a finite experiment instead needs a stated signal-to-uncertainty window. No physical
coherence time, attainable error budget or laboratory size follows from this inequality.

## 3. Orbital calibration and the ensemble denominator

Preparation must certify the extended $`b_4`$ of the actual endpoint Hamiltonian,
including relative phases, contamination and its own yield. Cooling before the
cycle does not introduce a bath into the mathematical cycle; cooling during it would.
A valid reverse-loading readout would have to establish its effective effect near
$`P_b`$ on the relevant output states. An important favorable special case is an
independently justified unitary readout followed by ideal rank-one origin detection.
Then $`M=V^\dagger Q_0V`$ is rank one and the same projector calculation gives

```math
F_{\rm cal}=\langle b_4|M|b_4\rangle,\qquad
\|M-P_b\|=\sqrt{1-F_{\rm cal}}.
```

Thus a certified calibration on $`b_4`$ can bound this readout error under those
structural assumptions. Without them, a high response on one input does not determine
a general effect: $`M=I`$ accepts $`b_4`$ perfectly but also accepts every orthogonal
state. Reversing a parameter schedule alone does not establish the required mapping.

The ensemble denominator must be fixed at the declared start. Initial heralding can
define that ensemble, with loading cost reported separately. Later survival filtering
changes the observable: if loss probability is $`q`$, then
$`p_{\rm raw}=(1-q)p_{\rm conditional}`$. Escape into the lattice continuum is not
loss to an unobserved environment. Site pinning, fluorescence and motional spectroscopy
must each be assigned to preparation, evolution or detection rather than conflated.

## Numerical diagnostics

`python tools/test_operational_contract.py --output NEW_PATH.json` performs six small
checks: elliptic/integral agreement, finite static endpoint states, projector distance,
the equal-histogram counterexample, the trace-distance inequality, and ensemble/error
conventions. It checks 17-, 33- and 65-site-side periodic **static** states; it does not
propagate a threshold cycle or extend the original 28-group / 272-control suite.
The values above are numerical diagnostics, not interval-certified constants.
