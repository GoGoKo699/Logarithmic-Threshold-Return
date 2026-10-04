# Threshold-return audit: outgoing matching, normalization and the gapless comparator

**4 October 2026. Author-side derivation and checks, not an independent report.** This audits the law recorded in scout06 for the same local square-lattice trap and time-quadratic round trip. The preceding archive is preserved without edits. No new trap, driving exponent, many-body system, detector, repository or contact is introduced.

## 1. Outcome and fixed claim

I found no error in the audited steps that changes the leading law

```math
P_{\mathrm{ret}}(T)=\frac{\pi^2}{4L^2}[1+o(1)],\qquad
L+\tfrac12\ln L=\ln(32\sqrt\pi\,T).
```

Here energies are in J, time in hbar/J, and T is the half duration of the original interval [-T,T]. The initial and final attraction is 4. Infinite lattice volume is taken first. The result remains an author-side matched-asymptotic result, not an independently verified theorem or a general statement about every two-dimensional trap.

The useful strengthening is an explicit finite outgoing-matching inequality uniform over passive continuations, rather than reliance on one absorbing numerical boundary. A full-band calculation checks the exact resolvent beyond its upper edge. A direct test of a gapless adiabatic theorem's hypothesis identifies why it does not restore slow return. The exact power-law comparison credits the older Bessel/Sturmian structure instead of treating a familiar coefficient as a new method.

## 2. Exact energy reduction and the physical state being counted

For the auxiliary infinite parabola, let alpha=4/T^2 and use inverse Fourier phase exp(-i omega t). Multiplication by t squared is minus the second energy derivative. The transform is understood as an oscillatory/tempered distribution, not as an L2 Fourier transform of a decaying contact amplitude: the particle remains deeply bound in the remote past and future. The absence of an incoming continuum component selects the retarded spatial resolvent.

```math
(\omega-H_0)\Psi(\omega)=\alpha|0\rangle c''(\omega),\quad
c=\alpha g c'',\quad
c''+p^2c=0,\quad p^2=-\frac1{\alpha g}.
```

The outgoing continuum condition is essential. An arbitrarily imposed coherent incident continuum is a different physical initial state; no robustness claim against it is made. This transformation and its reflected-wave interpretation are inherited from the Sturmian approach [S1], here exact in one channel because the lattice perturbation is rank one.

At omega<0, g and p are real with g<0, g'<0 and p'<0. The bound-state pole condition is 1+U g=0. The normalized instantaneous bound state's site weight is

```math
|\langle0|b\rangle|^2=\frac{g^2}{-g'},\qquad
p|p'|=\frac{-g'}{2\alpha g^2}.
```

