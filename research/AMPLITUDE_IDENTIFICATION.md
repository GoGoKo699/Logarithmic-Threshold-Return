# Gate A: reconstructing the particle from the energy equation

This note identifies energy-domain reflection with physical bound-state return
and bounds the cost of removing the auxiliary temporal tails. It gives the detailed
construction behind [ASYMPTOTIC Sections 2–3](ASYMPTOTIC.md),
[AUDIT Sections 2 and 5](AUDIT.md), and [ROUNDING Section 2](ROUNDING.md).

The energy representation and reflection interpretation are inherited from
Sokolovski–Pons [A1]. The tail comparison uses the established adiabatic commutator
method [A2]. The construction below applies these methods to the exact lattice
problem, including its logarithmic spectral singularities and the order of limits.

## 1. Statement and conventions

Let $`Q=|0\rangle\langle0|`$, $`H_0`$ be the square-lattice Laplacian with band
$`[0,8]`$, and extend the fixed parabola to all real times:

```math
H_\alpha(t)=H_0-(u+\alpha t^2)Q,\qquad
\alpha=(4-u)/T^2>0.
```

Use $`f(t)=(2\pi)^{-1}\int e^{-iEt}\widehat f(E)\,dE`$. Write
$`g(E)=\langle0|(E-H_0+i0)^{-1}|0\rangle`$ and
$`\rho(E)=-\operatorname{Im}g(E)/\pi`$ inside the band. Select the nonzero
recessive solution at positive infinity of

```math
c''+p^2c=0,\qquad p^2=\frac{-1/g-u}{\alpha}.
```

On a sufficiently negative half-line, $`p>0`$. Fix $`S'=p`$ there and define the
exact asymptotic coefficients by

```math
c(E)=p(E)^{-1/2}\{a_-e^{-iS(E)}+a_+e^{iS(E)}\}
       +O_{\alpha,u}(|E|^{-7/4}),\qquad E\to-\infty.
```

Here $`a_-`$ labels the physical **past** leg and $`a_+`$ the **future** leg;
these signs need not match a predecessor's labels after complex conjugation.
The conclusions of the chain below are

```math
P_{\rm aux}(\alpha,u)=\left|\frac{a_+}{a_-}\right|^2,\qquad
\left|\sqrt{P_\infty(T,u)}-\sqrt{P_{\rm aux}(\alpha,u)}\right|
\le \frac{C_{u_*}}{T},\quad 0\le u\le u_*<4.
```

The remote-time limits defining the auxiliary channels are taken **first, at fixed
$`\alpha,u`$**. The second bound is uniform in the displayed small-minimum family.
This avoids requiring a stationary-phase estimate uniform in two simultaneous
limits. The existing $`b=\rho_0uL\le1-\delta`$ family eventually lies in any
fixed interval $`[0,u_*]`$ with $`u_*>0`$.

## 2. A regular source, not multiplication of arbitrary distributions

Define the energy-space source

```math
q(E)=\alpha c''(E)-uc(E)=\frac{c(E)}{g(E)}.
```

The reciprocal $`1/g`$ is continuous on the real axis, with limit zero at
$`E=0,4,8`$. It is smooth elsewhere. Thus the scalar ODE has an ordinary $`C^2`$
solution across those three points; there is no extra delta source or connection
parameter at an edge. For $`E>8`$ the recessive solution decays exponentially with
an Airy-type exponent. For $`E\to-\infty`$,
$`g=E^{-1}+4E^{-2}+O(E^{-3})`$ and
$`p^2=(-E+4-u+O(E^{-1}))/\alpha`$.

The negative-tail WKB residual obeys
$`\int_{-\infty}^{-M}|\Omega/p|\,dE=O_{\alpha,u}(M^{-3/2})`$.
Variation of constants in the two WKB modes gives the coefficients above and the
integrable $`O(|E|^{-7/4})`$ amplitude remainder. This is a remote-energy statement,
not a WKB approximation through the threshold.

Choose a smooth cutoff $`\chi_-`$ supported strictly below zero and equal to one
at sufficiently negative energies. Split $`q=q_-+q_0`$, where
$`q_-=\chi_-q`$. The key property for the other part is

