# Current work order: scrutinize the finite-volume comparison

**4 October 2026, after the uniform-minimum pass.** Work only in
`GoGoKo699/Logarithmic-Threshold-Return`. The fixed Hamiltonian, observable,
coefficient and claimed domain are unchanged. Manuscript and outreach remain on hold.

## What Gate C supplied

research/UNIFORM_MINIMUM.md exposes the supremum over every 0<=b<=1-delta for fixed
delta>0. Subtracting b from both the exact coefficient and its reference wave number
leaves the central perturbation independent of b. The full integrable singular core
and its exponentially narrow forbidden region are retained, not cut out.

The passive denominator is controlled without assuming the zero-minimum sign of
Im(h). On the entire negative outer interval, W-u>=(delta/2)W, and positivity of
the two exact defect terms gives I_minus(u)<=(2/delta)^(5/2) I_minus(0), at the same
alpha and cutoff. This supplies a uniform author-side matching route and the old
coefficient pi^2/[4L^2(1-b)^2], without changing protected proof files or extending
through b=1. Seven small tests include varying-b examples but are not a proof by
sampling or additions to the original 272 controls.

## Next bounded task: Gate D

Read READER_PACKET Gate D and ROUNDING Section 6, with CORE's finite-size statement.
Reconstruct the endpoint-state comparison between the finite torus and infinite
lattice, including normalization, energy dependence and phase choice. Do not assume
that the initial vector is compactly supported or the finite and infinite states
are identical.

Check the weighted hopping estimate on each geometry, the periodic seam residual
and the time-integrated comparison. Explain why the real, even-time Hamiltonian
makes the return amplitude the midpoint bilinear psi(0)^T psi(0), not its norm.
Propagate the midpoint state error to this amplitude uniformly in the stated b
family. Verify that mu=1/2 and n(T)=2 ceil(4.5T)+1 yield o(1/L) error, including
the endpoint localization condition and all size-independent constants.

Produce a concise lemma chain or a concrete objection identifying the affected
passage. Do not optimize the lattice size, change boundaries or the cycle, solve
the residual-depth crossover, or adopt a different detector or platform. A required
coefficient/domain correction must be recorded and approved before editing protected
files. A completed author-side pass would still not be the absent separate report.

## Evidence, preservation and stopping rule

Pin current main and read WORKSPACE.md, AGENTS.md and STATUS.md. Run integrity,
all supplementary tests including tools/test_uniform_minimum.py, and all five
preserved scientific suites in fresh output paths. Keep raw failures and every
numerical difference; report byte equality separately from assertion success.
Inspect actual candidate, PR and post-merge reports, not only workflow badges.

All 27 mapped inputs, original references, and comparison/workload policy remain
unchanged. provenance/GATE_C_2026-10-04.json pins the incoming source and local
scope; later hosted outcomes require their own evidence. Other repositories and
the earlier unmerged alternate Gate B package are not imported into this work.

Broad source collection remains paused. Implementation and priority gaps remain
explicit in the support/mismatch map. No manuscript, release or outside invitation
is initiated. After the bounded proof scrutiny, consolidate rather than adding
new models to prolong development.
