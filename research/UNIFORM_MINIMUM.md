# Gate C: uniform return while the trap stays attractive

This note proves uniform logarithmic return for the positive-minimum family in
[ROUNDING Sections 2–4](ROUNDING.md), using the exact-lattice estimates of
[Gate B](REFLECTION_MATCHING.md) and the physical-channel identification of
[Gate A](AMPLITUDE_IDENTIFICATION.md).

## 1. Quantifiers and the physical parameters

Fix $`0<\delta<1`$. All constants below may depend on this fixed margin but not on
$`b\in[0,1-\delta]`$. The case $`\delta=1`$ is just zero minimum. Parameterize the
whole family, rather than treating a sequence of fixed-$`b`$ examples:

```math
\rho_0=\frac1{4\pi},\quad e_*=32e^{-L},\quad
u=\frac{b}{\rho_0L},\quad \alpha=\frac{e_*^2}{\rho_0L},\quad
T=\frac{\sqrt{(4-u)\rho_0L}}{e_*}.
```

For large $`L`$, uniformly $`0\le u\le u_*<4`$, and these definitions give exactly
$`\alpha=(4-u)/T^2`$ and the implicit logarithm equation in CORE. Remote time in
Gate A is still taken first at fixed $`\alpha,u`$. This parameterization does not
assert a new order of limits. Write

```math
k=\sqrt{1-b}\in[\sqrt\delta,1],\qquad R=L^{1/4},\quad B=L^2,
\qquad F_b(x)=-\frac{\rho_0L}{g(e_*x)}-b,\quad
F_b^0(x)=\frac{L}{L-V(x)}-b,
\quad V=\ln|x|-i\pi\mathbf1_{x>0}.
```

The exact equation is $`y''+F_b y=0`$. The replacement error
$`\Delta=F_b-F_b^0`$ is **exactly independent of $`b`$**. Gate B Section 1 gives
its integrated central bound $`Ce_*R^2`$ and its outer derivative bounds
$`|\Delta^{(j)}|\le Ce_*|x|^{1-j}`$, $`j=0,1,2`$, on $`R\le|x|\le B`$.
Those bounds come from convergent elliptic series, not differentiation of an
unspecified remainder [C1]. The desired statement is uniform after an irrelevant
phase choice:

```math
r_{L,b}=e^{i\theta_{L,b}}\left\{\frac{i\pi}{2L(1-b)}
+O_\delta\!\left(\frac1{LR}+\frac{R^2(1+\ln R)^2}{L^2}+e^{-cL}\right)\right\}.
```

The positive constant $`c`$ can be reduced to absorb polynomial factors. It does
not have to describe a sharp finite-$`L`$ error bar.

## 2. Central transfer includes the forbidden region

A second exact cancellation of the offset is decisive:

```math
F_b-k^2=F_0-1,\qquad
F_b^0=k^2+\frac VL+\frac{V^2}{L(L-V)}.
```

The subscript $`0`$ on $`F_0`$ here means the exact zero-minimum coefficient.
For $`|x|<1`$, put $`t=-\ln|x|`$. The measure becomes $`e^{-t}dt`$ and
$`|L-V|\ge L`$. On $`1\le|x|\le R`$, $`\mathop{\mathrm{Re}}\nolimits (L-V)\ge L/2`$
eventually. Thus, without removing any neighborhood of zero,

```math
F_b=k^2+V/L+\mathcal R,\qquad
\|\mathcal R\|_1\le C\frac{1+R(1+\ln R)^2}{L^2}+Ce_*R^2,\qquad
\|F_b-k^2\|_1\le C\frac{R(1+\ln R)}L+Ce_*R^2.
```

These constants are independent even of $`b`$ before conversion to wave amplitudes.
At zero $`F_b\to-b`$, so a uniform pointwise expansion would be false. For $`b>0`$
there is one negative-energy turning point: $`W(\eta)=1/G(\eta)=u`$ with
$`G(\eta)=-g(-\eta)`$. Monotonicity of $`G`$ makes it unique. At
$`|x|=e^{-\delta L/2}`$, the exact unshifted coefficient is
$`(1+\delta/2)^{-1}+o(1)>1-\delta`$. Therefore the turning point lies at
$`|x_t|<e^{-\delta L/2}`$ for sufficiently large $`L`$, uniformly over positive
$`b\le1-\delta`$. This location is explanatory only: the estimates above include
that entire region and do not rely on excising it or resolving it pointwise.

Use $`k^{-1/2}e^{\mp ikx}`$ as the two reference waves. Variation of constants gives

```math
\frac{d}{dx}\binom{A}{C}=\frac{i(F_b-k^2)}{2k}
\begin{pmatrix}-1&-e^{2ikx}\\e^{-2ikx}&1\end{pmatrix}\binom{A}{C}.
```

