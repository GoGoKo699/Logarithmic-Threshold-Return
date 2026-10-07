# Gate B: the leading reflection and its physical outer matching

This note derives the leading reflection coefficient at exact touching, $`u=0`$,
with physical outer matching and explicit remainder estimates. It develops
[ASYMPTOTIC Sections 4–7](ASYMPTOTIC.md) and [AUDIT Sections 3–5](AUDIT.md).
The positive-minimum and finite-volume extensions are in
[Gate C](UNIFORM_MINIMUM.md) and [Gate D](FINITE_VOLUME.md).

The energy-to-time identification and finite-endpoint comparison are supplied by
[Gate A](AMPLITUDE_IDENTIFICATION.md). The argument below starts from its nonzero
physical recessive energy solution. WKB residual estimates and elliptic logarithms
are inherited tools [B1–B2]. The endpoint cancellation and exact-lattice error
estimates are derived below.

## 1. Exact coefficient, local replacement and the target error

Put $`e_*=32e^{-L}`$, $`e_*^2=\alpha\rho_0L`$, $`\rho_0=1/(4\pi)`$,
$`R=L^{1/4}`$ and $`B=L^2`$. In the scaled energy $`E=e_*x`$ the exact equation is

```math
y''+F_{\rm ex}(x)y=0,\qquad
F_{\rm ex}(x)=-\frac{\rho_0L}{g(e_*x)},\qquad
F_0(x)=\frac{L}{L-V(x)},\qquad V(x)=\ln|x|-i\pi\mathbf1_{x>0}.
```

$`F_0`$ is used locally, not beyond the whole physical band. A prime below denotes
an $`x`$ derivative unless another variable is specified. The target is a
phase-adjusted amplitude $`i\pi/(2L)+o(L^{-1})`$, not merely a probability tending
to zero. A convenient remainder scale is

```math
\mathcal Q_L=\frac1{LR}+\frac{R^2(1+\ln R)^2}{L^2}+e^{-cL},\qquad c>0.
```

The exact elliptic expression in ASYMPTOTIC and the convergent complementary-modulus
series [B2, Eq. 19.12.1] give, on each side of the lower edge,

```math
g(E)=-\rho_0[\ln32-\ln(-E-i0)]+\gamma(E),\qquad
|\gamma^{(j)}(E)|\le C|E|^{1-j}(1+|\ln|E||),\quad j=0,1,2.
```

To justify differentiation, substitute $`1-m=(-E)(8-E)/(4-E)^2`$ in the negative-side
elliptic formula, and use the two real elliptic expressions inside the band. In [B2]
the expansion variable is the complementary **modulus squared**; the repository's
$`m`$ is the elliptic parameter. On a sufficiently small fixed edge neighborhood,
termwise derivatives of the convergent power-log series bound the omitted terms
as displayed. No derivative of an unspecified big-O term is assumed.

Inverting the resolvent now gives

```math
\int_{-R}^{R}|F_{\rm ex}-F_0|\,dx\le Ce_*R^2,\qquad
|\partial_x^j(F_{\rm ex}-F_0)|\le Ce_*|x|^{1-j},\quad
R\le|x|\le B,\quad j=0,1,2,
```

for sufficiently large $`L`$. The first bound also covers $`x\to0`$: the large
negative logarithm increases the denominator. On $`[R,B]`$, $`L-\ln x\asymp L`$;
the bounds on the derivatives follow by the quotient rule. These errors and their
endpoint-basis effects are smaller than $`\mathcal Q_L`$.

## 2. Physical passivity controls the positive side without an absorber

For the **exact** physical coefficient, $`\mathop{\mathrm{Im}}\nolimits F_{\rm ex}\le0`$ in
the spectral band. The current

```math
j=\mathop{\mathrm{Im}}\nolimits (\overline y\,y'),\qquad
j'=-\mathop{\mathrm{Im}}\nolimits F_{\rm ex}|y|^2
```

is nondecreasing there, and is zero in the real evanescent region beyond the upper
edge for the recessive solution. Consequently $`j\le0`$ at all preceding energies.
The reciprocal resolvent has continuous zero limits at the spectral singularities;
there are no point-current sources to add at the band edges or at energy 4.
Thus the actual far band supplies a passive load at $`B`$, rather than a chosen
numerical absorbing condition.