Stationary phase applied to the two energy waves p^(-1/2) exp(plus/minus i integral p), followed by exp(-i omega t), picks t=plus/minus p. Its normalization relative to the physical bound state is identical on the two legs. The factor involving [p|p'|]^{-1} divided by the site weight equals 2 alpha; the overall Fourier convention multiplies both legs equally. Therefore the physical bound-to-bound probability is the squared reflected/incoming energy-amplitude ratio. There is no extra logarithmic normalization factor missing from the probability.

The static identities are checked with high-precision derivatives of the exact Green function. This is a normalization check, not a complete independent construction of scattering wave operators.

## 3. A finite inequality for arbitrary passive positive-energy continuation

In the logarithmic region let

```math
F=\frac{L}{D},\quad D=L-\ln x+i\pi,\quad
q=\sqrt F,\quad h=q'/q=\frac1{2xD},\quad x>0.
```

Take R=L^(1/4), B=L^2 and L>=10. Then Re D>0, Re q>0, Im q<0 and Im h<0 throughout [R,B]. The exact lattice coefficient differs exponentially little on this scaled interval as L grows; constants can be enlarged to accommodate that difference. The explicit formulas in this section are for the local logarithmic coefficient, not an equality replacing the entire physical band.

For a nonzero solution write m=y'/y and

```math
r=\frac{m+h/2+iq}{iq-m-h/2},\qquad
\Omega=\frac{h^2}{4}-\frac{h'}2
=\frac1{4x^2D}-\frac3{16x^2D^2}.
```

Differentiation using m'=-F-m^2 yields, exactly,

```math
r'=2iqr+\frac{i\Omega}{2q}(1+r)^2.
```

Both rational identities are checked symbolically, not inferred from numerical curves.

### Why the physical boundary gives the required half-plane

The energy-coordinate current j=Im(y* y') satisfies j'=-Im(F)|y|^2>=0. The decaying physical solution beyond the entire band has zero current there. Consequently j<=0 at an earlier positive energy, and Im m<=0. More generally, every passive continuation imposes Im m(B)<=0, which propagates to the left.

Let z=m+h/2 and q=a+ib. Since Im z<=Im h/2<0,

```math
|iq-z|\ge a-\operatorname{Im}h/2\ge a,\qquad
|r|=\left|-1+\frac{2iq}{iq-z}\right|
\le 1+\frac{2|q|}{a}<4.
```

Here |arg q|<pi/4 ensures |q|/a<sqrt(2). The denominator cannot vanish for a passive m. At a zero of y, the logarithmic derivative chart may diverge, but r has the finite continuation -1; no solution is excluded by using that chart.

### Backwards propagation suppresses terminal information

Define

```math
\mathcal A=\int_R^B[-\operatorname{Im}q(x)]\,dx,\qquad
\mathcal I=\int_R^B\left|\frac{\Omega(x)}{q(x)}\right|dx.
```

Integrating the exact r equation backwards and using |r|<4 gives the finite bound

```math
\boxed{|r(R)|\le4e^{-2\mathcal A}+\frac{25}{2}\mathcal I.}
```

No particular terminal admittance, incoming phase, or guessed numerical absorber is selected in this bound. The earlier estimates A>=cL and I=O(1/(LR)) therefore control the physical outgoing matching with a terminally uniform error O(1/(LR))+O(exp(-cL)). The constants are conservative; this is not a tight finite-time accuracy certificate.

This is why high-energy details, including the square lattice's middle-band singularity, cannot return an order-1/L amplitude to alter the leading coefficient in the fixed problem. It is not a proof that arbitrary changes of the low-energy spectral density, an added bound mode, or a finite box leave the law unchanged. A finite box does not have the same continuous retarded boundary.

### What the numerical stress tests add

At L=10,20,50, integrate from B=8L with six terminal logarithmic derivatives: local outgoing WKB, 0, plus/minus 10, -i and -100i. Every load is passive; real loads have zero current at the endpoint. Use a common negative-energy extraction point. Their return-probability spreads are below 6e-12 in the recorded execution. A separate second-order vector integration checks the logarithmic-derivative solver.

The tests at B=L^2 also directly check the displayed finite bound at R. Those samples do not prove a claim about all boundary loads; the half-plane argument does. Terminal variations are mathematical tests, not six fabricated physical traps or a proposal to send radiation back at the particle.

## 4. Full physical band, not just a local absorbing cutoff

The earlier local-boundary calculation is now compared with integration of the exact square-lattice Green function from positive energy 12 or 16, beyond the band [0,8]. The calculation crosses both band edges and the van Hove point at 4, treating the reciprocal-resolvent limits correctly. An asymptotically decaying Airy logarithmic derivative supplies the physical far-energy condition. Zero-derivative and dissipative terminal conditions provide separate sensitivity tests, not alternate physical boundary assertions.

At T=30 the result is about 0.0347104052; at T=100 it is about 0.0271230810. Moving the positive endpoint and tightening integration changes these values by less than 3e-10 in the recorded comparisons. They agree with scout06's auxiliary infinite-parabola calculation. They are **not** relabeled as the original finite-cycle probabilities: scout06 separately computed approximately 0.0358074369 and 0.0269965798 for those cycles.

The full physical wavefunction evolves unitarily. The complex energy coefficient is a representation of continuum escape, not a bath added to obtain small survival. This check directly targets an important source of a possible spurious return law.

## 5. Central singularity and finite physical endpoints

The central proof is not changed. On [-R,R], V=ln(-x-i0) has an integrable logarithmic singularity. Its L1 remainder after the first expansion is bounded, even though the expansion is not pointwise uniform at x=0. The transfer-equation second-order remainder is O(R^2(1+ln R)^2/L^2). Matching to local WKB bases cancels the endpoint terms and leaves

```math
r_L=-\frac1{4L}\int_{-R}^{R}
\left[\operatorname{PV}\frac1x-i\pi\delta(x)\right]e^{-2ix}dx
+o(L^{-1})=\frac{i\pi}{2L}+o(L^{-1}).
```

The two terms give equal leading contributions. Omitting the causal jump is not an allowed real-potential approximation. With R=L^(1/4), the new explicit outer estimate is subleading to this amplitude. No new fit or replacement of the zero-energy core is used.

For the auxiliary-to-finite-cycle comparison, the tails |t|>T stay gapped. In s=t/T, P'=O(s^-3) and the reduced resolvent R_b=O(s^-2). One may use the off-diagonal commutator solution

```math
X=R_b P'P+P P'R_b,\qquad [H,X]=[P',P].
```

Its derivative and the products with the comparison generator are integrable on the tails. Integration by parts gives the preceding O(1/T) tail error, independent of how far the auxiliary endpoints are taken. This is an application of the standard commutator method [S3], not a new adiabatic theorem. Since 1/T is smaller than 1/L, the finite-endpoint passage is consistent with the leading law. A complete separate mathematical reader should still examine this construction rather than treating the finite tests as its proof.

## 6. Why a gapless adiabatic theorem does not rescue this state

Avron–Elgart's theorem [S3] does not require a spectral gap, but it requires an appropriate smoothly varying finite-rank spectral projection. The present bound projection has no norm-continuous extension to the instant of touching.

There is a direct test. Let b_eta be the normalized bound vector at energy -eta. In the local spectral representation it is proportional to (E+eta)^(-1). For a fixed positive ratio c not equal to one, the constant lower-edge density gives

```math
\lim_{\eta\downarrow0}\langle b_\eta|b_{c\eta}\rangle
=\frac{\sqrt c\ln c}{c-1}<1.
```

Indeed, the cross integral is asymptotic to rho_0 ln(c)/[(c-1)eta], and each squared norm is asymptotic to rho_0/eta or rho_0/(c eta). The norm distance of the two rank-one projections therefore has a strictly positive limit. For c=4,

```math
\lim\|P_\eta-P_{4\eta}\|
=\sqrt{1-(2\ln4/3)^2}\approx0.3819179344.
```

Both binding energies go to zero, but the projections are not even norm-Cauchy. Exact square-lattice Green-function calculations confirm this limit. This disproves the required premise in our problem; it is not a contradiction of gapless adiabatic theory. The state expands away rather than becoming a normalizable critical ground vector.

## 7. The coefficient has a familiar power-law tangent

A useful mathematical comparator is the passive auxiliary equation

```math
y''+(-x-i0)^\sigma y=0,\qquad 0<\sigma<1.
```

Write mu=1/(2+sigma). Its decaying positive-side solution is proportional to sqrt(x) H_mu^(2)(2mu exp(-i pi sigma/2)x^(1/(2mu))). Matching its constant and linear terms at zero to the two negative-side Hankel waves gives reflected/incoming coefficient ratio 2cos(pi mu)exp(-i pi mu), up to convention-dependent phase. Thus

```math
P_\sigma=4\cos^2\!\left(\frac{\pi}{2+\sigma}\right),\qquad
P_\sigma\sim\frac{\pi^2\sigma^2}{4}\quad(\sigma\downarrow0).
```

At sigma=1/2 this is the established 38% result [S1]. The general displayed identity is a direct standard-Bessel matching calculation used here as a comparator, not claimed as a new physical law or attributed to a paper that was not checked for that precise formula. Five exponents are verified with a separate ODE integration and exact Hankel decomposition.

Locally, our coefficient has F_L=1+V/L+..., while (-x-i0)^(1/L)=1+V/L+.... Therefore their leading reflection coefficients agree. A formal substitution sigma=1/L makes the coefficient plausible, but does not establish the uniform expansion, far-energy boundary control, or the physical finite-cycle limit. The exact logarithmic result is not P_sigma with a globally substituted exponent: their higher-order terms and far-energy behavior differ. Also, sigma is a power in the **energy-coordinate differential equation**, not the time-ramp exponent used in [S2].

This comparison narrows the novelty claim productively. The candidate contribution is a controlled logarithmic return law for the specified marginal threshold, not a new Bessel connection formula, a new Sturmian transform, or the first observation that threshold touching can lose a particle.

## 8. Decision boundary

This pass strengthens the outgoing matching and clarifies the spectral condition preventing a gapless adiabatic conclusion. It has not established a complete novelty theorem, a finite-size/residual-depth operating window or a laboratory implementation. Exact threshold contact, the order of limits, a prescribed quadratic control, and the initial bound state remain load-bearing.

The next valuable test concerns the **same physical protocol's finite-size and nonzero-minimum rounding scales**, rather than more exact repeats of the same audit or a new phenomenon. A result valid only after those ideal limits can still be important, but we should know whether a controlled finite regime exhibits its distinguishing behavior. No repository is requested and no existing project is modified in this pass.
