# Logarithmic threshold return: energy-domain derivation

**4 October 2026. Author-side matched-asymptotic derivation, not independent review.** The fixed physical model is the infinite square lattice with one attractive site and the finite schedule of scout05. This note does not replace it by a two-level crossing, a finite box, a continuum delta potential, or a finite interval with no bound state. Statements about large duration concern this model, not all two-dimensional traps.

## 1. Result, units and scope

Measure energy in J and time in hbar/J. Write the dimensionless half duration as T. The Hamiltonian on the actual interval is

```math
H(t)=H_0-4(t/T)^2|0\rangle\langle0|,\qquad -T\le t\le T,
\quad H_0=4I-\sum_{\langle r,r'\rangle}(|r\rangle\langle r'|+\mathrm{h.c.}).
```

Start and end with the same bound-state projector at attraction 4. Let P_ret(T) be its unconditional return probability. Set rho_0=1/(4 pi), Lambda=32, alpha=4/T^2, and define positive L and energy e_* by

```math
e_*^2=\alpha\rho_0 L,\qquad L=\ln(\Lambda/e_*).
```

Equivalently,

```math
L+\tfrac12\ln L=\ln(32\sqrt\pi T).
```

The derivation below gives

```math
\boxed{P_{\rm ret}(T)=\frac{\pi^2}{4L^2}[1+o(1)]
\sim\frac{\pi^2}{4\ln^2T}\longrightarrow0.}
```

A conservative matching estimate developed below has amplitude remainder of order L^(-5/4), apart from exponentially small terms and the O(T^(-1)) finite-endpoint correction. It is not proposed as a sharp finite-time error bar. The coefficient pi^2/4 comes from an explicit reflection amplitude, not a fit to the earlier table. Subleading constants inside a fitted logarithm are not claimed.

With units restored, T here means TJ/hbar in the original physical notation; the complete cycle lasts 2T. Infinite volume is taken before the slow-cycle limit. Any fixed finite lattice or fixed positive residual attraction is a different asymptotic problem.

## 2. An auxiliary infinite parabola, with its endpoint cost retained

To use a Fourier transform, first extend the same curvature alpha to all real times: H_alpha(t)=H_0-alpha t^2 |0><0|. The incoming and outgoing bound states are defined by their deep-trap limits. Denote the bound-to-bound probability of this auxiliary cycle by P_infty(alpha). This is not exactly P_ret(T) at finite T.

The extra tails |t|>T have an isolated bound state separated from the band by at least the fixed initial gap. In scaled time s=t/T, the bound projector P(s) obeys P'(s)=O(|s|^(-3)) and P''(s)=O(|s|^(-4)) for |s| large. The reduced resolvent is O(|s|^(-2)); these estimates follow by expanding the rank-one bound eigenvector at attraction 4s^2 with bounded H_0. On any bounded tail segment away from s=0, the gap is positive. The usual adiabatic integration-by-parts construction therefore has integrable tail constants uniformly in the remote endpoint.

More explicitly, invert the off-diagonal commutator with H on P'(s) to form the adiabatic comparison operator. Its norm decays at least as |s|^(-5), its derivative is integrable, and the comparison generator times this operator is integrable. Integrating once in s gives an O(T^(-1)) operator error for transporting the bound projector on either added tail. Unitarity then gives, after irrelevant phases,

```math
\big||A_{\rm finite}|-|A_{\rm infinite}|\big|\le C/T.
```

This suffices because 1/T is smaller than any inverse power of L. The code separately lengthens the gapped tails at fixed alpha and compares the actual time evolution with the energy-domain answer. It does not silently assign the infinite-parabola answer to the finite protocol.

## 3. Exact rank-one energy equation

Let c(omega) be the time-Fourier transform of the amplitude at the attractive site, with inverse phase exp(-i omega t). Multiplication by t^2 becomes minus the second omega derivative. Imposing outgoing spatial radiation gives

```math
(\omega-H_0)\Psi(\omega)=\alpha|0\rangle c''(\omega),\qquad
c(\omega)=\alpha g(\omega)c''(\omega),
```

where

```math
g(\omega)=\langle0|(\omega-H_0+i0)^{-1}|0\rangle.
```

Thus a single scalar equation is exact:

```math
c''(\omega)+p(\omega)^2c(\omega)=0,\qquad
p^2=-\frac{1}{\alpha g(\omega)}.
```

