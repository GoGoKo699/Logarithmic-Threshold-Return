# Verification and source provenance

The verification runner checks source integrity, scientific assertions and
agreement with the saved numerical references. These checks have separate records.

## Preserved inputs

[IMPORT_MAP.json](IMPORT_MAP.json) identifies all 27 protected scientific and
historical inputs by source path, byte length and SHA-256. It covers the research
notes, prior-art comparison, scientific scripts, companion model, saved results
and selected archive members. [SUITES.json](SUITES.json) is the active scientific
input registry. Verification preserves both registries and all referenced inputs.

The five scientific suites contain **28 groups and 272 controls**. Supplementary
checks and repeated executions are counted separately. Archived code is not an
execution dependency of the active suites. [Archive records](../archive/README.md)
retain the source-access records and diagnostic failures.

## Run and interpret the checks

`python verify.py --output-dir verification-artifacts` requires a fresh output
directory. It checks the protected inputs, runs the active suites, retains logs and
observed JSON, and writes complete field differences against the saved references.
The original assertions must pass and reported group/case counts must match the
registry. Timeouts, invalid outputs, changed scientific metadata or structure, and
out-of-threshold numerical changes fail the run.

The numeric regression threshold is an absolute **1e-10** plus a symmetric relative
**1e-9**. It is a regression alert, not a rigorous solver-error estimate. All raw
differences and byte-equality flags remain visible, including differences accepted
under the comparison policy. A changed benchmark requires source-level investigation;
references and thresholds must not be adjusted merely to obtain a passing run.

Only top-level environment and date fields are treated as descriptive metadata.
Integer counts, status strings and scientific parameters remain checked. Suite 07
has a narrowly scoped review of specified solver-evaluation counters under
`suite07-workload-v1`. [HOSTED_IMPORT_REVIEW.json](HOSTED_IMPORT_REVIEW.json)
records the source-derived classification and the original failed comparison.
The raw failed flags remain in each comparison; ordinary counts, changed types
and physical values remain subject to the standard checks.

Scientific assertions, agreement under the recorded policy and exact byte identity
are distinct outcomes. [INITIAL_VALIDATION.json](INITIAL_VALIDATION.json) records
the reference baseline with its execution environment. Consult the actual run's
report for its observations and comparison results.

## Hosted evidence

The [verification workflow](../.github/workflows/verify.yml) retains observed
outputs, comparisons, an environment report and the tracked source snapshot,
including on failure. Its artifacts have a finite retention period; input hashes
and validation records remain in Git. Each run identifies the revision it checked.

For the mathematical argument and its domain, use the
[proof map](../research/PROOF_STATUS.md) and
[limits and accuracy](../research/LIMITS_AND_ACCURACY.md).
