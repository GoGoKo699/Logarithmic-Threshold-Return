# Finite depth and finite volume: a controlled window for logarithmic return

**4 October 2026. New author-side derivation following scout07.** This note extends the stated local square-lattice protocol only by its two previously identified physical rounding parameters. It does not claim a universal trap class, a complete crossover function, a sharp minimum system size, or an experimentally implemented device. The preceding matched-asymptotic result and its audit are preserved unchanged in the evidence archive.

## 1. Same endpoints, a positive minimum

Use units $J=\hbar=1$ until the final interpretation. The square-lattice operator has spectrum $[0,8]$,

```math
H_0=4I-\sum_{\langle x,y\rangle}(|x\rangle\langle y|+\mathrm{h.c.}).
```

On $[-T,T]$ choose

```math
H(t)=H_0-U(t)|0\rangle\langle0|,\qquad
U(t)=u+(4-u)(t/T)^2,\qquad 0\le u<4.
```

The endpoint attraction remains exactly 4 and the endpoint bound state is the same state used previously. $u=U_{\min}/J$ is the residual attraction, not a binding energy or an added particle-loss rate. Every member with $u>0$ has a bound state at every instant. $T$ is the half-cycle time, equal to $T_{\rm physical}J/\hbar$ after restoring units.

Let $P_\infty(T,u)$ denote the infinite-lattice return probability. Let $P_n(T,u)$ denote return to the endpoint ground state on a periodic $n\times n$ square. The finite and infinite endpoint bound states are close but are not declared identical.

## 2. The scaled residual parameter follows from the exact energy equation

As in the preceding derivation, first extend the same parabola to all times and set $\alpha=(4-u)/T^2$. Let $g(\omega)=\langle0|(\omega-H_0+i0)^{-1}|0\rangle$. Fourier transformation of the contact amplitude gives

```math
c=g(\alpha c''-uc),\qquad
c''+\frac{-1/g-u}{\alpha}\,c=0.
```

The transform and its bound-return/reflection interpretation are inherited from the energy-domain approach of Sokolovski–Pons [S1]. This is its rank-one specialization with a nonzero minimum. The site-weight normalization on the two bound legs is still identical: differentiating $p^2=(-1/g-u)/\alpha$ removes the constant $u$ and leaves the preceding stationary-phase identity. The gapped extra tails still start at attraction 4; uniformly for small $u$, their comparison with the finite interval costs $O(1/T)$ in amplitude.

At the lower edge,

```math
g(\omega)=-\rho_0\{\ln32-\ln(-\omega-i0)\}
+O(\omega\ln|\omega|),\qquad \rho_0=\frac1{4\pi}.
```

Define $L,e_*$ by

```math
e_*^2=\alpha\rho_0L,\qquad L=\ln(32/e_*),
```

or, equivalently,

```math
L+\frac12\ln L=\ln\frac{32T}{\sqrt{(4-u)\rho_0}}.
```

At $\omega=e_*x$, the local equation is

```math
y''+\left[\frac{L}{L-\ln(-x-i0)}-b\right]y=0,
\qquad \boxed{b=\rho_0uL=\frac{uL}{4\pi}.}
```

Thus the effect of a minimum attraction is set by its product with the large logarithm, not by $u$ alone. The square-lattice corrections are exponentially small on the same polynomial-size matching intervals used in the zero-minimum proof.

## 3. Joint limit below the rounding boundary

**Claim with explicit domain:** suppose $T\to\infty$ and $0\le b(T)\le1-\delta$ for a fixed $\delta>0$. Then the extension of the preceding matching argument gives

```math
\boxed{
P_\infty(T,u(T))
=\frac{\pi^2}{4L^2[1-b(T)]^2}\,[1+o(1)].
}
```

In particular, if $b(T)\to b_0<1$, the asymptotic coefficient relative to $1/L^2$ is $\pi^2/[4(1-b_0)^2]$. This is not a formula for fixed $u>0$ all the way to arbitrarily large $T$, and it cannot be extrapolated to $b=1$. It is a new author-side consequence on the stated joint family, not an independently reviewed theorem.

### Central estimate

Write $V=\ln(-x-i0)$ and $q_0^2=1-b$. On $|x|\le R=L^{1/4}$,

```math
\frac{L}{L-V}-b=q_0^2+\frac{V}{L}+\mathcal R_L,
\qquad
\|\mathcal R_L\|_{L^1(-R,R)}
\le \frac{C[1+R(1+\ln R)^2]}{L^2}.
```

The free comparison has wave number $q_0\ge\sqrt\delta$. The transfer-equation error is uniformly $O_\delta(R^2(1+\ln R)^2/L^2)$. The fact that the exact coefficient tends to $-b$ at $x=0$ does not invalidate this integrated estimate: it is not a pointwise uniform Taylor expansion. For $b>0$, the small negative-energy forbidden region is included in that estimate, not cut out. Its turning point is exponentially close to zero when $b<1$.

### Outer estimate and a necessary change from the old proof