The energy-domain reflection interpretation is the rank-one specialization of the established Sturmian approach [S1]. It is not a new transformation principle. The calculation is particularly simple here because the lattice perturbation has rank one; no truncation of a many-channel Sturmian expansion is needed.

At negative omega, g<0, p is real, and the two WKB phases correspond to the incoming and outgoing bound-state trajectories t=-p(omega) and t=+p(omega). Both have identical stationary-phase normalization factors. Indeed, p|p'|=-g'/(2 alpha g^2), while the normalized instantaneous bound state's site weight is g^2/(-g'). Their ratio is independent of the sign of t. The physical return probability is consequently the squared ratio of the reflected and incident energy-wave amplitudes.

For omega>8, g>0 and the physical solution decays as an Airy-type solution toward positive infinity. Inside the band, Im g<0, so Im p^2<0. This imaginary coefficient represents outgoing continuum probability in the auxiliary equation, not a bath or nonunitarity of the physical Schrödinger evolution.

## 4. The exact lattice Green function and the causal logarithm

For omega<0,

```math
g(\omega)=-\frac{2}{\pi(4-\omega)}
\mathbf K\left(\frac{16}{(4-\omega)^2}\right).
```

For 0<omega<8, put a=(omega-4)^2/16:

```math
g(\omega)=\frac{\operatorname{sgn}(\omega-4)}{2\pi}\mathbf K(a)
-\frac{i}{2\pi}\mathbf K(1-a).
```

The parameter convention for K is the one used in scout05. The real part is independently checked as a principal-value spectral integral and Im g=-pi rho(omega). Near the lower band edge,

```math
g(\omega)=-\rho_0\,[\ln\Lambda-\ln(-\omega-i0)]
+O\big(\omega\ln|\omega|\big).
```

On the upper side of the threshold, ln(-omega-i0)=ln omega-i pi. The sign of this imaginary term matters for the reflection coefficient. It cannot be dropped while retaining the real logarithm.

Rescale omega=e_* x. The energy equation near the threshold becomes

```math
y''+F_L(x)y=0,\qquad
F_L(x)=\frac{L}{L-\ln(-x-i0)},
```

up to exponentially small, smoothly controlled lattice corrections on polynomial-size intervals in x. In particular, e_*=32 exp(-L). The log equation is used locally and matched to the exact lattice; its artificial far-negative logarithmic pole at x=-exp(L) is never treated as a physical lattice singularity.

## 5. Why pointwise convergence is insufficient

For every fixed nonzero x, F_L(x) tends to 1. But at x=0, its limiting value for every finite L is zero. A pointwise substitution F=1 would miss the small reflected amplitude altogether. A naive WKB integral through x=0 is also not valid because the logarithmic derivatives are singular.

Use a central interval |x|<=R, with R=L^(1/4), and match to WKB solutions outside it. On the central interval write V(x)=ln(-x-i0). Then

```math
F_L=1+V/L+\mathcal R_L,\qquad
\int_{-R}^{R}|\mathcal R_L|dx
\le \frac{C[1+R(1+\ln R)^2]}{L^2},
```

and the integral of |F_L-1| is O(R(1+ln R)/L). These are L1 estimates, not a uniform pointwise Taylor expansion at zero. For |x|<1, the negative logarithm only increases the denominator; its first two powers are integrable. For 1<|x|<R, the denominator remains at least L/2 for sufficiently large L.

The integral equation relative to y''+y=0 therefore has a convergent small-norm first perturbation on this interval. Its second-order transfer error is bounded by O(R^2(1+ln R)^2/L^2). This controls the logarithmic central singularity without inventing a narrow forbidden band or discarding a finite core.

## 6. Outer matching and suppression of remote band structure

Let q=sqrt(F_L), with Re q positive and Im q nonpositive, h=q'/q, and

```math
\Omega=\tfrac14h^2-\tfrac12h'
=\frac{1}{4x^2D}-\frac{3}{16x^2D^2},
\qquad D=L-\ln(-x-i0).
```

The functions q^(-1/2)exp(plus/minus i integral q) have residual Omega times themselves. On R<=x<=L^2 and on the analogous negative interval up to |x|=exp(L/2), the integral of |Omega/q| is O(1/(LR)). Exact lattice corrections are exponentially smaller in these ranges.

