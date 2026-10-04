#!/usr/bin/env python3
"""Verify preserved inputs, active Markdown links and standalone threshold suites.

Observed outputs are retained in a new directory. Numeric thresholds are regression
alerts, not solver error certificates. References and archived attempts are never run
as update targets. This runner uses only the Python standard library.
"""
from __future__ import annotations
import argparse
from decimal import Decimal
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tarfile
import time
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
ATOL, RTOL = Decimal('1e-10'), Decimal('1e-9')


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode(data: bytes):
    def constant(x):
        raise ValueError(f'Nonfinite JSON constant: {x}')
    def pairs(values):
        result = {}
        for k, v in values:
            if k in result:
                raise ValueError(f'Duplicate JSON key: {k}')
            result[k] = v
        return result
    return json.loads(data, parse_constant=constant, object_pairs_hook=pairs)


def compare(a, b, path='') -> list[dict]:
    """Keep all differences; reject changed types/counts/structure by default."""
    meta = path == '/environment' or path.startswith('/environment/') or path == '/date'
    base = dict(path=path, metadata=meta)
    if any(isinstance(v, float) and not math.isfinite(v) for v in (a, b)):
        return [{**base, 'kind': 'nonfinite', 'reference': repr(a), 'observed': repr(b), 'accepted': False}]
    if type(a) is not type(b):
        return [{**base, 'kind': 'type', 'reference': a, 'observed': b, 'accepted': meta}]
    if isinstance(a, dict):
        out = []
        for k in sorted(a.keys() | b.keys()):
            p = path + '/' + k.replace('~', '~0').replace('/', '~1')
            if k not in a or k not in b:
                allowed = p in ('/environment', '/date') or p.startswith('/environment/')
                out.append(dict(path=p, metadata=allowed, kind='key', reference=a.get(k), observed=b.get(k), accepted=allowed))
            else:
                out.extend(compare(a[k], b[k], p))
        return out
    if isinstance(a, list):
        out = [] if len(a) == len(b) else [{**base, 'kind': 'length', 'reference': len(a), 'observed': len(b), 'accepted': meta}]
        for i, (x, y) in enumerate(zip(a, b)):
            out.extend(compare(x, y, path + '/' + str(i)))
        return out
    if isinstance(a, float):
        if not math.isfinite(a) or not math.isfinite(b):
            return [{**base, 'kind': 'nonfinite', 'reference': repr(a), 'observed': repr(b), 'accepted': False}]
        if a == b:
            return []
        da, db = Decimal(str(a)), Decimal(str(b))
        difference = abs(da - db)
        scale = max(abs(da), abs(db))
        return [{**base, 'kind': 'float', 'reference': a, 'observed': b,
                 'absolute_difference': str(difference),
                 'symmetric_relative_difference': str(difference / scale) if scale else '0',
                 'accepted': meta or difference <= ATOL + RTOL * scale}]
    if a == b:
        return []
    return [{**base, 'kind': 'value', 'reference': a, 'observed': b, 'accepted': meta}]



def review_workload(suite: str, differences: list[dict]) -> dict:
    """Interpret only source-inspected solver work counts, preserving raw flags.

    Suite 07 sums solve_ivp.nfev at checks.py:57 and :82 and stores that sum
    as function_evaluations. Other integers, types and scientific values are
    not exempted. This rule was added after retaining the initial CI failure.
    """
    patterns = (
        r'/groups/full_physical_band/rows/\d+/values/\d+/function_evaluations',
        r'/groups/passive_boundary_family/rows/\d+/values/\d+/function_evaluations',
        r'/groups/passive_boundary_family/independent_formulation/(vector|riccati)/function_evaluations',
        r'/groups/finite_passivity_bound/rows/\d+/terminations/\d+/function_evaluations',
    )
    workload, unresolved = [], []
    for item in differences:
        if item['accepted']:
            continue
        values = (item.get('reference'), item.get('observed'))
        is_work = (suite == '07_threshold_audit' and item['kind'] == 'value'
                   and all(type(v) is int and v >= 0 for v in values)
                   and any(re.fullmatch(pattern, item['path']) for pattern in patterns))
        if is_work:
            workload.append(dict(path=item['path'], reference=values[0], observed=values[1],
                                 role='ODE function evaluations, not a physical result or scientific case count'))
        else:
            unresolved.append(item['path'])
    return dict(policy='suite07-workload-v1', accepted=not unresolved,
                reviewed_workload=workload, unresolved=unresolved,
                scope='Explicit source-derived counter semantics; raw differences and thresholds remain unchanged')

