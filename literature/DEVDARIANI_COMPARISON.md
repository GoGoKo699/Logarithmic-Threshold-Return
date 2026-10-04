# Devdariani comparison: the threshold, not the word logarithmic

**4 October 2026. Construction-level author-side comparison.** This closes the
specified primary-access gap in the preserved [prior-art register](PRIOR_ART.md).
It does not certify exhaustive priority or independently validate our proof.
The scientific notes and saved numerical references remain unchanged.

## Primary source and access boundary

A. Z. Devdariani, *Transitions of electrons from a bound state into the continuous
spectrum. Quadratic approximation in a model of a short-range potential*,
Theoretical and Mathematical Physics **11**, 460–469 (1972),
[DOI: 10.1007/BF01028561](https://doi.org/10.1007/BF01028561).
The [MathNet record](https://www.mathnet.ru/eng/tmf2852) supplies the original
Russian TMF **11**(2), 213–225, and its legitimate full-text download.

The Russian original was checked visually at pp. 213–221 and 224–225, including
Eqs. (1), (2), (8)–(11), (18), (20), (22), (32)–(34), and Appendix (P.5).
Pages 222–223 did not render reliably and their interpolation is not used here.
No English full-text access, complete reproduction of the paper, or permission
to redistribute its PDF is claimed. The [access record](../provenance/CONTINUATION_2026-10-04.json)
separates successful reading from failed retrievals.

The source uses a free radial half-line equation with a time-dependent Robin
condition, $`\psi_r(0,t)=f(t)\psi(0,t)`$, where
$`f(t)=-a t^2+\beta`$ and $`a>0`$. Its logarithmic derivative is boundary data,
not a logarithmic spectral singularity. Equation (18) identifies recapture with
the squared Stokes coefficient; Appendix (P.5) gives the complementary ionization
probability. Equation (8) gives $`P_i=2\cos(2\pi/5)=\sqrt{P_a}`$.
The parameter $`\lambda=\beta/a^{1/5}`$ appears in Eq. (22); negative, zero,
and positive detuning are already treated. The touching result is credited to
Devdariani–Demkov, reference [3] (1971), whose original has not been read here.

## An explicit bridge to the energy equation

The following is our reconstruction from the stated boundary problem, not a
translation of the source. Use inverse Fourier phase $`e^{-iEt}`$ and the outgoing
radial solution. Its boundary derivative divided by its value is
$`m(E)=i\sqrt{2(E+i0)}`$. If $`B(E)`$ is the boundary amplitude, multiplication
by $`-at^2`$ becomes $`a\partial_E^2`$, giving

```math
B''(E)+\frac{\beta-i\sqrt{2(E+i0)}}{a}B(E)=0.
```

On the negative-energy axis set $`E=-z^2/2`$ and
$`B(-z^2/2)=\sqrt z\,\Phi(z)`$. The chain rule gives

```math
\Phi''(z)+\left[\frac{z^3+\beta z^2}{a}
-\frac{3}{4z^2}\right]\Phi(z)=0.
```

This reproduces Eq. (11), including the sign and the inverse-square term.
It makes the comparison construction-level rather than dimensional analogy.
The letter $`z`$ replaces the old paper's spectral variable; it is not this
repository's residual attraction $`u`$. Likewise its Stokes coefficient is not
our half-cycle duration $`T`$.

For fixed negative boundary value $`f`$, direct substitution of
$`\sqrt{-2f}\,e^{fr}`$ gives $`E_b=-f^2/2`$. At touching,
$`E_b(t)=-a^2t^4/2`$. The changes of variables

```math
t=a^{-2/5}\tau,\qquad r=a^{-1/5}x,\qquad
\beta=a^{1/5}\lambda
```

remove $`a`$ from the differential equation and boundary condition. Thus slowing
this exactly scaled touching problem does not introduce a growing logarithm.
The source's probability labels imply, by elementary algebra,
$`P_a=(3-\sqrt5)/2\simeq0.381966`$, not 0.62.

## The invariant distinction in our fixed lattice problem

Our exact contact equation is instead

```math
c''(E)+\frac{-1/g(E)-u}{\alpha}c(E)=0,
\qquad \alpha=(4-u)/T^2.
```

Define the positive negative-energy threshold functions
$`W_D(E)=\sqrt{-2E}`$ and $`W_L(E)=-1/g(E)`$. For any fixed $`s>0`$,
our own threshold expansion implies

```math
\lim_{\epsilon\downarrow0}
\frac{W_D(-s\epsilon)}{W_D(-\epsilon)}=\sqrt s,
\qquad
\lim_{\epsilon\downarrow0}
\frac{W_L(-s\epsilon)}{W_L(-\epsilon)}=1.
```

The second identity follows from
$`W_L(-\epsilon)\sim[\rho_0\ln(32/\epsilon)]^{-1}`$.
A constant change of units cannot turn one ratio into the other. A nonlinear
energy change is not a shortcut either: its derivative and normalization terms
must be carried into the physical scattering problem. The inverse-square term
in the explicit bridge above illustrates precisely that obligation.

Our binding law is essential rather than polynomial. Our rescaling retains
$`L`$ and $`b=\rho_0uL`$, so a uniform proof for $`b\le1-\delta`$ is still
needed. The formal small-power tangent discussed in [AUDIT Section 7](../research/AUDIT.md)
is not such a proof. The method and the existence of threshold loss are inherited;
the spectral matching estimate is the point to test.

## Decision and remaining work

**Core preserved; attribution narrowed.** This specific construction does not
supply the logarithmic coefficient, the finite-endpoint estimate, or our
finite-periodic-volume joint law. That is a scoped comparison, not an assertion
that no predecessor could contain them. Do not advertise touching, detuning,
a scaled crossover parameter, or reflection-as-recapture as discoveries here.

The next evidence is the [separate-reader packet](../research/READER_PACKET.md)
and the unfinished [physical-premise audit](ASSUMPTIONS.md), not a new model.
The five algebra tests in `python tools/test_predecessor.py` check this bridge,
scaling, binding, probability labels and threshold ratios. They are not an
independent review or additional members of the preserved 272-control suite.
