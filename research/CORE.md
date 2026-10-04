# Logarithmic threshold return: the consolidated physical claim

**4 October 2026. Research-core note, not a submission manuscript or an independent report.** The main object is the fixed local square-lattice problem developed in scouts05–08. A new anisotropy check supports its spectral interpretation; it is not a second centerpiece.

## Question

If a trap is weakened until its bound state meets the continuum at one instant and then restored, does arbitrarily slow control retain a nonzero fraction of the initially bound particle?

The existence of loss in such protocols is established. The question here is the slow-cycle law at a logarithmic two-dimensional threshold, and whether that law has a controlled finite-system, imperfect-touching regime. No quantum speedup, many-body effect or absence of a classical-wave analogue is required. The physical dynamics are coherent single-particle Schrödinger evolution.

## One local Hamiltonian and one unconditional measurement

Set J=hbar=1. On the infinite square lattice,

```math
H_0=4I-\sum_{\langle x,y\rangle}(|x\rangle\langle y|+\mathrm{h.c.}),\qquad
H(t)=H_0-[u+(4-u)(t/T)^2]|0\rangle\langle0|.
```

The cycle is -T<=t<=T, and T is its **half duration**. The endpoint attraction is 4, independent of 0<=u<4. Start in its normalized bound state |b4> and measure return to the same state:

```math
P_\infty(T,u)=|\langle b_4|\mathcal U(T,-T)|b_4\rangle|^2.
```

There is no bath, free waiting interval, incoming continuum population, discarded outcome or normalization after escape. The missing return probability remains in continuum states. Reversing a parameter schedule is not reversing the full quantum dynamics. Site occupation is not automatically the bound-state return projector; an eventual experimental readout must implement or calibrate the declared measurement.

## The result and the noncommuting limits

Define rho0=1/(4 pi) and L through

```math
L+\tfrac12\ln L=\ln\frac{32T}{\sqrt{(4-u)\rho_0}},\qquad
b=\rho_0uL.
```

The recorded author-side derivation gives, uniformly for 0<=b<=1-delta with a fixed delta>0,

```math
\boxed{P_\infty(T,u(T))=
\frac{\pi^2}{4L^2[1-b(T)]^2}[1+o(1)].}
```

At exact touching, u=0, this becomes pi^2/(4 ln^2 T) to leading order and tends to zero. A positive minimum u=o(1/ln T) has the same leading coefficient; u of order 1/ln T with b tending to a constant below one changes the coefficient but preserves vanishing return. Every positive-minimum member has a bound state at all times.

A fixed nonzero u, by contrast, gives a fixed gap and ultimately returns with probability one. Likewise a fixed finite periodic lattice ultimately follows a discrete ground state even at u=0. The limits differ because the small gap and accessible volume are not held fixed in the joint family. This is not a violation of a gapped adiabatic theorem.

For the original isotropic model, an explicit sufficient finite side is n(T)=2 ceil(4.5T)+1. Along that sequence, with positive u(T) in the domain above, the same law holds. Its n^2=O(T^2) site count is a conservative construction, not a minimum laboratory size.

## Why a logarithm changes return

The static local resolvent has the threshold expansion

```math
g(\omega)=-\rho_0[\ln32-\ln(-\omega-i0)]+O(\omega\ln|\omega|).
```

The bound energy solves U[-g(-eta)]=1, so eta(U)~32 exp(-4 pi/U) at weak attraction. The gap is exponentially small rather than algebraic. The exact lattice Green function and essential weak binding are inherited facts, not the claimed dynamical contribution.

For the auxiliary parabola extended to all times, Fourier transformation of the contact amplitude gives the exact scalar equation

```math
c''+[-1/g(\omega)-u]c/\alpha=0,\qquad \alpha=(4-u)/T^2.
```

This is a rank-one specialization of the established energy/Sturmian method. The negative-energy wave branches represent the two bound-state trajectories and have equal stationary-phase normalization. Their reflection probability is the auxiliary bound return. Extra gapped temporal tails change the original finite-cycle amplitude by O(1/T).

At omega=e*x, with e*^2=alpha rho0 L and L=ln(32/e*), the threshold equation is

```math
y''+\left[\frac{L}{L-\ln(-x-i0)}-b\right]y=0.
```

