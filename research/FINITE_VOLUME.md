# Gate D: finite volume without replacing the initial state

**5 October 2026. Author-side lemma chain; not a separate-reader report.**
This expands [ROUNDING Section 6](ROUNDING.md) for the same periodic squares and
quadratic cycle. The protected proof, observable, leading coefficient and sufficient
size family are unchanged. No smaller necessary size, new boundary condition, or
experimental implementation is claimed. [The proof map](PROOF_STATUS.md) collects
the four author-side gates after this pass.

## 1. Statement, embeddings and constants

Let $`n=2R+1\ge3`$, $`\Lambda_R=\{-R,\ldots,R\}^2`$, and let $`E_n`$ extend a
torus vector by zero outside $`\Lambda_R`$. The finite and infinite free operators
are $`H_{0,n}`$ and $`H_{0,\infty}`$, with spectrum in $`[0,8]`$. Both have diagonal
4 and hopping -1 to their four neighbors. Write

```math
H_j(t)=H_{0,j}-[u+(4-u)(t/T)^2]Q_j,\qquad
\psi_j(-T)=b_j,\qquad j\in\{n,\infty\},
```

where $`b_j`$ is the positive real normalized endpoint bound vector at attraction
4, and its energy is $`-\eta_j`$. Thus $`b_n`$ and $`b_\infty`$ are different
vectors in different spaces. Only $`E_n b_n`$ is compared with $`b_\infty`$.

Define the entirely analytic lower bound and weight constants

```math
g_*=2\sqrt2-2,\quad a_\mu=4(\cosh\mu-1),\quad v_\mu=4\sinh\mu,\qquad
\mu>0,\quad a_\mu<g_*,\quad C_\mu=\frac{12}{g_*-a_\mu},\quad
D_\mu=\frac{4\sqrt2 C_\mu}{g_*}.
```

We prove, with no constant depending on $`n,T,u`$,

```math
\begin{aligned}
\|E_n b_n-b_\infty\|&\le D_\mu e^{-\mu R},\\
\|E_n\psi_n(0)-\psi_\infty(0)\|&\le\mathcal B_\mu(T,R),\\
\mathcal B_\mu(T,R)&=e^{-\mu R}
 \left[D_\mu+4C_\mu\frac{e^{v_\mu T}-1}{v_\mu}\right],\\
|A_n-A_\infty|&\le2\mathcal B_\mu(T,R).
\end{aligned}
```

Here $`A_j=\langle b_j|\mathcal U_j(T,-T)|b_j\rangle`$ and $`P_j=|A_j|^2`$.
The bounds hold throughout the stated cycle family $`0\le u<4`$. They require
only its endpoint gap, not a volume-independent minimum instantaneous gap.

## 2. Endpoint gaps and the energy-dependent normalized vectors

The rank-one resolvent equation is

```math
G_j(\eta)=\langle0|(H_{0,j}+\eta)^{-1}|0\rangle,\qquad
4G_j(\eta_j)=1,\qquad
b_j=\frac{(H_{0,j}+\eta_j)^{-1}|0\rangle}
 {\|(H_{0,j}+\eta_j)^{-1}|0\rangle\|}.
```

$`G_j`$ is strictly decreasing on $`\eta>0`$. The infinite threshold divergence
is already established in the core; on a torus the zero mode makes $`G_n`$
diverge at zero. These facts and decay at infinity give one negative eigenvalue.
There cannot be two: on vectors orthogonal to $`|0\rangle`$ the quadratic form
is that of the nonnegative free operator. The infinite endpoint operator has
spectrum nonnegative on $`b_\infty^\perp`$.

For an analytic lower bound, use the two-dimensional trial space spanned by
$`|0\rangle`$ and $`|s\rangle=\tfrac12\sum_{|x|_1=1}|x\rangle`$. Its endpoint
compression on the infinite square is

```math
\begin{pmatrix}0&-2\\-2&4\end{pmatrix},\qquad
\lambda_{\min}=2-2\sqrt2,
\qquad \eta_\infty\ge g_*.
```

This is a variational bound, not a claim that the two-dimensional space is invariant.
It removes any dependence of weight admissibility on a rounded elliptic-integral root.

To compare finite and infinite binding, write the free heat kernel as
$`e^{-4t}\sum_{k\ge0}t^k A^k/k!`$, with nonnegative nearest-neighbor path counts.
Every torus path lifts uniquely to an infinite path. Consequently

```math
\langle0|e^{-tH_{0,n}}|0\rangle
=\sum_{z\in\mathbb Z^2}\langle nz|e^{-tH_{0,\infty}}|0\rangle
\ge\langle0|e^{-tH_{0,\infty}}|0\rangle.
```

The sum and Laplace integral can be interchanged by positivity. Hence
$`G_n(\eta)\ge G_\infty(\eta)`$ and $`\eta_n\ge\eta_\infty`$.
Also $`H_{0,n}-4Q_n\ge-4I`$, so
$`g_*\le\eta_\infty\le\eta_n\le4`$. Positive heat-kernel entries fix the
positive real choices of the normalized resolvent vectors.

