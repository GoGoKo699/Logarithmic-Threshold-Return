# Does the coefficient require a perfectly symmetric square lattice?

**4 October 2026. New author-side scope calculation.** This is one falsification test of the recorded mechanism, not a new platform, schedule, or principal claim. The physical particle still evolves under a local hopping Hamiltonian with a single attractive site. The isotropic result and its rounding analysis remain unchanged in the parent archive.

## 1. The only variation: fixed positive hopping anisotropy

Choose an arbitrary fixed reference energy J0 and write time in hbar/J0. Let ax, ay be strictly positive dimensionless nearest-neighbor hoppings, fixed as the half-duration T increases. The dispersion is

```math
E(k_x,k_y)=2a_x(1-\cos k_x)+2a_y(1-\cos k_y).
```

The single-band spectrum is [0,4(ax+ay)]. Keep the same site potential U(t)=u+(g0-u)(t/T)^2, with fixed g0>0 and 0<=u<g0. The benchmark is ax=ay=1, g0=4. The initial and final tested vector is the bound state at g0 for the chosen lattice. Different anisotropies do not silently share the same binding energy or initial vector.

The question is whether equal hoppings or the coincident middle-band saddle is essential to the leading threshold return. Static elliptic-integral lattice resolvents are established tools; no priority is claimed for the resolvent evaluated below.

## 2. Exact local Green function and its constants

Put s=ax+ay and p=ax ay. Below the band, direct integration over one Bloch momentum gives

```math
\begin{aligned}
G(\eta)&=-g(-\eta)\\
&=\frac1\pi\int_0^\pi
\frac{dk}{\sqrt{[\eta+2s-2a_x\cos k]^2-4a_y^2}}\\
&=\frac{2}{\pi\sqrt{16p+\eta(4s+\eta)}}\,
\mathbf K\!\left(\frac{16p}{16p+\eta(4s+\eta)}\right).
\end{aligned}
```

Here K uses its parameter rather than modulus convention. One obtains the last line by the tangent-half-angle substitution and the standard complete elliptic integral. The code independently checks the preceding single-angle integral; it does not fit the constant in the logarithm.

For 0<omega<4 min(ax,ay), define z=omega(4s-omega)/(16p). Retarded continuation yields

```math
g(\omega)=-\frac{1}{2\pi\sqrt p}
\left[\mathbf K(1-z)+i\mathbf K(z)\right].
```

Consequently the lower-edge expansion is

```math
\begin{aligned}
g(\omega)&=-\rho\,[\ln\Lambda-\ln(-\omega-i0)]
+O(\omega\ln|\omega|),\\
\rho&=\frac1{4\pi\sqrt{a_xa_y}},\qquad
\Lambda=\frac{64a_xa_y}{a_x+a_y}.
\end{aligned}
```

In particular Im g(0+)=-pi rho. For eta>0, eta exp[G(eta)/rho] tends to Lambda. Derivative versions of the expansion follow from differentiating the elliptic expression. The constants in these estimates are permitted to depend on the fixed positive hoppings.

| ax | ay | rho | Lambda |
|---:|---:|---|---:|
| 1 | 1 | 1/(4 pi) | 32 |
| 1 | 1/2 | 1/(2 sqrt(2) pi) | 64/3 |
| 1 | 1/4 | 1/(2 pi) | 64/5 |

The continuum edge density and logarithmic energy scale change. The logarithmic singularity and its causal imaginary jump do not.

**Terminology correction:** the density of states tends to the finite nonzero constant rho at this lower edge. The logarithm is in the local Green function, obtained by integrating that density against the resolvent denominator. It is not the middle-band van Hove divergence. The phrase “logarithmic density-of-states threshold” in scout06 ASYMPTOTIC.md Section 8 was imprecise; its operative Green-function equations were already correct. That original record is preserved rather than silently rewritten.

## 3. Check every part of the matching, not just the local expansion

The existing method depends on more than finding a logarithm. For this fixed positive-hopping class its required properties can be verified as follows.

**Exact scalar reduction.** The potential still has rank one and exactly quadratic time dependence. For alpha=(g0-u)/T^2 the same Fourier equation is exact:

```math
c''+\frac{-1/g(\omega)-u}{\alpha}c=0.
```

The stationary-phase normalization on the incoming and outgoing bound legs is the same. Changing ax and ay does not change the algebra connecting energy-wave reflection with return. The transform is inherited from the Sokolovski-Pons approach, not a new device or a dissipative evolution.

**A bound state and a gapped endpoint.** G decreases continuously from infinity to zero on eta>0. Thus U G(eta)=1 has a unique solution for every U>0. For fixed g0, the endpoint gap is strictly positive. Since H0 is bounded, the deep-trap projector and reduced-resolvent estimates on the added tails have the same decaying powers as in scout06. Their constants depend on ax,ay,g0. The O(1/T) amplitude correction from the auxiliary infinite parabola therefore remains smaller than 1/ln T.

