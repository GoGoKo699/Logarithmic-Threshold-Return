# From the selected tutorial to logarithmic return

**6 October 2026. A learning bridge to the existing author-side result.**
Start with the single-book route in [TUTORIAL](../TUTORIAL.md). This note
restates the fixed argument at base `3b944c727d3f6aafb9431ede8a28a4b97d6e25a5`;
the linked proof notes remain authoritative. It adds no theorem or verification claim.

The physical question is simple: a particle starts bound to a local trap, the
trap weakens and returns, and we ask how much returns to the initial bound
orbital. Near threshold, the instantaneous bound orbital becomes shallow and
spatially extended. Near the continuum edge, a fixed-gap adiabatic
argument no longer answers the question uniformly.

## 1. Translate the potential and the resolvent

The lattice impurity is exactly rank one. Set energy and time units to
$`J=\hbar=1`$, let $`Q=|0\rangle\langle0|`$, and write

```math
H(t)=H_0-U(t)Q,\qquad U(t)=u+\alpha t^2,\qquad
\alpha=(4-u)/T^2,\qquad -T\le t\le T.
```

Here $`H_0`$ is the nearest-neighbor square-lattice Laplacian with band
$`[0,8]`$. The endpoint attraction is 4 and $`T`$ is half the cycle duration.
The observable is

```math
P_\infty(T,u)=|\langle b_4|\mathcal U(T,-T)|b_4\rangle|^2.
```

The normalized orbital $`|b_4\rangle`$ extends over multiple sites. Its
projection is different from occupation of site 0. Probability is unconditional:
escaped population is not discarded before normalization. See [CORE](CORE.md).

The book's Chapter 9 preview uses the operator $`(H_0-E)^{-1}`$.
Our local retarded convention is

```math
g(E)=\langle0|(E-H_0+i0)^{-1}|0\rangle.
```

Below the band, the local matrix element of the book's resolvent is $`-g(E)`$.
Above threshold the boundary prescription must also be specified; the sign
translation alone does not choose an incoming or outgoing solution.
The lattice model requires no continuum contact-potential regularization.

## 2. A shallow bound state is exponentially close to the band

At fixed attraction $`U>0`$, write the bound energy as $`E=-\eta`$ and
$`G(\eta)=-g(-\eta)>0`$. The rank-one eigenvalue equation reduces to

```math
1=UG(\eta),\qquad
G(\eta)=\rho_0\ln(32/\eta)+O(\eta\ln(1/\eta)),\qquad \rho_0=\frac1{4\pi},
\qquad \eta(U)\sim32e^{-1/(\rho_0U)}.
```

The normalized bound vector can be chosen as
$`|b_U\rangle=(H_0+\eta)^{-1}|0\rangle/\sqrt{-G'(\eta)}`$:
the squared norm of its numerator is $`-G'(\eta)`$. This gives the orbital
whose endpoint projector defines return; see [Gate D, Section 2](FINITE_VOLUME.md).

The logarithm is in the local Green function. The lower-edge density of states
is finite and nonzero; the middle-band van Hove singularity is a separate
feature. The small gap therefore closes essentially, rather than as a finite
power of $`U`$. This is the first model-specific ingredient to bring to the
book's threshold-dynamics methods. See [SPECTRAL_SCOPE](SPECTRAL_SCOPE.md) and
[ASYMPTOTIC, Section 4](ASYMPTOTIC.md).

## 3. Quadratic time dependence becomes an energy equation

Extend the parabola to all real times as an auxiliary problem. With inverse
Fourier phase $`e^{-iEt}`$, let $`c(E)`$ transform the contact amplitude.
Multiplication by $`t^2`$ becomes $`-\partial_E^2`$. The transformed source
equation and retarded reconstruction give

```math
(E-H_0)\widehat\Psi(E)=|0\rangle[\alpha c''(E)-uc(E)],
\qquad c=g(\alpha c''-uc),
\qquad c''+\frac{-1/g-u}{\alpha}c=0.
```

The reduction packages the lattice into one scalar function $`g`$. It still
needs a physical boundary condition: the solution recessive at positive
infinity and the retarded reconstruction specify no incoming continuum.
The complex coefficient inside the band describes outgoing continuum
population in this representation; the physical time evolution is unitary.
The distributional and norm-level justification is [Gate A, Sections 2–3](AMPLITUDE_IDENTIFICATION.md).

On the sufficiently negative energy leg, put $`p^2=(-1/g-u)/\alpha>0`$.
The modes $`p^{-1/2}e^{\mp iS}`$, with $`S'=p`$, have stationary times
$`t=\mp p`$: they label the past and future bound legs. For $`u>0`$ there is
a small turning region near threshold; this oscillatory description is not
asserted for every negative energy.