Here is a useful explicit control of the outgoing boundary, rather than an assumption that the far continuum causes no return. For the physical solution put m=y'/y and define the local WKB reflection coordinate

```math
r(x)=\frac{m+h/2+iq}{iq-m-h/2}.
```

Direct differentiation gives

```math
r'=2iqr+\frac{i\Omega}{2q}(1+r)^2.
```

The current j=Im(y* y') satisfies j'=-Im(F)|y|^2>=0 on the positive spectral band, and j=0 at the decaying far-positive boundary. Thus j<=0, or Im m<=0 wherever m is defined. On R<=x<=L^2, q stays close to the positive real axis and h is small. The displayed Möbius transform then bounds |r| by a constant independent of L. Backward integration of its exact equation gives an attenuated boundary term plus an integral bounded by C integral |Omega/q|.

Moreover,

```math
-\int_R^{L^2}\operatorname{Im}q(x)dx\ge cL
```

for a fixed c>0 and sufficiently large L. The reflection information entering from the remainder of the physical band is suppressed by exp(-cL), irrespective of the van Hove singularity farther away. This step uses passivity of the retarded boundary, not an artificial perfectly absorbing detector.

On the negative side q and h are real and the same current argument gives |r|<=1. Transport to the deep-bound asymptotic region changes its magnitude by at most a constant times integral |Omega/q|. Between |x|=exp(L/2) and a fixed negative physical energy the exact logarithmic-resolvent derivative estimates make this integral exponentially small. Away from the edge, the exact resolvent is smooth and behaves as 1/omega at negative infinity; its WKB-defect integral is finite and multiplied by sqrt(alpha). There is no negative-energy turning point outside the central interval.

Together, the two outer regions change the central reflection amplitude, apart from a phase, by O(1/(LR))+O(exp(-cL)). This is the matching step that should receive focused scrutiny in a separate mathematical reading. The code checks the local estimates and endpoint stability, not an all-L bound by numerical sampling.

## 7. The reflection coefficient, without fitting a logarithm

Expand the central transfer to first order and express the endpoint data in the local WKB bases rather than abruptly matching to free waves. Integration by parts cancels the endpoint terms proportional to V(plus/minus R). The phase-adjusted reflected amplitude is

```math
r_L=-\frac{1}{4L}\int_{-R}^{R}V'(x)e^{-2ix}dx
+O\left(\frac1{LR}+\frac{R^2(1+\ln R)^2}{L^2}\right)
+O(e^{-cL}).
```

The distributional derivative is

```math
V'(x)=\operatorname{PV}\frac1x-i\pi\delta(x).
```

Both terms contribute. The symmetric finite-window principal value is -2i Si(2R), while the delta contributes -i pi. Hence

```math
r_L=\frac{i}{4L}[2\operatorname{Si}(2R)+\pi]+o(L^{-1})
=\frac{i\pi}{2L}+o(L^{-1}),
```

up to an overall propagation phase of unit modulus. The central remainder with R=L^(1/4) is o(1/L), and the outer term is O(L^(-5/4)). Squaring and using the gapped-tail comparison establishes the result in Section 1.

This calculation explains why keeping only the real logarithm would give the wrong prefactor. It also explains why substituting an algebraic bound-energy closing exponent from a one-dimensional trap is not a derivation of the two-dimensional law.

## 8. Interpretation and limits

A slowly weakened two-dimensional trap does not approach a nonzero 38-percent recapture plateau in this model. Its return vanishes, but only as an inverse square logarithm of the cycle scale. The logarithmic density-of-states threshold makes the auxiliary reflection weak, rather than leaving a scale-independent reflection coefficient as in the one-dimensional zero-range comparator.

The main physical Hamiltonian stays unitary. Escaped probability occupies the continuum. A fixed finite box and a positive minimum trap depth both retain a normalizable isolated state and belong to different limits. The exact zero minimum, fixed quadratic approach, single-site trap, initial bound state and thermodynamic order of limits remain explicit assumptions.

The result is an author-side asymptotic derivation with a spelled-out matching argument, not a computer-certified bound, independent peer review, exhaustive priority claim or experimental proposal. Its finite-L leading approximation is quantitatively slow to converge. The next audit should challenge the retarded energy-to-time identification, the outer current-based matching and the endpoint estimate before expanding to any other protocol. The detailed scope of existing threshold and two-dimensional ionization results is in SOURCES.md.