Since $`k^{-1}\le\delta^{-1/2}`$, the Volterra series has a second-order bound
$`C_\delta\|F_b-k^2\|_1^2 e^{C_\delta\|F_b-k^2\|_1}`$ uniformly. This is the
source of uniform transfer control, not a collection of fixed-$`b`$ limits.

## 3. Positive outer matching does not assume a sign for the logarithmic derivative

For the physical recessive solution the current satisfies
$`j'=-\mathop{\mathrm{Im}}\nolimits F_b|y|^2\ge0`$ in the band, with zero current beyond its
upper edge. Subtracting real $`b`$ changes neither sign nor the absence of point
sources at spectral singularities. Hence $`j\le0`$ as in Gate B.

On $`[R,B]`$, $`F_b=k^2+O(\ln L/L)+O(e_*B)`$, uniformly. For the exact square
root $`q=\sqrt{F_b}`$ choose positive real part and nonpositive imaginary part;
set $`h=q'/q`$, $`\Omega=h^2/4-h'/2`$. For $`L\ge L_\delta`$,
$`\mathop{\mathrm{Re}}\nolimits q\ge\sqrt\delta/2`$, $`|q|/\mathop{\mathrm{Re}}\nolimits q\le\sqrt2`$,
and $`|h|\le\mathop{\mathrm{Re}}\nolimits q`$. Where $`y\ne0`$, $`m=y'/y`$ obeys

```math
|iq-m-h/2|\ge\mathop{\mathrm{Re}}\nolimits q-|h|/2\ge\tfrac12\mathop{\mathrm{Re}}\nolimits q.
```

The nonsingular chart
$`r=[y'+(h/2+iq)y]/[(iq-h/2)y-y']`$ consequently has $`|r|<7`$; at a zero
of $`y`$ it equals $`-1`$. Neither the denominator nor this conclusion uses
$`\mathop{\mathrm{Im}}\nolimits h\le0`$. Indeed that sign can reverse after subtracting $`b`$.
The exact Riccati identity is still

```math
r'=2iqr+\frac{i\Omega}{2q}(1+r)^2,\qquad
|r(R)|\le7e^{-2\mathcal A}+32\mathcal I_+,
\quad \mathcal A=\int_R^B-\mathop{\mathrm{Im}}\nolimits q\,dx,\quad
\mathcal I_+=\int_R^B|\Omega/q|\,dx.
```

To track constants, put $`D=L-\ln x+i\pi`$ for the local coefficient. Then

```math
(F_b^0)'=\frac{L}{xD^2},\qquad
(F_b^0)''=\frac{L(2-D)}{x^2D^3},\qquad
h^0=\frac{L}{2xD(L-bD)},\qquad
\frac\Omega q=\frac{5F_b'^2}{16F_b^{5/2}}-\frac{F_b''}{4F_b^{3/2}}.
```

All inverse powers of $`F_b`$ are controlled by the fixed margin. Gate B's
$`C^2`$ replacement bounds give
$`\mathcal I_+=O_\delta((LR)^{-1}+e_*\ln B+e_*^2B)`$.
Also $`-\mathop{\mathrm{Im}}\nolimits \sqrt{F_b^0}=\pi/(2Lk)[1+O_\delta(\ln L/L)]`$.
The integrated exact-root correction is $`O_\delta(e_*B^2)`$, so
$`\mathcal A=\pi L/(2k)[1+o_\delta(1)]\ge\pi L/4`$ eventually. Thus the
physical right-end data have reflection $`O_\delta((LR)^{-1})+O(e^{-cL})`$,
independently of the particular passive load inherited from the rest of the band.
No local logarithm is extrapolated across that whole band.

## 4. A shifted spectral-measure bound controls the entire negative tail

Let $`a=e_*R`$, $`W(\eta)=1/G(\eta)`$, and $`K_u=W-u`$ for $`\eta\ge a`$.
The exact lower-edge expansion gives

```math
uG(a)=b\left[1-\frac{\ln R}{L}+O(a)\right]\le1-\delta/2
```

for sufficiently large $`L`$. Since $`G`$ decreases, this implies the global bound
$`K_u\ge(\delta/2)W>0`$ on the **whole** negative outer interval. It rules out
additional outer turning points without an approximation at deep energies.

For the unit-mass positive spectral measure,
$`G'= -\int\rho(E)(E+\eta)^{-2}dE`$ and
$`G''=2\int\rho(E)(E+\eta)^{-3}dE`$. Cauchy–Schwarz gives
$`GG''\ge2G'^2`$, hence $`W'>0`$ and $`W''\le0`$. With derivatives now taken
in $`\eta`$, the exact physical-energy change of variables yields