On $`[R,B]`$ use the exact $`q=\sqrt{F_{\rm ex}}`$, with positive real part,
$`h=q'/q`$, and $`\Omega=h^2/4-h'/2`$. A chart that does not exclude zeros of $`y`$ is

```math
r=\frac{y'+(h/2+iq)y}{(iq-h/2)y-y'},\qquad
r'=2iqr+\frac{i\Omega}{2q}(1+r)^2.
```

The differential identity follows by substitution of $`y''=-q^2y`$.
Where $`y\ne0`$, passivity says $`\mathop{\mathrm{Im}}\nolimits (y'/y)\le0`$. Hence

```math
|iq-y'/y-h/2|\ge\mathop{\mathrm{Re}}\nolimits q-|h|/2.
```

For large $`L`$, $`|h|\le\mathop{\mathrm{Re}}\nolimits q`$ and
$`|q|/\mathop{\mathrm{Re}}\nolimits q\le\sqrt2`$ throughout this interval. Therefore
$`|r|\le1+4\sqrt2<7`$. At a zero of $`y`$, uniqueness gives $`y'\ne0`$ and
$`r=-1`$; the denominator is still nonzero. This also includes a Dirichlet terminal
load. The bound uses no favorable sign of the small lattice correction to $`h`$.

Define $`\mathcal A=\int_R^B-\mathop{\mathrm{Im}}\nolimits q\,dx`$ and
$`\mathcal I_+=\int_R^B|\Omega/q|\,dx`$. Backwards variation of constants gives

```math
|r(R)|\le7e^{-2\mathcal A}+32\mathcal I_+.
```

For the local coefficient, writing $`D=L-\ln x+i\pi`$ gives the exact identities

```math
h_0=\frac1{2xD},\qquad
\Omega_0=\frac1{4x^2D}-\frac3{16x^2D^2}.
```

Since $`D\asymp L`$, $`\mathcal I_+=O((LR)^{-1})+O(e_*\ln B+e_*^2B)`$.
The last two terms follow from the derivative bounds of Section 1 and are
exponentially small. Uniformly on this interval,

```math
-\mathop{\mathrm{Im}}\nolimits q_0=\frac{\pi}{2L}
\left[1+O\!\left(\frac{\ln L}{L}\right)\right].
```

The integrated lattice correction is $`O(e_*B^2)`$, so
$`\mathcal A=\pi L/2[1+o(1)]`$ and is at least $`\pi L/4`$ eventually.
It follows that the exact physical outgoing data at $`R`$ have
$`r(R)=O((LR)^{-1})+O(e^{-cL})`$.

For $`F_0`$ itself, the earlier stronger bound
$`4e^{-2\mathcal A}+(25/2)\mathcal I_+`$ in AUDIT remains valid. The constants
7 and 32 above simply avoid relying on preservation of $`\mathop{\mathrm{Im}}\nolimits h_0<0`$
when transferring the estimate to the exact lattice. No old finite bound is changed.

## 3. The negative tail can be bounded directly from the exact spectral measure

This avoids extending the local logarithm to its artificial far-negative pole.
Let $`\epsilon=-E>0`$ and use the exact positive spectral measure:

```math
G(\epsilon)=-g(-\epsilon)=\int_0^8\frac{\rho(E)}{E+\epsilon}\,dE,
\qquad W(-\epsilon)=\frac1{G(\epsilon)}.
```

On the whole negative axis $`q,h`$ are real, $`q>0`$, and the same current gives
$`|r|\le1`$. Remove the purely oscillatory factor $`e^{2i\int q}`$ in the
reflection equation. The change in the phase-adjusted reflection is bounded by
$`2\mathcal I_-`$, where the exact energy-coordinate substitution yields

```math
\mathcal I_-=\int_{-\infty}^{-R}|\Omega/q|\,dx
=\sqrt\alpha\int_{e_*R}^{\infty}
\left[\frac{G''(\epsilon)}{4\sqrt{G(\epsilon)}}
-\frac{3G'(\epsilon)^2}{16G(\epsilon)^{3/2}}\right]d\epsilon.
```

Primes in this formula are $`\epsilon`$ derivatives. To check the conversion,
$`q=e_*p`$, $`p=\sqrt{W/\alpha}`$, and
$`\Omega/p=\sqrt\alpha[5W'^2/(16W^{5/2})-W''/(4W^{3/2})]`$ in physical energy.
Substitute $`W=1/G`$. The measure gives
$`GG''\ge2G'^2`$ by Cauchy–Schwarz, so the displayed integrand is nonnegative;
no absolute-value cancellation has been used in this equality.