Set $q^2=L/(L-V)-b$, choosing $\operatorname{Re}q>0$ and $\operatorname{Im}q\le0$, and $h=q'/q$. On the matching regions outside $R$, $q$ stays bounded away from zero and

```math
|h|=O_\delta((L|x|)^{-1}),\qquad
\int |\Omega/q|\,dx=O_\delta((LR)^{-1}),\qquad
\Omega=h^2/4-h'/2.
```

The earlier zero-minimum proof used a favorable sign of $\operatorname{Im}h$. That sign should **not** simply be assumed after subtracting $b$. Instead use the passive half-plane $\operatorname{Im}m\le0$ for $m=y'/y$ and

```math
|iq-m-h/2|\ge\operatorname{Re}q-|h|/2
\ge\tfrac12\operatorname{Re}q
```

for sufficiently large $L$. This bounds the reflection coordinate

```math
r=\frac{m+h/2+iq}{iq-m-h/2}
```

by a constant depending only on $\delta$. Its exact Riccati equation remains

```math
r'=2iqr+\frac{i\Omega}{2q}(1+r)^2.
```

Positive-side attenuation out to $x=L^2$ is at least $c_\delta L$. Remote physical-band data are therefore exponentially suppressed, while the integrated defect produces $O_\delta(1/(LR))$. On the negative side there is no additional turning point outside the central region; the exact resolvent and the fixed negative-energy/deep-bound tails complete the matching as in scout06. The constants are uniform for $b\le1-\delta$, not across $b=1$.

### Leading coefficient

Matching the central transfer in local wave bases cancels its endpoint terms. Up to an irrelevant phase,

```math
r=-\frac1{4Lq_0^2}\int_{-R}^R
\left[\operatorname{PV}\frac1x-i\pi\delta(x)\right]
 e^{-2iq_0x}\,dx+o_\delta(L^{-1}).
```

For positive $q_0$ the integral tends to $-2i\pi$, uniformly when $q_0$ is bounded away from zero. Thus

```math
r=\frac{i\pi}{2L(1-b)}+o_\delta(L^{-1}).
```

The remainder may be bounded by the preceding $O_\delta(L^{-5/4})$ outer error plus the smaller central and finite-tail errors. Squaring gives the claimed joint law. A formal pole at $b=1$ would make a probability diverge; it signals loss of validity of this expansion, not a physical divergence.

## 4. Consequences for control accuracy

If $u(T)=o(1/\ln T)$, then $b\to0$ and the zero-minimum coefficient is recovered. If $u(T)\sim4\pi b_0/\ln T$ with fixed $0<b_0<1$, the attraction remains **strictly positive throughout every cycle**, yet return still vanishes with the modified coefficient.

The static gap in that joint family becomes very small:

```math
\eta(u)\sim32e^{-4\pi/u},\qquad
\eta(u)/e_*\sim e^{-L(1/b-1)}\longrightarrow0
\quad(0<b<1\text{ fixed}).
```

There is no contradiction of gapped adiabatic theory. Each member has a gap, but the gap is not held fixed as the duration increases. No gap-independent error constant is assumed. Conversely, every fixed $u>0$ defines a fixed gapped family and ultimately has return approaching one [S2].

An inverse-logarithmic depth scale is not an experimental precision certificate. Timing, environmental coherence, the actual mapping of a control voltage or light shift into $u$, and other confining potentials have not been supplied. The calculation only quantifies this particular Hamiltonian imperfection.

## 5. Fixed positive minimum: an action scale, not a solved crossover

For a fixed residual attraction, the minimum binding $\eta(u)$ solves $uG(\eta)=1$, where

```math
G(\epsilon)=-g(-\epsilon)
=\frac{2}{\pi(4+\epsilon)}\mathbf K\!\left(\frac{16}{(4+\epsilon)^2}\right).
```

The exact auxiliary forbidden interval is $-\eta<\omega<0$. Its action is

```math
\mathcal A(T,u)=\frac{T}{\sqrt{4-u}}
 \int_0^{\eta(u)}\sqrt{u-\frac1{G(\epsilon)}}\,d\epsilon.
```

The existence of an energy-domain barrier and restoration of adiabatic reflection for a level turning below threshold are already explained in Sokolovski–Pons [S1, Section IV]. They are not discovered here. For the logarithmic edge, put $\epsilon=\eta e^{-v}$ and $a=4\pi/u$. Since $G(\eta e^{-v})\sim\rho_0(a+v)$,

```math
\mathcal A(T,u)\sim
\frac{T\eta(u)}{\sqrt{4-u}}
\sqrt{\frac{u}{a}}\int_0^\infty e^{-v}\sqrt v\,dv
=\frac{T u\eta(u)}{4\sqrt{4-u}}
\qquad (u\downarrow0).
```

The inverse-action duration is exponentially large in $1/u$. This explains why a fixed small residual attraction can have a wide intermediate low-return regime before its ultimate adiabatic recovery. We have not derived the full return function around $b=1$, a uniform barrier prefactor, or a rigorous rule that $\mathcal A=1$ fixes a chosen percentage. No exact probability is set equal to $e^{-2\mathcal A}$.

## 6. A sufficient finite-volume family