```math
\mathcal I_-(u)=\sqrt\alpha\int_a^\infty
\left[\frac{5W'^2}{16(W-u)^{5/2}}-\frac{W''}{4(W-u)^{3/2}}\right]d\eta.
```

Both displayed terms are nonnegative. Their powers of $`W-u`$ can therefore be
bounded separately, without losing a cancellation or differentiating an asymptotic:

```math
\boxed{\mathcal I_-(u)\le(2/\delta)^{5/2}\mathcal I_-(0)
=O_\delta((LR)^{-1})+O_\delta(\sqrt\alpha).}
```

Here $`\mathcal I_-(0)`$ uses the same $`\alpha,a`$; it is the exact integral
already bounded in Gate B Section 3, not a second physical cycle. On this interval
$`q,h`$ are real and current passivity gives $`|r|\le1`$. The phase-adjusted
reflection changes by at most $`2\mathcal I_-(u)`$ on passage to the deep-bound
coefficients. The factor $`\sqrt\alpha`$ and the positive-margin inequality are
both essential. Copying the zero-minimum integral without shifting its denominators
would not establish the desired uniformity.

## 5. Endpoint cancellation, coefficient and finite-time comparison

At $`s=\pm R`$, let $`\mathsf P_k(s)`$ have columns
$`k^{-1/2}(1,\mp ik)^T e^{\mp iks}`$ and let $`\mathsf W_b(s)`$ have columns
$`q^{-1/2}(1,-h/2\mp iq)^T e^{\mp iks}`$. Direct inversion gives

```math
\mathsf P_k(s)^{-1}\mathsf W_b(s)
=I-\frac{V(s)}{4Lk^2}
\begin{pmatrix}0&e^{2iks}\\e^{-2iks}&0\end{pmatrix}
+O_\delta\!\left(\frac1{LR}+\frac{(1+\ln R)^2}{L^2}+e_*R\right).
```

The normalization removes the linear diagonal term for every permitted $`k`$.
Composing the right basis, backwards central transfer and inverse left basis,
then expanding the incident denominator, gives

```math
r_c=-\frac{i}{2kL}\int_{-R}^RV e^{-2ikx}dx
-\frac{V(R)e^{-2ikR}-V(-R)e^{2ikR}}{4Lk^2}+O_\delta(\mathcal Q_L)
=\frac{i[2\mathop{\mathrm{Si}}\nolimits (2kR)+\pi]}{4Lk^2}+O_\delta(\mathcal Q_L),
```

where $`\mathcal Q_L=(LR)^{-1}+R^2(1+\ln R)^2/L^2+e^{-cL}`$.
The identity uses both terms of
$`V'=\mathop{\mathrm{PV}}\nolimits (1/x)-i\pi\delta(x)`$. The bound
$`|\mathop{\mathrm{Si}}\nolimits (2kR)-\pi/2|\le1/(kR)`$ is uniform for
$`k\ge\sqrt\delta`$. Sections 3–4 give the claimed auxiliary amplitude in
Section 1, with remainder $`O_\delta(L^{-5/4})`$.

Gate A's uniform $`O(T^{-1})`$ amplitude-modulus comparison applies because
$`u\le u_*<4`$ eventually. In this parameterization
$`T^{-1}=O(e^{-L}/\sqrt L)`$ uniformly. Squaring, and using
$`\pi/[2L(1-b)]\ge\pi/(2L)`$, proves the explicit uniform conclusion

```math
\sup_{0\le b\le1-\delta}
\left|\frac{4L^2(1-b)^2}{\pi^2}P_\infty(T(L,b),u(L,b))-1\right|
=O_\delta(L^{-1/4})\longrightarrow0.
```

This is the already claimed joint law, with its quantifiers exposed. It is not
uniform as $`\delta\downarrow0`$, is not a statement at $`b=1`$, and does not
supply a fixed-positive-$`u`$ crossover or a finite-volume proof.

## Numerical diagnostics and source

Uniformity follows from the offset-independent central perturbation, the passive
denominator bound and domination of the exact shifted negative-tail defect.

`python tools/test_uniform_minimum.py --output NEW_PATH.json` supplies small
symbolic, integral and finite-ODE diagnostics. Their sampled parameter values do
not prove the supremum above. These checks are separate from the original 272
controls and do not simulate exponentially long physical cycles.

[C1] NIST DLMF [Section 19.12](https://dlmf.nist.gov/19.12), Eqs. 19.12.1–3:
The HTML convergent series and complementary-modulus convention were checked.
They support the inherited local expansion. No textbook was read for this source
check.