The lower-edge density is bounded above and below by positive constants in a fixed
small energy interval. Splitting the measure there gives
$`G\ge c\ln(32/\epsilon)`$ and $`G''\le C\epsilon^{-2}`$ for small $`\epsilon`$.
The upper part of the measure has finite total mass, even though its density has
a middle-band singularity. For $`D=\ln(32/\epsilon)`$,

```math
\int_{a}^{\epsilon_0}\frac{d\epsilon}{\epsilon^2\sqrt{\ln(32/\epsilon)}}
\le\frac{C}{a\sqrt{\ln(32/a)}}.
```

Indeed, this is an integral of $`e^D/\sqrt D`$; for $`D\ge1`$ its derivative is
at least half of itself. On $`\epsilon\ge\epsilon_0`$ the remaining integrand is
integrable: its large-$`\epsilon`$ asymptotic is $`5/(16\epsilon^{5/2})`$ because
the spectral measure has unit mass and bounded support. Therefore

```math
\mathcal I_-\le\frac{C\sqrt\alpha}{e_*R\sqrt{L-\ln R}}+C\sqrt\alpha
=O\!\left(\frac1{LR}\right)+O(\sqrt\alpha).
```

This controls the entire exact negative-energy tail and exhibits the coordinate
factor explicitly. The phase-adjusted limit of $`r`$ exists by the integrable
reflection equation, and is the WKB coefficient ratio used in Gate A. No additional
turning point or incoming channel is introduced.

## 4. Central transfer and the two endpoint matrices

On $`[-R,R]`$ the integrated expansion is

```math
F_{\rm ex}=1+V/L+\mathcal R,\qquad
\|\mathcal R\|_1\le C\frac{1+R(1+\ln R)^2}{L^2}+Ce_*R^2,
\qquad \|F_{\rm ex}-1\|_1=O\!\left(\frac{R(1+\ln R)}L\right).
```

For $`|x|<1`$, $`L-\ln|x|\ge L`$ and the first two powers of the logarithm are
integrable. For $`1\le|x|\le R`$, the denominator is at least $`L/2`$ eventually.
These facts prove the bounds; a pointwise Taylor expansion at zero is not required.

Write $`y=Ae^{-ix}+Ce^{ix}`$, with the usual variation constraint. Then

```math
\binom{A}{C}'=\frac{i(F_{\rm ex}-1)}2
\begin{pmatrix}-1&-e^{2ix}\\e^{-2ix}&1\end{pmatrix}\binom{A}{C}.
```

The plane-wave matrix and its inverse have bounded norms on the real interval.
The integral equation therefore has second-order remainder bounded by
$`C\|F_{\rm ex}-1\|_1^2e^{C\|F_{\rm ex}-1\|_1}`$. Propagation is from $`R`$ to
$`-R`$, so its first-order lower-left entry is
$`-i(2L)^{-1}\int_{-R}^{R}Ve^{-2ix}dx`$.

Specify the local wave basis at an endpoint $`s=\pm R`$ by the columns

```math
\mathsf W(s)=q(s)^{-1/2}
\begin{pmatrix}
e^{-is}&e^{is}\\
[-h(s)/2-iq(s)]e^{-is}&[-h(s)/2+iq(s)]e^{is}
\end{pmatrix}.
```

The phases $`e^{\pm is}`$ set a convention at each endpoint; they do not assert
that the outer WKB phase is globally $`x`$. If $`\mathsf P`$ is the analogous
plane-wave matrix with $`q=1,h=0`$, direct inversion gives

```math
\mathsf P(s)^{-1}\mathsf W(s)
=I-\frac{V(s)}{4L}
\begin{pmatrix}0&e^{2is}\\e^{-2is}&0\end{pmatrix}
+O\!\left(\frac1{LR}+\frac{(1+\ln R)^2}{L^2}+e_*R\right).
```

In particular, there is no linear diagonal term from $`q-1`$; the amplitude
normalization $`q^{-1/2}`$ cancels it. This is the explicit basis change missing
from a bare instruction to cancel the endpoints.