The following estimate is deliberately conservative. It establishes an explicit finite family exhibiting the same asymptotic, not a necessary lattice size or an optimized experimental design.

Let $n=2R+1$ be odd and embed its periodic square into the corresponding centered square in the infinite lattice. Denote this embedding by $E_n$. Let $d(x)=|x_1|+|x_2|$ on the infinite lattice and the corresponding torus graph distance on the finite lattice. For $W=e^{\mu d}$, nearest-neighbor hopping obeys

```math
\left\|\frac{WH_0W^{-1}-(WH_0W^{-1})^\dagger}{2i}\right\|
\le4\sinh\mu,
```

and

```math
\operatorname{Re}(WH_0W^{-1})\ge-4(\cosh\mu-1)I.
```

Both follow from a row-sum bound on the four neighboring edges, where adjacent distance values differ by at most one. The local time-dependent attraction commutes with $W$ and has no anti-Hermitian contribution. Hence the weighted propagated norm grows at most as $e^{4\sinh\mu\,t}$, independently of the residual depth.

### Initial localized states are uniformly controlled

At attraction 4, the infinite bound energy is $-\eta_0$ with $\eta_0\simeq1.04587817$. The periodic heat kernel is a sum of the nonnegative infinite-lattice image kernels. Its origin resolvent is at least the infinite one, so the finite binding $\eta_n\ge\eta_0$; also $\eta_n\le4$.

Choose $\mu>0$ with $4(\cosh\mu-1)<\eta_0$. The weighted resolvent equation and its real-part bound give a uniform bound on $\|Wb_n\|$ and $\|Wb_\infty\|$. The unnormalized bound is $(H_0+\eta)^{-1}|0\rangle$ and its norm is at least $1/(8+\eta)\ge1/12$, so normalization does not destroy this bound.

Embedding the finite bound vector produces only an exponentially small seam residual for the infinite endpoint Hamiltonian. On the orthogonal complement of its bound state, the shifted endpoint Hamiltonian is bounded below by $\eta_n\ge\eta_0$. The residual therefore bounds that component by $C_\mu e^{-\mu R}$. The positive real choices of the two bound vectors fix their relative phase, giving

```math
\|E_n b_n-b_\infty\|\le C_\mu e^{-\mu R}.
```

### Finite evolution and return

The finite/infinite Hamiltonian difference acts only at the periodic seam. Duhamel's formula, the initial estimate and the weighted norm bound give at the midpoint

```math
\|E_n\psi_n(0)-\psi_\infty(0)\|
\le C_\mu(1+T)e^{4\sinh\mu\,T-\mu R}.
```

This is a full state-norm estimate. It does not replace the finite lattice by an energy grid, invoke a hard propagation speed, or assume an exactly compact initial state.

Because the Hamiltonian is real and the control is even in time, the return amplitude is $A=\psi(0)^T\psi(0)$ for an initially real normalized bound state. Consequently

```math
|A_n-A_\infty|
\le2C_\mu(1+T)e^{4\sinh\mu\,T-\mu R}.
```

To retain a leading amplitude of order $1/L$, it is sufficient that the right side be $o(1/L)$. For example, $\mu=1/2$ is admissible, and

```math
\boxed{n(T)=2\lceil4.5T\rceil+1}
```

gives

```math
4\sinh(1/2)T-\tfrac12R
\le-(2.25-4\sinh(1/2))T
\simeq-0.16561878T.
```

It follows that the joint residual law of Section 3 also holds on this sequence of **finite periodic lattices**, with $n^2=O(T^2)$ sites. Every member with $u(T)>0$ is gapped. The time, minimum depth and volume change together; the ordinary fixed-volume or fixed-depth adiabatic limit is not being contradicted.

The coefficient 9 in the side-length choice is a sufficient bound from exponential weights, not an optimized propagation velocity or a required number of sites. The finite examples in RESULT.md converge at considerably smaller sizes. They do not prove a sharper universal size scaling or a monotonic dependence on size.

## 7. Evidence, attribution and remaining gap

The exact finite torus is represented by its discrete momentum measure, combined by the reflection and exchange symmetries that leave the site state invariant. This is a lossless finite-dimensional reduction, not a continuum quadrature. Separate coordinate-space propagation tests it. Infinite-lattice results use the exact square-lattice spectral density with independent quadrature refinement; slow oscillatory integrals require their own resolution, even if norm is conserved.

New analytical contributions in this note are the $b$-dependent extension of the preceding logarithmic matching and the explicit finite-size sufficient-family estimate. The Fourier/Sturmian interpretation, gapped recovery, forbidden-region reasoning and exponential-weight method are established tools [S1,S2]. We do not claim exhaustive priority for the particular combination. The full apparatus precedent audit and a separate critical-reader report remain absent.

The result now has a finite, nonzero-minimum domain rather than depending only on an exact singular endpoint. What remains unresolved is the sharp finite-size crossover, the full $b\approx1$ crossover, and a realistic preparation/coherence/resource specification. These are not silently filled in by a large simulated lattice or a fitted logarithm. No further change of trap, dimensionality, particle number or control shape has been introduced.