Writing $`c\sim p^{-1/2}(a_-e^{-iS}+a_+e^{iS})`$ on that remote leg,
equal bound-leg normalization gives $`P_{\rm aux}=|a_+/a_-|^2`$.
Taking remote time first at fixed $`\alpha,u`$, [Gate A](AMPLITUDE_IDENTIFICATION.md)
then compares it with the finite cycle:

```math
\left|\sqrt{P_\infty(T,u)}-\sqrt{P_{\rm aux}(\alpha,u)}\right|
\le C_{u_*}/T,\qquad 0\le u\le u_*<4.
```

This is a comparison of amplitude moduli. It does not identify arbitrary
complex phases between representations.

## 4. The causal logarithm makes reflection small

Set $`e_*^2=\alpha\rho_0L`$, $`L=\ln(32/e_*)`$, $`E=e_*x`$ and
$`b=\rho_0uL`$. The exact scaled coefficient and its threshold form are

```math
y''+F_by=0,\qquad F_b=-\frac{\rho_0L}{g(e_*x)}-b,
\qquad F_b^0=\frac{L}{L-V(x)}-b,
\qquad V(x)=\ln|x|-i\pi\mathbf1_{x>0}.
```

For $`b\le1-\delta`$ with fixed $`\delta>0`$, the reference wave number
is $`k=\sqrt{1-b}\ge\sqrt\delta`$. Away from zero the coefficient approaches
$`k^2`$, suggesting weak reflection. A uniform pointwise Taylor expansion at
zero is false. The proof instead controls the integrated central error and
matches to the exact outer lattice equation.

After endpoint cancellation and a phase choice, the leading reflected
amplitude is

```math
\widetilde r_{L,b}=
-\frac1{4Lk^2}\int_{-R}^{R}
\left[\operatorname{PV}\frac1x-i\pi\delta_0(x)\right]e^{-2ikx}\,dx
+o_\delta(L^{-1})
=\frac{i\pi}{2L(1-b)}+o_\delta(L^{-1}),\qquad R=L^{1/4}.
```

Here $`\delta_0`$ is the Dirac distribution, distinct from the fixed margin
$`\delta`$. The principal-value integral tends to $`-i\pi`$ and the causal
jump supplies another $`-i\pi`$. Both are needed for the coefficient.
This is an explanation of the existing matched calculation, not a stand-alone
Born approximation valid across the entire band. [Gate B](REFLECTION_MATCHING.md)
controls exact touching; [Gate C](UNIFORM_MINIMUM.md) controls the full stated
minimum-depth family, including its turning region.

Squaring the amplitude and using the finite-endpoint comparison yields
$`P_\infty=\pi^2/[4L^2(1-b)^2]\,[1+o(1)]`$. At $`u=0`$,
$`L\sim\ln T`$ and the return tends to zero as $`\pi^2/(4\ln^2T)`$.

## 5. Read the limit before applying the formula

| Parameters as the cycle slows | Conclusion within the recorded claim |
|---|---|
| Infinite lattice, exact touching | Logarithmically vanishing bound return |
| $`u=b/(\rho_0L)`$, $`0\le b\le1-\delta`$, fixed $`0<\delta\le1`$ | Uniform leading law above |
| Periodic squares with $`n(T)=2\lceil4.5T\rceil+1`$, in the same $`0\le\rho_0uL\le1-\delta`$ family | Same law along a sufficient growing family, using each lattice's own endpoint orbital |
| Fixed positive minimum or fixed finite square | Ultimate adiabatic return; constants need not stay uniform as the gap closes or size grows |

The finite-square statement follows from localized endpoint states, a propagation
bound and a seam comparison in [Gate D](FINITE_VOLUME.md). It is not obtained
by substituting a discrete density of states into the infinite-lattice logarithm.
The size is sufficient, not optimal. The margin below $`b=1`$ stays fixed;
the formula is not a complete crossover or a finite-time precision guarantee.
See [PROOF_STATUS](PROOF_STATUS.md) for the exact supremum statement and
[LIMITS_AND_ACCURACY](LIMITS_AND_ACCURACY.md) for the remaining boundaries.

## What understanding this bridge should enable

Explain why the static logarithm gives essential binding, why the drive becomes
a second-order energy equation, and why its reflection coefficient requires a
separate physical normalization. Then explain how the causal jump fixes the
leading coefficient and why fixed and joint limits differ. The reading checkpoints
in [TUTORIAL](../TUTORIAL.md) guide that process.

The tutorial supplies background machinery. The project's derivations, precise
predecessor attributions and scientific limitations remain in the linked research
and literature records. A tutorial choice establishes neither priority nor
independent review, and introduces no new manuscript or outreach step.
