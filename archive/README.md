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