def integrity(root: Path = ROOT) -> dict:
    mapping = decode((root / 'provenance/IMPORT_MAP.json').read_bytes())
    history = root / mapping['history_archive']['path']
    if sha(history.read_bytes()) != mapping['history_archive']['sha256']:
        raise ValueError('History archive hash mismatch')
    checked = 0
    with tarfile.open(history, 'r:xz') as archive:
        members = {m.name: m for m in archive.getmembers()}
        if len(members) != len(archive.getmembers()):
            raise ValueError('Duplicate archive member')
        for name, row in mapping['files'].items():
            p = Path(name)
            if p.is_absolute() or '..' in p.parts:
                raise ValueError('Unsafe mapped path')
            if 'archive_member' in row:
                m = members[row['archive_member']]
                if not m.isfile():
                    raise ValueError('Non-file historical member')
                stream = archive.extractfile(m)
                data = stream.read()
            else:
                data = (root / p).read_bytes()
            if sha(data) != row['sha256'] or len(data) != row['bytes']:
                raise ValueError(f'Preserved source mismatch: {name}')
            checked += 1
    registry = decode((root / 'provenance/SUITES.json').read_bytes())
    for suite in registry['suites']:
        for name, expected in suite['files'].items():
            if sha((root / 'tests' / suite['name'] / name).read_bytes()) != expected:
                raise ValueError(f'Scientific identity mismatch: {suite["name"]}/{name}')
    links = 0
    for p in sorted(root.rglob('*.md')):
        relative = p.relative_to(root)
        if any(x in {'.git', '.venv', '__pycache__', 'verification-artifacts', 'scout-history'} for x in relative.parts):
            continue
        text = p.read_text(encoding='utf-8')
        if any(ord(c) < 32 and c not in '\n\r\t' for c in text):
            raise ValueError(f'Unexpected control character: {relative}')
        if sum(bool(re.match(r'^```', line)) for line in text.splitlines()) % 2:
            raise ValueError(f'Unclosed fenced block: {relative}')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if '://' in target or target.startswith(('#', 'mailto:')):
                continue
            target = unquote(target.split('#')[0])
            resolved = (p.parent / target).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                raise ValueError(f'Unresolved local link: {relative} -> {target}')
            links += 1
    return dict(status='PASS', preserved_files=checked, local_links=links, suites=len(registry['suites']))


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--integrity-only', action='store_true')
    ap.add_argument('--output-dir', type=Path, default=ROOT / 'verification-artifacts')
    ap.add_argument('--timeout', type=float, default=1200.)
    args = ap.parse_args()
    if not math.isfinite(args.timeout) or args.timeout <= 0:
        ap.error('Timeout must be finite and positive')
    check = integrity()
    print('PASS integrity', check, flush=True)
    if args.integrity_only:
        return
    output = args.output_dir.resolve()
    if output == ROOT or ROOT.is_relative_to(output):
        ap.error('Output must not be the repository or an ancestor')
    for reserved in ('tests', 'research', 'literature', 'provenance', 'archive', 'tools', '.github', '.git'):
        if output.is_relative_to(ROOT / reserved):
            ap.error('Output must not be inside a maintained source directory')
    output.mkdir(parents=True, exist_ok=False)
    env = {**os.environ, 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1', 'PYTHONDONTWRITEBYTECODE': '1'}
    runtime = dict(python=platform.python_version(), system=platform.platform(), machine=platform.machine(),
                   threads={k: env[k] for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS')},
                   revision={k: os.environ.get(k) for k in ('GITHUB_SHA', 'GITHUB_RUN_ID')})
    (output / 'environment.json').write_text(json.dumps(runtime, indent=2) + '\n')
    registry = decode((ROOT / 'provenance/SUITES.json').read_bytes())
    rows = []
    for suite in registry['suites']:
        name = suite['name']
        folder = output / name
        folder.mkdir()
        for filename in suite['files']:
            shutil.copyfile(ROOT / 'tests' / name / filename, folder / ('reference.json' if filename == 'results.json' else filename))
        observed = folder / 'observed.json'
        start = time.monotonic()
        print('RUN', name, flush=True)
        with (folder / 'execution.log').open('w') as log:
            try:
                process = subprocess.run([sys.executable, str(ROOT / 'tests' / name / 'checks.py'), '--output', str(observed)],
                                         cwd=ROOT / 'tests' / name, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=args.timeout)
                code = process.returncode
            except subprocess.TimeoutExpired:
                code = 124
                log.write('\nRunner timeout: incomplete execution.\n')
        error = None
        differences = []
        actual = {}
        byte_equal = False
        try:
            reference = (folder / 'reference.json').read_bytes()
            raw = observed.read_bytes()
            byte_equal = raw == reference
            actual = decode(raw)
            if not isinstance(actual, dict):
                raise ValueError('Result is not an object')
            differences = compare(decode(reference), actual)
        except (ValueError, OSError, TypeError) as exc:
            actual = {}
            error = f'{type(exc).__name__}: {exc}'
        assertions = code == 0 and actual.get('status') == 'PASS'
        counts = actual.get('group_count') == suite['groups'] and actual.get('case_count', actual.get('cases')) == suite['cases']
        raw_agreement = error is None and all(d['accepted'] for d in differences)
        review = review_workload(name, differences)
        agreement = error is None and review['accepted']
        evidence = dict(error=error, byte_identical=byte_equal, absolute_threshold=str(ATOL), relative_threshold=str(RTOL),
                        agreement=agreement, raw_agreement=raw_agreement, workload_review=review,
                        differences=differences, scope='Regression comparison, not an error certificate')
        (folder / 'comparison.json').write_text(json.dumps(evidence, indent=2, allow_nan=False) + '\n')
        row = dict(name=name, status='PASS' if assertions and counts and agreement else 'FAIL', returncode=code,
                   scientific_assertions_passed=assertions, counts_match=counts, reference_agreement=agreement,
                   byte_identical=byte_equal, raw_reference_agreement=raw_agreement,
                   reviewed_workload_fields=len(review['reviewed_workload']),
                   groups=suite['groups'], cases=suite['cases'], differences=len(differences),
                   seconds=round(time.monotonic() - start, 3))
        rows.append(row)
        print(row, flush=True)
    postcheck = integrity()
    report = dict(status='PASS' if all(r['status'] == 'PASS' for r in rows) else 'FAIL',
                  suite_count=len(rows), group_count=sum(r['groups'] for r in rows), case_count=sum(r['cases'] for r in rows),
                  all_reference_bytes_identical=all(r['byte_identical'] for r in rows), before=check, after=postcheck,
                  runs=rows, scope='Author-side execution and regression checks, not independent proof review')
    (output / 'REPORT.json').write_text(json.dumps(report, indent=2, allow_nan=False) + '\n')
    print('WROTE', output / 'REPORT.json', flush=True)
    if report['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