```math
f_0=\mathcal F^{-1}q_0\ \in L^1(\mathbb R_t).
```

Here is an explicit justification for the otherwise delicate logarithmic points.
Near each $`E_j\in\{0,4,8\}`$, on both sides of the point, the exact elliptic
resolvent and its first two derivatives give

```math
q(E_j+2^{-n}y)=A_j/n+O_{C^2_y}(n^{-2}),\qquad
1/2\le |y|\le2,
```

with the **same** leading $`A_j`$ on the two sides. At a band edge the causal
imaginary jump changes the reciprocal only at order $`n^{-2}`$; at the middle-band
singularity its imaginary logarithm also has a shared leading coefficient.
Multiplication by $`c(E)=c(E_j)+O(E-E_j)`$, with bounded first two derivatives,
preserves these estimates. The statement is local in $`E`$, at fixed $`\alpha,u`$.

For completeness, take smooth nested cutoffs $`\chi_n(x)=\chi(2^nx)`$ and
$`d_n=\chi_n-\chi_{n+1}`$. On their annuli decompose
$`q\,d_n=(A_j/n)d_n+h_n`$. The inverse Fourier $`L^1`$ norm of each rescaled
cutoff is independent of scale. The constant part telescopes into an outer cutoff
and coefficients $`A_j/n-A_j/(n-1)=O(n^{-2})`$. The rescaled $`C^2`$ bounds on
$`h_n`$ imply $`\|\mathcal F^{-1}h_n\|_1\le Cn^{-2}`$: bound its Fourier
integral directly for $`|t|\le1`$ and integrate by parts twice for $`|t|>1`$.
Both series are summable. Smooth compact pieces and the exponentially decaying
positive tail have the same integrability property. This proves the asserted
$`L^1`$ property without assuming a uniform Taylor expansion at an edge.

## 3. Retarded reconstruction and no incoming continuum

The regular-frequency contribution is the norm-convergent vector integral

```math
\Psi_0(t)=-i\int_{-\infty}^t
 e^{-iH_0(t-s)}|0\rangle f_0(s)\,ds.
```

Its remote limits follow directly from $`f_0\in L^1`$:

```math
\|\Psi_0(t)\|\longrightarrow0\quad(t\to-\infty),\qquad
\left\|\Psi_0(t)+i e^{-iH_0t}q_0(H_0)|0\rangle\right\|
\longrightarrow0\quad(t\to+\infty).
```

These are norm statements, not merely vanishing occupation at the origin.
An exponential regulator in the integral gives the resolvent
$`(E-H_0+i\eta)^{-1}`$; dominated convergence in time permits $`\eta\downarrow0`$.
In the contact matrix element, the integrable logarithmic boundary values give
$`\widehat{\langle0|\Psi_0\rangle}=gq_0`$ in distributions. This specifies the
retarded product rather than multiplying an arbitrary tempered distribution by
an undefined boundary value.

The negative-frequency part has no on-shell singularity:

```math
\Psi_-(t)=\frac1{2\pi}\int e^{-iEt}
 (E-H_0)^{-1}|0\rangle q_-(E)\,dE.
```

Use smooth oscillatory cutoffs to define the integral. At negative infinity,
$`(E-H_0)^{-1}|0\rangle/g(E)=|0\rangle+O(|E|^{-1})`$ in Hilbert norm, with
symbol derivative bounds from the convergent resolvent expansion. The difference
between this vector factor and $`|0\rangle`$, multiplied by $`c(E)`$, is
$`O(|E|^{-5/4})`$ and is norm integrable. Its inverse transform tends to zero.
The WKB remainder is likewise norm integrable. Only the two scalar oscillatory
modes therefore contribute to the leading remote bound amplitude.

Together $`\Psi=\Psi_-+\Psi_0`$ obeys
$`\langle0|\Psi\rangle=\mathcal F^{-1}c`$ and

```math
(i\partial_t-H_0)\Psi=|0\rangle\mathcal F^{-1}q
=-(u+\alpha t^2)Q\Psi.
```

