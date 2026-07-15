#!/usr/bin/env python3
"""Build the deterministic minimum recurring-workspace download."""

from __future__ import annotations

import argparse
import hashlib
import io
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "templates" / "recurring-workspace"
DOWNLOADS = ROOT / "downloads"
ARCHIVE = DOWNLOADS / "minimum-recurring-workspace.zip"
CHECKSUM = DOWNLOADS / "minimum-recurring-workspace.sha256"
ARCHIVE_ROOT = "minimum-recurring-workspace"
ZIP_TIMESTAMP = (2020, 1, 1, 0, 0, 0)


def source_files() -> list[Path]:
    return sorted(path for path in SOURCE.rglob("*") if path.is_file())


def archive_name(path: Path) -> str:
    return f"{ARCHIVE_ROOT}/{path.relative_to(SOURCE).as_posix()}"


def build_bytes() -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(
        buffer,
        mode="w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as bundle:
        for path in source_files():
            info = zipfile.ZipInfo(archive_name(path), ZIP_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            bundle.writestr(info, path.read_bytes())
    return buffer.getvalue()


def checksum_text(payload: bytes) -> str:
    digest = hashlib.sha256(payload).hexdigest()
    return f"{digest}  {ARCHIVE.name}\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the committed archive or checksum is out of date",
    )
    args = parser.parse_args()

    payload = build_bytes()
    checksum = checksum_text(payload)
    if args.check:
        try:
            actual_payload = ARCHIVE.read_bytes()
            actual_checksum = CHECKSUM.read_text(encoding="utf-8")
        except OSError as exc:
            raise SystemExit(f"FAIL starter bundle missing: {exc}") from exc
        if actual_payload != payload:
            raise SystemExit("FAIL starter bundle is out of date")
        if actual_checksum != checksum:
            raise SystemExit("FAIL starter checksum is out of date")
        print("PASS deterministic_starter_bundle")
        return 0

    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    ARCHIVE.write_bytes(payload)
    CHECKSUM.write_text(checksum, encoding="utf-8")
    print(f"WROTE {ARCHIVE.relative_to(ROOT)}")
    print(f"WROTE {CHECKSUM.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
