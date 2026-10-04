# Current work order: challenge the leading reflection amplitude

**4 October 2026, after the physical-amplitude pass.** Work only in
`GoGoKo699/Logarithmic-Threshold-Return`. The fixed Hamiltonian, observable and
claimed law are unchanged. Manuscript drafting and outreach remain on hold.

## Gate A: what was supplied

research/AMPLITUDE_IDENTIFICATION.md supplies an author-side lemma chain for the
retarded energy solution, its no-incoming-continuum norm asymptote, equal bound-leg
normalization, exact continuum-current accounting, and the uniform O(1/T) finite-
endpoint comparison. Remote time is taken first at fixed alpha and u. Only the
subsequent tail bound needs the stated uniformity in the small-minimum family.

The reciprocal-log source lemma and the strong reconstruction are explicit new
proof passages, not consequences of passing numerical checks. A separate reader
should challenge them. Seven small new tests check algebra and finite examples;
they do not constitute independent review or new asymptotic controls. The initial
elliptic-evaluation failure and its exact arithmetic repair are preserved under
archive/GATE_A_DIAGNOSTIC_FAILURE.md. Protected proofs and references are unchanged.

## Next bounded task: reader Gate B, author-side only

Read READER_PACKET Gate B, ASYMPTOTIC Sections 4–7 and AUDIT Sections 3–5.
Reconstruct the central transfer expansion and endpoint-basis cancellation,
retaining both the principal-value and causal delta terms. Verify the sign and
coefficient of i*pi/(2L), then the exact reflection-coordinate equation and
passive far-band matching at amplitude error o(1/L). Do not replace the physical
retarded condition by a numerical absorber, and do not discard the singular core.

Produce a concise lemma chain or a concrete objection naming the affected passage.
Stop once that implication is supported at its stated order or a specific gap is
recorded. Any objection changing the leading coefficient or domain requires the
recorded approval process before editing protected files. Gates C and D are not
automatically closed by work on B. Reopen A for a concrete objection, not another
identical normalization check.

## Physical scope and independent reading

The support/mismatch map in literature/ASSUMPTIONS.md remains the implementation
boundary. Some source-count targets are unmet; exact preparation, unconditional
projector readout and a calibrated joint device remain unestablished. Broad generic
citation accumulation stays paused. New evidence must target an identified mismatch.

A genuinely separate proof report is absent. Another assistant pass is author-side
work. Do not contact readers or issue invitations without explicit instruction.
No new ramp, platform, detector, disorder, interacting system, full crossover or
optimal-size campaign is authorized. Correctness, significance and implementation
are distinct assessments; verification counts do not establish physical importance.

## Verification and retained evidence

Pin the actual base and read WORKSPACE.md, AGENTS.md and STATUS.md. Run integrity,
all existing infrastructure/algebra/operational/residual tests, the new
`python tools/test_amplitude_identification.py`, and all preserved scientific suites
in fresh output paths. Keep complete logs and failures; do not overwrite references.
Report byte equality separately from scientific assertion success. Inspect actual
PR and post-merge runs and their downloaded artifacts. The existing workload-review
policy and all 27 mapped inputs remain unchanged.

provenance/GATE_A_2026-10-04.json records this pass's base, scope and local checks.
The main claim still requires the remaining proof scrutiny, precise priority
comparison and separate reading; no manuscript or release is initiated here.