The negative integral is smooth as an oscillatory integral; the regular source is
continuous and integrable. Hence this distributional solution is the ordinary
strong solution on every finite time interval, where the lattice Hamiltonian is
bounded and continuous. Norm is conserved. No completeness claim for arbitrary
incoming continuum states is required: this constructs the one channel requested
by the model. Adding a homogeneous free wave is not harmless; it would alter its
incoming condition and, after contact coupling, the scalar equation's source.

## 4. The normalization, with all Fourier factors retained

For $`E<0`$, the normalized bound vector at attraction $`-1/g(E)`$ has site weight
$`w(E)=g(E)^2/[-g'(E)]`$. Differentiating the exact energy momentum gives

```math
p|p'|=\frac{-g'}{2\alpha g^2},\qquad
\frac{1}{2\pi p|p'|}=\frac{\alpha}{\pi}\,w(E).
```

The saddle of $`\pm S(E)-Et`$ is $`t=\pm p(E)`$. The minus mode contributes at
negative times and the plus mode at positive times. The corresponding $`E_t`$
satisfies the exact instantaneous pole equation
$`1+(u+\alpha t^2)g(E_t)=0`$. Stationary phase gives a contact amplitude of modulus
$`|a_\pm|/\sqrt{2\pi p(E_t)|p'(E_t)|}`$. Relative to the instantaneous bound
orbital, **both** factors are $`\sqrt{\alpha/\pi}\,|a_\pm|`$.

One can verify the limiting stationary-phase step by rescaling
$`-E=\alpha t^2y`$: its parameter is $`\alpha|t|^3\to\infty`$ at fixed
$`\alpha`$, the saddle is nondegenerate near $`y=1`$, and the opposite mode is
nonstationary. Smooth compact remainders vanish by Fourier integrability;
negative nonstationary tails are controlled by integration by parts. The derivative
of each saddle phase is $`-E_t`$, giving the bound dynamical phase up to a constant
and the usual stationary-phase phase. Also $`b(t)\to|0\rangle`$ in norm.
Consequently the reconstructed incoming state is a pure bound channel and the
future contains its outgoing bound channel plus the free asymptote in Section 3.
The two future terms are asymptotically orthogonal: $`\rho(E)q(E)`$ is integrable
on the band, so its origin amplitude vanishes, while $`b(t)\to|0\rangle`$.

The incident coefficient cannot vanish for a nonzero recessive solution. The
following current identity also proves this and checks the normalization:

```math
j=\operatorname{Im}(\overline c\,c'),\qquad
j'=\frac{\pi}{\alpha}\rho(E)|q(E)|^2,\qquad
|a_-|^2-|a_+|^2=\frac{\pi}{\alpha}
\int_0^8\rho(E)|q(E)|^2\,dE.
```

There are no edge delta terms, and $`j(+\infty)=0`$. If $`a_-=0`$, the identity
forces both coefficients and $`q`$ on the band to vanish; ODE uniqueness then
forces $`c=0`$. Normalize $`|a_-|=\sqrt{\pi/\alpha}`$. The outgoing continuum
norm is exactly $`\int\rho|q|^2`$, so

```math
P_{\rm aux}=\frac{|a_+|^2}{|a_-|^2},\qquad
1=P_{\rm aux}+\int_0^8\rho(E)|q(E)|^2\,dE.
```

This is closed-system probability accounting. The complex coefficient in the
energy ODE is not physical dissipation. It also shows why numerical norm
conservation alone would not have established the incoming condition: Section 3,
not this identity in isolation, selected it.

## 5. Uniform removal of the gapped temporal tails

Put $`s=t/T`$ and $`U_u(s)=u+(4-u)s^2`$. On $`|s|\ge1`$ the bound energy is
isolated by at least the endpoint gap. Uniformly for $`u\in[0,u_*]`$ with
$`u_*<4`$, expanding the spectral projector of
$`H_u(s)/U_u(s)=-Q+H_0/U_u(s)`$ at $`1/U_u=0`$ gives

```math
P'=O(|s|^{-3}),\quad P''=O(|s|^{-4}),\quad
R=O(|s|^{-2}),\quad R'=O(|s|^{-3}),
```