**Threshold approximation with derivatives.** The displayed elliptic formulas give the logarithmic expansion and its first two derivative controls on both sides of the edge. The first saddle lies at fixed energy 4 min(ax,ay)>0. For sufficiently large L, every polynomial-size central/matching interval scaled by e*=Lambda exp(-L) lies below it. The lattice corrections there are exponentially small compared with inverse powers of L.

**Physical positive-energy continuation.** The spectral representation gives Im g<=0 on the full band, with positive density inside it, including on either side of its saddles. For the scalar coefficient Im(-1/g)<=0. The retarded current inequality used in the previous outgoing-boundary argument therefore persists. A distant saddle may change the coefficient strongly, but its return contribution is attenuated before reaching the central region. There is no arbitrary absorber inserted into the Hamiltonian. The leading amplitude only needs the established current bound on the remote continuation, not an explicit closed form at every saddle.

**Negative-energy continuation.** Below zero, g<0 is smooth and has no zeros. At u=0 there is no negative-energy turning point. At 0<=u rho L<=1-delta the sole turning point lies within the small central interval, as in scout08. Away from the edge the resolvent and its derivatives are smooth; at minus infinity g~1/omega. These give the same integrable WKB-defect tails. No additional isolated band or remote eigenstate has been introduced.

These checks allow the existing matched-asymptotic proof to be applied to this explicit family. They are not a theorem for every Hamiltonian with the same first logarithm: arbitrary additional poles, simultaneous spectral deformations or loss channels would require separate hypotheses.

## 4. The resulting corollary and its boundary

Define

```math
\begin{aligned}
e_*^2&=\alpha\rho L,\qquad L=\ln(\Lambda/e_*),\\
L+\tfrac12\ln L&=\ln\frac{\Lambda T}{\sqrt{(g_0-u)\rho}},\qquad
\beta=u\rho L.
\end{aligned}
```

The scaled equation, including a positive minimum, is unchanged in form:

```math
y''+\left[\frac{L}{L-\ln(-x-i0)}-\beta\right]y=0
```

up to the controlled exponentially small lattice terms. With the proof properties verified above, the preceding reflection integral gives

```math
P_{\rm ret}(T,u(T))=
\frac{\pi^2}{4L^2[1-\beta(T)]^2}[1+o(1)],
\quad 0\le\beta(T)\le1-\delta.
```

In particular, for u=0 and any fixed ax,ay,g0>0,

```math
\boxed{P_{\rm ret}(T,0)\sim\frac{\pi^2}{4\ln^2 T}.}
```

This is a **corollary of the existing matching argument under newly checked fixed-anisotropy hypotheses**. It is not independent validation of that argument or a new universal reflection principle. Lambda and rho change the relation between L and the physical duration, and can change finite-duration answers. A table at equal L is not a table at equal physical time or equal preparation cost.

The result is explicitly **not uniform as ay/ax tends to zero**. At ay=0 the motion is one dimensional and the threshold singularity changes. One cannot obtain a dimensional-crossover law by setting ay=0 in these formulas. Nor does this pass change the quadratic schedule, replace the pointlike lattice attraction by a general continuum well, or claim robustness to arbitrary disorder or extra bands.

Finite-volume locality extends by replacing 4 sinh(mu) in the weighted evolution bound by 2(ax+ay)sinh(mu), and 4(cosh(mu)-1) by 2(ax+ay)(cosh(mu)-1). The old numerical coefficient 4.5 is retained only for the original isotropic choice. No optimized size law or new anisotropic device specification is claimed.

## 5. Numerical scope, independent formulations and actual errors

The new standalone suite compares the elliptic formula to an independent momentum integral at five hopping choices and three negative energies each. It tests both real logarithmic and retarded imaginary constants at three edge scales, and compares a finite 41-by-41 local coordinate evolution with the corresponding momentum evolution.

The scalar checks use the exact lower-edge resolvent on their finite auxiliary interval, with a local outgoing WKB boundary. At L=10,20,40 and four hopping choices, their probabilities approach the corresponding logarithmic-equation result. For L=20 and ay/ax=1/4, changing both boundaries and tightening integration changes the probability by about 8.04e-10; a separate vector second-order formulation differs from the Riccati result by about 2.24e-11. These are specific consistency checks, not rigorous error bars or full-band/time-domain simulations at exponentially long durations. The previous isotropic full-band tests are preserved, not newly rerun here.

The scalar data do not supply the corollary by numerical extrapolation. They check its implementation; the analytical hypotheses above are the reason the leading law transfers. The same-parent-code, same-proof provenance remains visible.
