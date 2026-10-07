# Sokolovski–Pons–Muga 2014: construction-level comparison

Source: D. Sokolovski, M. Pons and J. G. Muga, *Adiabaticity near a continuum
threshold: An exactly solvable model*, Phys. Rev. A **89**, 042125 (2014),
[DOI](https://doi.org/10.1103/PhysRevA.89.042125). The supplied seven-page
published PDF was read in full (Sections I–VIII and Appendix); the decisive
equations on printed pp. 042125-2 through 042125-6 were visually checked.
The file identity and reading scope are recorded in
[provenance](../provenance/SOURCE_COMPARISON_2014_2026-10-05.json).

## Method and physical comparison

The paper is a direct predecessor for the outgoing energy/Sturmian method, normalized bound-state
population, and the contrast between finite confinement and a continuum threshold.
It does not directly establish the present two-leg logarithmic return law or its
shrinking-minimum/growing-volume uniformity.

## Source model and asymptotic assumptions

| Item | Primary passage | Exact scope |
|---|---|---|
| Protocol and endpoints | Section III, p. 2, Eq. (9); p. 3, Eq. (11) | $`H(t)=-\partial_x^2/2+vt\delta(x)`$ with $`v>0`$. Initial preparation follows the deep bound state as $`t\to-\infty`$. Evolution stops at $`t_f<0`$, with $`\Omega_f=vt_f<0`$. There is no reopening leg. |
| Binding law and normalization | Section III, p. 2, text after Eq. (9) and Eq. (10) | $`E_0(t)=-(vt)^2/2=-\Omega(t)^2/2`$ and $`\phi_0(x,\Omega)=\sqrt{\lvert\Omega\rvert}e^{-\lvert\Omega\rvert\lvert x\rvert}`$ on the full line. The spatial norm is one. |
| Measured state | Section VI, p. 4, Eqs. (26)–(28) | $`A_{\rm stay}=\langle\phi_0(\Omega_f),\Psi(t_f)\rangle`$; $`P_{\rm stay}=\lvert A_{\rm stay}\rvert^2`$. This is normalized final-bound-state population, not position occupation or return to a restored initial well. |
| Exact reduction | Sections IV–V, pp. 3–4, Eqs. (13)–(25) | Outgoing Sturmians obey $`\rho(\omega)=i\sqrt{2\omega}`$ on the stated branch. The coefficient solves the first-order equation $`ivB'+\rho B=0`$. One energy integral gives the exact wave function; remote-time stationary phase fixes its normalization. |
| Slow limit | Section VI, p. 4, Eq. (29) | The displayed limit is $`v\to0`$ at each fixed $`E_f<0`$. It gives adiabatic amplitude, including phase, not a joint threshold limit uniform in $`E_f(v)`$. |
| Accuracy criterion | Section VI, pp. 4–5, Eqs. (30)–(32); Section VIII, p. 6, Eq. (42) | Stationary-phase width must be separated from the nearest energy singularity. The paper distinguishes complex-amplitude accuracy from modulus accuracy; a stricter amplitude criterion is not an exact necessary condition for probability near one. |
| Finite box | Section VII, pp. 5–6, Eqs. (35)–(41) | Walls lie at $`x=\pm a`$; the stopped level remains negative. The Sturmian function has poles, with $`\rho=-k\cot(ka)`$ and $`k=\sqrt{2\omega}`$. Their broad-box limit recovers the continuum cut. |

For the continuum approach, the positive dimensionless ratio is

```math
\gamma=\frac{\dot E_f}{E_f^2}
=\frac{4v}{|\Omega_f|^3},\qquad
E_f=-\frac{\Omega_f^2}{2},\quad \dot E_f=-v\Omega_f>0.
```

The absolute-value form follows directly from the source's negative-$`\Omega_f`$
convention. The final specialization printed in Eq. (31) lacks that sign
correction; the invariant ratio and the paper's positive-$`\gamma`$ figures are the
unambiguous quantities used here. This source-level sign issue does not affect
the present lattice argument.

Equation (32) gives a small-loss quadratic approximation. After that equation,
the authors explicitly defer a uniform approximation when the stationary point
coalesces with the threshold branch point. Section VIII's final paragraph extends
the intuition to nonlinear protocols only when they are already sufficiently slow
for perturbative Eq. (6) to hold. Neither passage supplies a low-return asymptotic
for an arbitrary nonlinear cycle.

For the box, the nearest Sturmian pole is
$`\omega_1=\pi^2/(2a^2)`$, and Eq. (40) uses
$`\dot E_f/(\omega_1-E_f)^2`$. **The pole is not the next instantaneous eigenvalue
$`E_1(t_f)`$**: Eq. (41) explicitly retains the factor
$`[(\omega_1-E_f)/(E_1(t_f)-E_f)]^4`$. The pole-to-cut discussion in Eq. (39)
is not a quantitative error estimate for a joint size-and-duration family.

## Comparison with the fixed lattice return

The present [claim](../research/PROOF_STATUS.md) uses a two-dimensional lattice,
$`U(t)=u+(4-u)(t/T)^2`$, and the same normalized bound state at both endpoints
$`t=\pm T`$. Its observable is unconditional bound-to-bound return after the whole
cycle. At zero minimum,

```math
\eta(U)\sim32e^{-4\pi/U},\qquad
\eta(s)\sim32e^{-\pi/s^2},\quad s=t/T.
```

These are essential-binding scales, not the source's quadratic binding law.
Changing the static binding function in a heuristic criterion does not also
change its one-way protocol, first-order energy equation and endpoint observable
into the present second-order reflection problem.

Nor can Eq. (31) be used at a turning point by observing that an instantaneous
derivative vanishes: its stationary-phase and small-loss hypotheses must first
hold. The return regime under study has probability tending to zero.
The fixed-$`E_f`$ limit, the weak-loss expansion and the broad-box discussion do not
supply uniformity for the present $`u(T)\to0`$ and increasing torus.

The finite-box analysis is nevertheless a substantive predecessor. Ordinary
finite-size recovery, squared-speed leakage near adiabaticity, outgoing
energy-domain reduction and stationary-phase normalization are inherited
ingredients. [LIMITS_AND_ACCURACY](../research/LIMITS_AND_ACCURACY.md) applies
standard gapped reasoning to our fixed torus; it is not a new recovery mechanism.
The comparison concerns the controlled logarithmic physical return and its stated
joint domain, with the existing local-power prediction included.