## 3. The same weight estimates on both geometries

Use $`d(x)=|x_1|+|x_2|`$ in centered coordinates. On the torus this equals the
shortest graph distance from the origin. A periodic edge from $`R`$ to $`-R`$
has distance difference zero, not $`2R`$. Every neighboring distance difference
has absolute value at most one.

For the infinite lattice first use the bounded invertible weight
$`W_M=e^{\mu\min(d,M)}`$. The weighted hopping coefficient on an edge is
$`-e^{\mu(d_M(x)-d_M(y))}`$. Its Hermitian and anti-Hermitian parts have the
corresponding $`-\cosh`$ and $`i\sinh`$ entries. Symmetric row/column-sum bounds give

```math
\operatorname{Re}(W_MH_0W_M^{-1})\ge-a_\mu I,\qquad
\|\operatorname{Im}(W_MH_0W_M^{-1})\|\le v_\mu.
```

For $`f_j=(H_{0,j}+\eta_j)^{-1}|0\rangle`$, take the real part of the weighted
resolvent equation to get $`\|W_M f_j\|\le(\eta_j-a_\mu)^{-1}`$.
The spectral interval gives $`\|f_j\|\ge(8+\eta_j)^{-1}\ge1/12`$.
After normalization and then monotone convergence as $`M\to\infty`$,

```math
\|e^{\mu d}b_j\|\le C_\mu.
```

The real on-site potential commutes with the weight and contributes no
anti-Hermitian part. Differentiating the squared weighted propagated norm and
using Gronwall gives, for $`-T\le t\le0`$,

```math
\|e^{\mu d}\psi_j(t)\|\le C_\mu e^{v_\mu(t+T)}.
```

The finite bounds are direct matrix estimates. On the infinite lattice the
bounded-weight proof precedes monotone convergence, avoiding an unproved use of
an unbounded similarity transform on the evolving vector. No hard propagation
front or compactly supported initial state is assumed.

## 4. The periodic seam and static state comparison

Define $`S_n=H_{0,\infty}E_n-E_nH_{0,n}`$ and let $`\chi_\partial`$ select
sites of $`\Lambda_R`$ with at least one coordinate of absolute value $`R`$.
The diagonal terms cancel. Each missing periodic hop is replaced by an outgoing
hop across the embedded square's boundary. There are at most two such hops per
boundary site and two image entries per hop. Absolute row and column sums are
at most four, including corners. Therefore

```math
S_n=S_n\chi_\partial,\qquad \|S_n\|\le4,\qquad
\|S_n z\|\le4e^{-\mu R}\|e^{\mu d}z\|.
```

This finite-rank identity is exact. A one-site collar already contains the entire
range, which is useful for tests but is not a change to the infinite geometry.
The local potential cancels as well, so the same $`S_n`$ is the generator mismatch
for every time of the declared cycle.

Let $`v_n=E_n b_n`$ and $`f_n=S_n b_n`$. The residual equation retains the
**finite** binding energy:

```math
(H_\infty(-T)+\eta_n)v_n=f_n,\qquad
\|f_n\|\le4C_\mu e^{-\mu R}.
```

Set $`P=|b_\infty\rangle\langle b_\infty|`$ and $`q=(I-P)v_n`$.
On $`P^\perp`$, $`H_\infty(-T)+\eta_n\ge\eta_n I`$, yielding
$`\|q\|\le\|f_n\|/g_*`$. Positivity makes
$`c=\langle b_\infty,v_n\rangle>0`$, so $`c=\sqrt{1-\|q\|^2}`$ and

```math
\|v_n-b_\infty\|^2=2(1-c)=\frac{2\|q\|^2}{1+c}\le2\|q\|^2.
```

This proves the first bound in Section 1, including relative phase and normalization.
It also controls the energies without assuming they coincide: the least spectral
value of $`H_\infty(-T)+\eta_n`$ is $`\eta_n-\eta_\infty\ge0`$, hence
$`0\le\eta_n-\eta_\infty\le\|f_n\|`$ for the normalized $`v_n`$.

## 5. Propagation to the midpoint and the transpose identity

The embedded finite solution has defect $`-S_n\psi_n(t)`$ in the infinite
Schrodinger equation. Duhamel's formula, unitarity, the static comparison and
Section 3 give exactly the midpoint bound $`\mathcal B_\mu(T,R)`$ in Section 1.
Only a half-cycle of length $`T`$ is propagated. The initial mismatch is added
once; it is not discarded or hidden inside a compact-support approximation.

For the return, let $`V=\mathcal U(0,-T)`$. The Hamiltonian is real symmetric
and satisfies $`H(t)=H(-t)`$. Transposing a time-ordered product reverses its
order, and the positive half-cycle has just this reversed schedule. Thus