where $`R=(1-P)(H_u-E_b)^{-1}(1-P)`$. Compact tail intervals have uniformly
positive gap and bounded derivatives. Set

```math
K=[P',P],\qquad X=RP'P+PP'R,\qquad [H_u,X]=K.
```

Then $`X=O(|s|^{-5})`$, $`X'=O(|s|^{-6})`$ and
$`\|K\|\|X\|=O(|s|^{-8})`$. Let $`U_T'=-iTH_uU_T`$ and
$`U_A'=(-iTH_u+K)U_A`$, with the same identity initial condition at $`a`$.
The adiabatic propagator intertwines $`P(a)`$ and $`P(s)`$. Differentiating
$`U_A^\dagger XU_T`$ and integrating once proves, on either oriented tail,

```math
\|U_T(b,a)-U_A(b,a)\|
\le\frac{\|X(a)\|+\|X(b)\|
+\int_a^b(\|X'\|+\|K\|\|X\|)\,ds}{T}
```

for $`b\ge a`$; reverse endpoints using unitarity. This is the finite-interval
commutator argument [A2] with its integrable tail constants displayed, not a direct
appeal to a theorem whose hypotheses only cover a compact drive.

Remote bound channels exist before taking an adiabatic limit. Choose the real
normalized $`b(s)`$ with positive origin amplitude. After removing its dynamical
phase, differentiating $`U_T(s_0,s)b(s)`$ leaves a term of norm $`\|b'(s)\|`$.
Its tail integral is finite, so the phase-adjusted channel vectors are norm-Cauchy.
The same uniform comparison can therefore be passed to the remote endpoint.
At $`s=\pm1`$ the two channel vectors differ from phase multiples of $`b_4`$ by
at most $`C/T`$. Their norms are one. Inserting them into the finite central
propagator and applying the triangle inequality gives the assertion in Section 1.
Uniqueness of a solution with the prescribed incoming norm-asymptote identifies
these channels with the reconstruction above: a difference tending to zero in
the past has conserved zero norm.

No claim that the auxiliary and finite cycles are identical at finite $`T`$ is
made. Since $`T^{-1}=o(L^{-1})`$, the comparison is small enough for the recorded
leading return amplitude. The compact-frequency argument need not itself have
constants uniform in $`\alpha`$; the remote limit precedes this uniform tail bound.

## 6. Numerical diagnostics and attribution

Sections 2–4 establish source regularity, retarded reconstruction and channel
accounting. Section 5 gives the uniform tail estimate that connects the auxiliary
reflection coefficient to the finite-cycle return probability.

`python tools/test_amplitude_identification.py --output NEW_PATH.json` checks seven
small algebra/finite examples: normalization, an exact Airy benchmark, causal
source reconstruction, lattice current accounting, reciprocal-log annuli, the tail
commutator/derivatives, and a finite tail propagator inequality. These finite
diagnostics do not prove the all-time Fourier argument or the all-$`L`$ theorem.
The [initial diagnostic failure](../archive/GATE_A_DIAGNOSTIC_FAILURE.md) and its
exact repair are retained.

### Primary attribution and reading boundary

[A1] D. Sokolovski and M. Pons, *Adiabaticity in a time dependent trap: a passage near
continuum threshold*, PRA **92**, 042121 (2015),
[author preprint](https://arxiv.org/pdf/1506.04019). Section IV, Eqs. (21)–(26), was
re-read in parsed full text and printed p. 4 was visually checked. The inherited
Sturmian/reflection construction is not claimed as new. The lattice-specific
regularity and norm reconstruction above are our argument, not attributed to A1.

[A2] J. E. Avron and A. Elgart, *Adiabatic Theorem without a Gap Condition*,
Commun. Math. Phys. **203**, 445–463 (1999),
[author full text](https://arxiv.org/html/math-ph/9805022v4). Section 4, Lemma 1 and
Eqs. (3)–(11), was re-read at passage level. Only the commutator comparison method
is used on the gapped tails; no gapless theorem is applied at the touching instant.
