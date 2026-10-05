# Limits and accuracy of the fixed return law

**5 October 2026. Author-side clarification, not a new central result.**
This note makes two implications of the existing argument precise before prose is
built around them. It leaves the Hamiltonian, observable and main asymptotic domain
in [PROOF_STATUS](PROOF_STATUS.md) unchanged.

## 1. Fixed finite size restores return uniformly in the minimum depth

Fix an odd periodic side length $`n\ge3`$. Let $`Q=|0\rangle\langle0|`$ and
$`H_n(U)=H_{0,n}-UQ`$, with eigenvalues $`E_{0,n}(U)<E_{1,n}(U)\le\cdots`$.
The ground state is simple for every $`U\in[0,4]`$: if $`A_n`$ is the
nonnegative adjacency matrix of the connected torus, then
$`5I-H_n(U)=I+A_n+UQ`$ is irreducible and nonnegative. The Perron-Frobenius
eigenvector for its largest eigenvalue is the ground vector of $`H_n(U)`$.
Continuity of the finite-matrix eigenvalues and compactness give

```math
g_n=\min_{0\le U\le4}[E_{1,n}(U)-E_{0,n}(U)]>0.
```

For $`s=t/T\in[-1,1]`$, write
$`H_{n,u}(s)=H_n(u+(4-u)s^2)`$. Uniformly for $`u\in[0,4]`$,

```math
\|\partial_s H_{n,u}\|\le8,\qquad
\|\partial_s^2 H_{n,u}\|\le8.
```

The closed interval includes the trivial constant cycle at $`u=4`$ only to make
compactness explicit. No extension of the logarithmic law to that depth is made.
Let $`\Pi(s,u)`$ be the ground projection and
$`R=(I-\Pi)(H_{n,u}-E_{0,n})^{-1}(I-\Pi)`$ the reduced resolvent. The uniform
gap and smooth finite matrix imply uniform bounds on $`\Pi',\Pi'',R,R'`$
over this compact parameter rectangle. Reuse the commutator argument in
[Gate A Section 5](AMPLITUDE_IDENTIFICATION.md):

```math
K=[\Pi',\Pi],\quad X=R\Pi'\Pi+\Pi\Pi'R,\quad [H_{n,u},X]=K,
\qquad
C_n=\sup_{0\le u\le4}\left[
\|X(-1,u)\|+\|X(1,u)\|
+\int_{-1}^{1}(\|X'\|+\|K\|\|X\|)\,ds\right]<\infty.
```

The physical propagator and the intertwining adiabatic propagator differ in norm
by at most $`C_n/T`$. Both endpoint projections are the same
$`\Pi_{4,n}=|b_{4,n}\rangle\langle b_{4,n}|`$. Hence the final leakage norm is
at most $`C_n/T`$, and unitarity gives the probability bound

```math
\boxed{\sup_{0\le u\le4}[1-P_n(T,u)]\le\frac{C_n^2}{T^2}.}
```

Thus even an arbitrary sequence $`u(T)\to0`$ restores return at **fixed** $`n`$.
This is a standard gapped-adiabatic consequence, not a failure of adiabatic theory
or a newly discovered recovery mechanism. The constants depend on $`n`$.
Indeed $`g_n\le E_{1,n}(0)-E_{0,n}(0)=4\sin^2(\pi/n)\to0`$; a gap bound
uniform in all sizes is unavailable. This argument does not apply with an
uncontrolled substitution $`n=n(T)`$. Gate D supplies that different comparison.

The corresponding infinite-lattice statement at fixed $`u>0`$ uses the gap
$`\eta(u)>0`$ throughout the cycle. Its constants depend on $`u`$ and do not
justify substituting the shrinking-depth family. This is why fixed positive depth,
fixed size, and the joint logarithmic limit give different conclusions.

For primary attribution, Jansen-Ruskai-Seiler, *Bounds for the adiabatic approximation
with applications to quantum computation*, J. Math. Phys. **48**, 102111 (2007),
[author preprint](https://arxiv.org/pdf/quant-ph/0603175), Theorem 3, Eq. (6) and
the following bound on printed pp. 4–5, gives the standard gap-dependent estimate.
Those passages were checked in parsed full text. The compact-parameter argument
above supplies the uniformity in $`u`$; a pointwise theorem alone would not.

The [2014 primary comparison](../literature/SOKOLOVSKI_PONS_MUGA_2014.md)
also supplies direct historical context: its Section VII already contrasts
finite-box Sturmian poles with the continuum threshold cut and ordinary
near-adiabatic recovery. That discussion is not our uniform-in-minimum torus
estimate, and its pole is not the next instantaneous eigenvalue. Neither generic
finite-confinement recovery nor its qualitative contrast with a continuum is a
new physical mechanism claimed here.

## 2. The controlled remainder does not resolve subleading logarithms

At zero minimum put $`\ell=\ln T`$. The exact scale definition gives

```math
L+\tfrac12\ln L=\ell+c,\qquad c=\ln(32\sqrt\pi),
\qquad
L=\ell-\tfrac12\ln\ell+c+O(\ln\ell/\ell).
```

The last relation follows by substitution into the strictly increasing left-hand
side. It is an expansion of the **scale definition**. The composed A-C estimates
only establish

```math
P_\infty(T,0)=\frac{\pi^2}{4L^2}[1+O(L^{-1/4})].
```

The relative change produced by substituting the scale expansion into $`L^{-2}`$
is of order $`\ln\ell/\ell`$, smaller than the controlled remainder
$`O(\ell^{-1/4})`$. Therefore neither the coefficient of a next-order
$`\ln\ln T/\ln T`$ term nor a constant next-order correction in the physical
probability is established. Keeping implicit $`L`$ is useful notation, not a
precision certification or a proven improvement of the asymptotic error order.
The unspecified remainder constants and onset also do not supply a finite-duration
confidence interval. The leading law alone does not prove eventual monotonicity.

## 3. The power comparator has a domain

[AUDIT Section 7](AUDIT.md) uses
$`y''+(-x-i0)^\sigma y=0`$ with $`0<\sigma<1`$. Its return expression
$`P_\sigma=4\cos^2[\pi/(2+\sigma)]`$ is quoted only on that domain.
For the local tangent in [CRITICAL_ASSESSMENT](CRITICAL_ASSESSMENT.md),

```math
\sigma_{\rm eff}=\frac1{L(1-b)}\le\frac1{\delta L}<1
\quad\text{once }L>\delta^{-1},\qquad 0\le b\le1-\delta.
```

This restores the explicit scope when the inherited comparator is restated. It
changes neither its small-power expansion nor the leading logarithmic prediction.
The energy-coordinate exponent remains distinct from a time-ramp exponent.

These clarifications use finite-matrix spectral facts, the existing commutator
estimate and elementary asymptotic algebra. No additional numerical suite, optimized
volume, crossover result or independent review is claimed.
