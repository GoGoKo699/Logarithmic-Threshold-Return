# Preserved development history

[scout-records.tar.xz](scout-records.tar.xz) contains unchanged selected records from
threshold scouts 05–09: their source-access records and the failed residual-depth quadrature attempt.
The archive has 10 regular-file members; provenance/IMPORT_MAP.json records every
member's original source, byte length and SHA-256. No third-party paper, unrelated
research archive or parked lead is included.

The first residual-depth calculation used 600 continuum nodes per half band. It
conserved norm but failed an independent refinement test. The history preserves the
then-current checks and model, failed log, grid scan and corrected log. The active
suite 08 uses the subsequently validated grid policy. The criterion was not loosened
and the failed attempt is not counted as a passing reference.

Archive paths and old aggregate status statements are historical. To inspect them,
extract into a separate empty directory:

```sh
mkdir -p scout-history
tar -xJf archive/scout-records.tar.xz -C scout-history
```

Do not run obsolete code as part of the active suite. Its directory layout records
what was copied from development; the current scripts and canonical results are under
`tests/`. Historical validation files may name files or earlier ZIPs that are not
replicated as live repository paths. This is deliberate separation, not a claim that
those originals were deleted; the supplied aggregate conversation archives remain
unchanged and their hashes are recorded.

The five main research notes and five active scientific suites are ordinary browsable
repository files. History is not an additional prerequisite for following the result.

## Dated assessments and earlier presentation

These records retain their assessed revisions and original conclusions:

- [Critical assessment](../research/CRITICAL_ASSESSMENT.md): cross-component checks,
  the local-power comparator and its bounded significance analysis.
- [5 October sanity check](../research/SANITY_CHECK_2026-10-05.md): mathematical
  spot checks, execution evidence and documentary corrections at the recorded base.
- [Prepared reader brief](../research/READER_PACKET.md): the dated review route and
  report template.
- [Provenance](../provenance/README.md): A–D records, source-access updates,
  import preservation and hosted comparison policy.

The earlier progress-oriented [status page](https://github.com/GoGoKo699/Logarithmic-Threshold-Return/blob/b09f51a36f176b4b663ca6282185e5db7a537c7d/STATUS.md)
and [proof summary](https://github.com/GoGoKo699/Logarithmic-Threshold-Return/blob/b09f51a36f176b4b663ca6282185e5db7a537c7d/research/PROOF_STATUS.md)
are preserved at that immutable revision. The current versions organize the same
result by scope, derivation and evidence.