```math
\mathcal U(T,0)=V^T,\qquad
A=b^T V^TVb=\psi(0)^T\psi(0).
```

This uses transpose, **not** adjoint. For infinite bounded operators it follows
by operator-norm convergence of the time-sliced propagators; transpose is defined
in the real site basis. The series $`\sum_x\psi_x^2`$ is absolutely convergent
because $`\sum_x|\psi_x|^2=1`$. An even but complex Hamiltonian, or a real but
non-even schedule, would not justify this particular identity.

Embedding preserves the bilinear form. For normalized $`x,y`$,
$`|x^Tx-y^Ty|\le(\|x\|+\|y\|)\|x-y\|`$. Consequently

```math
|A_n-A_\infty|\le2\mathcal B_\mu,\qquad
|P_n-P_\infty|\le4\sqrt{P_\infty}\,\mathcal B_\mu+4\mathcal B_\mu^2.
```

The second inequality retains the small amplitude: a state error $`o(1/L)`$ is
sufficient for a relative probability error $`o(1)`$ when $`P_\infty\asymp_\delta L^{-2}`$.
Using only the norm conservation $`\psi^\dagger\psi=1`$ would not measure return.

## 6. The already claimed family is sufficient, uniformly

At $`\mu=1/2`$, $`a_\mu<13/25<4/5<g_*`$. These are analytic inequalities:
$`\cosh(1/2)\le1+1/8+(1/384)/(1-1/120)<1.13`$ and
$`\sqrt2>7/5`$. Similarly,
$`\sinh(1/2)\le1/2+1/48+(1/3840)/(1-1/168)<209/400`$.
Thus no rounded numerical root is needed for either margin.

Choose exactly the preserved family

```math
R(T)=\lceil4.5T\rceil,\quad n(T)=2R(T)+1,\qquad
\gamma=\frac94-4\sinh(1/2)>\frac4{25}>0.
```

With $`K_\mu=D_\mu+4C_\mu`$ the explicit comparison obeys

```math
\mathcal B_{1/2}(T,R(T))\le K_{1/2}(1+T)e^{-\gamma T}=o(L^{-1}).
```

The exact coefficient $`\gamma\simeq0.165618778`$ is a diagnostic decimal, not
the basis of its positive sign. The side length is sufficient, not necessary or
optimized; there are $`O(T^2)`$ sites, not $`O(T)`$ sites.

Uniformity follows without introducing a new minimum-gap constant. In Gate C's
parameterization,

```math
u=\frac b{\rho_0 L},\qquad
T(L,b)=\frac{e^L}{32}\sqrt{(4-u)\rho_0 L}.
```

For $`L\ge2\pi`$ and $`0\le b\le1-\delta`$, $`u\le2`$, so $`T`$ is bounded
below by $`e^L\sqrt{2\rho_0 L}/32`$, independently of $`b`$. The exponential
volume error therefore vanishes uniformly relative to $`1/L`$. Combining with
[Gate C](UNIFORM_MINIMUM.md) gives the same normalized limit on the finite tori:

```math
\sup_{0\le b\le1-\delta}
\left|\frac{4L^2(1-b)^2}{\pi^2}
P_{n(T(L,b))}(T(L,b),u(L,b))-1\right|\longrightarrow0.
```

The relative error added by finite volume is
$`O_\delta(L\mathcal B+L^2\mathcal B^2)`$ and is negligible beside Gate C's
conservative remainder. This does not exchange fixed-volume and slow-time limits.

## 7. Tests, attribution and decision

`python tools/test_finite_volume.py --output NEW.json` supplies eight small
algebra/matrix/short-cycle diagnostics. Large finite grids used to check a static
Fourier integral are labeled quadrature, not exact infinite propagation. Nested
finite geometries test the seam/Duhamel identity, not an infinite-lattice simulation.
These diagnostics are separate from the original 272 controls and cannot prove the
uniform all-size statement by sampling.

Exponential localization is established methodology, not a discovery of this pass.
For attribution only, the primary publisher abstract and metadata of J. M. Combes
and L. Thomas, *Asymptotic behaviour of eigenfunctions for multiparticle Schrodinger
operators*, Commun. Math. Phys. **34**, 251-270 (1973),
[DOI 10.1007/BF01646473](https://doi.org/10.1007/BF01646473), were checked on
5 October 2026. Its full construction was not read or imported. All lattice weight,
seam and normalization estimates needed here are derived above; no continuum
hypothesis is silently transferred. This is not an additional experimental-precedent
record or a reopening of broad source collection.

**Decision:** Gate D has an explicit author-side route preserving the finite family
and original law. All four specified gates now have author-side expansions. A separate
critical report, exhaustive priority, and model-specific implementation remain absent.
The next step is consolidated critical assessment, not another model or an automatic
Gate E. Protected notes, saved references and the original archive remain unchanged.