Section 2 makes the right-end reflected/incident ratio small enough to replace
it by zero at cost $`O((LR)^{-1})+O(e^{-cL})`$. Composing the right basis change,
backwards transfer, and inverse left basis change gives the phase-adjusted left
ratio

```math
\begin{aligned}
r_c={}&-\frac{i}{2L}\int_{-R}^RV(x)e^{-2ix}\,dx\\
&-\frac{V(R)e^{-2iR}-V(-R)e^{2iR}}{4L}
+O(\mathcal Q_L).
\end{aligned}
```

The normalized incident denominator is $`1+O(R(1+\ln R)/L)`$. Expanding its
inverse contributes only to the stated second-order remainder. Thus the second
line is a required first-order basis contribution, not a correction that can be
silently discarded. The transfer integral alone contains artificial boundary terms.

## 5. Both causal contributions survive, with equal leading signs

In distributions, $`V'=\mathop{\mathrm{PV}}\nolimits (1/x)-i\pi\delta(x)`$. Integration by
parts in the preceding expression cancels its explicit boundary term and gives

```math
r_c=-\frac1{4L}\int_{-R}^{R}
\left[\mathop{\mathrm{PV}}\nolimits \frac1x-i\pi\delta(x)\right]e^{-2ix}dx
+O(\mathcal Q_L)
=\frac{i}{4L}[2\mathop{\mathrm{Si}}\nolimits (2R)+\pi]+O(\mathcal Q_L).
```

This identity can also be obtained by separately integrating the ordinary
$`\ln|x|`$ and step-function terms; no singular core is removed. The principal-value
part tends to $`-i\pi`$, and the delta part is $`-i\pi`$ exactly. Each contributes
$`i\pi/(4L)`$ at leading order. Using the opposite branch or retaining only the
real logarithm is a different boundary problem, not an equivalent approximation.

The sine-integral tail is $`O(R^{-1})`$. Section 3 changes $`r_c`$ only by a unit
phase and $`O((LR)^{-1})+O(\sqrt\alpha)`$ on passage to the deep-bound amplitudes.
Combining with Gate A and $`R=L^{1/4}`$ gives the existing conclusion

```math
r_{\rm aux}=e^{i\theta_L}
\left[\frac{i\pi}{2L}+O(L^{-5/4})\right],\qquad
P_\infty(T,0)=\frac{\pi^2}{4L^2}[1+o(1)].
```

The displayed amplitude refers to the auxiliary bound-channel ratio up to its
phase convention; the original finite-cycle amplitude modulus differs by
$`O(T^{-1})`$ as in Gate A. Since $`T^{-1}=o(L^{-5/4})`$, that comparison does not
change the probability statement. No phase observable or sharp finite-time error
bar is asserted.

## 6. Numerical diagnostics and the positive-minimum extension

The endpoint matrices, exact-lattice passive bound and spectral-measure estimate
for the entire negative tail connect the central reflection calculation to the
physical channels of Gate A.

`python tools/test_reflection_matching.py --output NEW_PATH.json` runs six small
checks: the basis/Riccati algebra, distributional cancellation, finite central
transfers, passive terminal examples including a zero of $`y`$, exact negative-tail
integrals, and high-precision local coefficient derivatives. These finite checks
are separate from the original 272 controls; they do not prove the asymptotic
bounds by sampling or simulate time-domain threshold dynamics. The initial
structural symbolic-zero assertion failure and its canonicalization repair are
retained in [the failure record](../archive/GATE_B_DIAGNOSTIC_FAILURE.md).

[Gate C](UNIFORM_MINIMUM.md) establishes uniformity for the positive-minimum
family. A result for every fixed minimum parameter below the boundary alone
would not establish a uniform result along varying parameter sequences.

### Method sources and actual access

[B1] NIST Digital Library of Mathematical Functions, [Section 2.7(iii)](https://dlmf.nist.gov/2.7#iii),
Eqs. 2.7.20–25: HTML discussion and error-control expressions checked. This is a
method reference, not a direct application of its real-exponential theorem to the
complex physical band. The current and reflection inequalities above are derived
explicitly for this problem. The underlying book was not newly read.

[B2] NIST Digital Library of Mathematical Functions, [Section 19.12](https://dlmf.nist.gov/19.12),
Eqs. 19.12.1–3: HTML convergent elliptic series and modulus conventions checked.
These series support the local derivative expansion.