For b below one this approaches a constant-coefficient equation away from its singular point, so its reflected amplitude becomes small. That is different from a scale-invariant finite-power threshold problem which retains a nonzero reflection coefficient. The leading probability is calculated, not inferred from a finite plateau.

## Proof spine and the steps a reader should challenge

On |x|<=R=L^(1/4), expand the coefficient in the integrated L1 sense around wave number sqrt(1-b). The logarithmic singularity is integrable even though a pointwise uniform Taylor expansion is false. The second-order transfer error is O_delta(R^2(1+ln R)^2/L^2).

Outside this interval, the exact reflection-coordinate equation and the retarded current half-plane bound control arbitrary passive far-band continuation. The integrated WKB defect is O_delta(1/(LR)); attenuation suppresses reflected information from distant band structure exponentially in L. Deep negative-energy propagation is controlled by the smooth resolvent and the absence of another outer turning point.

Matching in the local wave bases cancels artificial endpoint terms and leaves

```math
r=-\frac1{4L(1-b)}\int_{-R}^{R}
[\operatorname{PV}(1/x)-i\pi\delta(x)]e^{-2i\sqrt{1-b}x}\,dx+o(L^{-1})
=\frac{i\pi}{2L(1-b)}+o(L^{-1}).
```

Both the real logarithm and its causal imaginary jump contribute. Ignoring either the central singularity or its branch discontinuity gives an incorrect leading coefficient. Squaring and including the O(1/T) gapped-tail comparison gives the stated law.

For finite volume, initial endpoint bound states are uniformly exponentially localized. A weighted hopping bound and a seam Duhamel estimate give

```math
\|E_n\psi_n(0)-\psi_\infty(0)\|
\le C_\mu(1+T)e^{4\sinh\mu\,T-\mu R},\qquad n=2R+1.
```

The real, even-time Hamiltonian yields return amplitude psi(0)^T psi(0). Choosing mu=1/2 and the stated side length makes finite-volume error negligible beside 1/L. The proof includes the finite/infinite initial-state difference; it does not assume the initial vector is compactly supported.

The detailed matched argument, its audit and rounding proof are preserved in the evidence archive. This compact spine exposes rather than replaces the main proof obligations: the energy-to-time normalization, passive outer matching, endpoint comparison and uniform limits. No independent reader has verified them.

## Finite evidence and what its percentages mean

In the prior validated scout, u=0.1 and full duration 600 give return about 2.600280% on a 385-by-385 periodic square, compared with 2.600265% in the infinite-lattice spectral calculation. The same small minimum on a 17-by-17 square instead returns about 99.9991%. All are finite-time, closed-system calculations, not hardware performance or values inferred from the leading asymptotic.

The leading formula converges slowly. It is not an accurate percentage prediction at every accessible duration. Full finite-time propagation and scalar large-L calculations have distinct purposes and remain labeled separately. Norm conservation alone did not establish quadrature resolution; a failed development grid and its correction remain in the parent evidence.

## What supports the physical interpretation

The added fixed-anisotropy check in SPECTRAL_SCOPE.md changes only the positive hopping strengths along x and y. Their exact lower-edge density and logarithmic scale change, but the same matching hypotheses hold and the leading pi^2/4 coefficient survives. This is not uniform as one hopping vanishes, and not a theorem for arbitrary traps or dimensional crossover. It checks that the result does not require coincident square-lattice saddles or fourfold hopping symmetry.

The single-site, single-particle construction is the minimal object of interest, not a claim made impressive by increasing system size. The measured quantity, conditional assumptions and comparator are fixed.

## Attribution and development boundary

Sokolovski-Pons supply threshold-touching loss, the energy-domain method and the power-law comparator. Existing gapless adiabatic theorems and overcritical ionization results have different projection or protocol hypotheses. Fixed-frequency periodic 2D ionization is another distinct limit. PRIOR_ART.md records what was actually compared; unsuccessful searches are not novelty evidence.

The prospective advance is a controlled logarithmic slow-return law and its finite, positive-minimum domain. The known static singularity, generic adiabatic failure and elementary locality methods are not separate discoveries. No claim of all-two-dimensional universality, exact crossover, optimal size, technological superiority or completed apparatus is made.

**Development decision:** a dedicated, bounded theory project is justified. Submission readiness, complete assumption provenance, exhaustive priority and a separate critical-reader report are not established. Manuscript drafting and outside contact are not initiated by this note.
