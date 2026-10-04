# Repository editing rules

Read WORKSPACE.md and work_orders/CURRENT.md first. Pin and inspect the actual base
revision. The owner permits modifications and merging after checks; do not force-push
over concurrent work or change unrelated repositories.

The imported research notes and tests are identified in provenance/IMPORT_MAP.json.
Keep their original bytes during organizational edits. The numerical runner must preserve
references, retain generated outputs and report all differences. A mismatch is evidence
to investigate, not a reason to refresh expected values or enlarge tolerances silently.

Run `python verify.py --integrity-only` and the applicable scientific suites. Keep raw
logs, including failures and timeouts. Do not report a completed run from an interrupted
attempt. Check the actual PR and post-merge workflows before describing their outcome.
Infrastructure tests, numerical controls and independent scientific review are distinct.

Keep active documents claim-led. Use GitHub-supported inline math and fenced math blocks;
do not place an unescaped vertical bar in a Markdown table cell. Do not invent sources,
experimental performance, email addresses, a chosen tutorial or completed priority checks.
New source claims need exact primary attribution and an honest access-depth record.

Use archive/ for obsolete attempts, not as part of the active numerical import path.
Do not include third-party PDFs, credentials, font files or unrelated scout archives.
Public narrative must not advertise a target journal or imply submission readiness.
Manuscript drafting and outside contact remain on hold.
