#!/usr/bin/env python3
"""Check the clean-folder recurring-work starter and its download."""

from __future__ import annotations

import hashlib
from pathlib import Path
import tempfile
import zipfile

from build_starter_bundle import (
    ARCHIVE,
    ARCHIVE_ROOT,
    CHECKSUM,
    SOURCE,
    archive_name,
    build_bytes,
    checksum_text,
    source_files,
)


REQUIRED_FILES = {
    "README.md",
    "WORKING_AGREEMENT.md",
    "TODAY.md",
    "SOURCE_SHELF.md",
    "REVIEW_LOG.md",
    "context/README.md",
    "outputs/README.md",
}
REQUIRED_WORKING_AGREEMENT_SECTIONS = {
    "## Purpose",
    "## Source Order",
    "## Authority",
    "## Definition of Done",
    "## Learning Rule",
}
BLOCKED_TEXT = (
    "/Users/",
    "BEGIN PRIVATE KEY",
    "sk-",
    "customer export",
    "connector payload",
)


def fail(message: str) -> None:
    raise SystemExit(f"FAIL {message}")


def check_source() -> None:
    actual = {path.relative_to(SOURCE).as_posix() for path in source_files()}
    if actual != REQUIRED_FILES:
        missing = sorted(REQUIRED_FILES - actual)
        extra = sorted(actual - REQUIRED_FILES)
        fail(f"starter files differ; missing={missing}, extra={extra}")

    working_agreement = (SOURCE / "WORKING_AGREEMENT.md").read_text(
        encoding="utf-8"
    )
    missing_sections = sorted(
        section
        for section in REQUIRED_WORKING_AGREEMENT_SECTIONS
        if section not in working_agreement
    )
    if missing_sections:
        fail("working agreement sections missing: " + ", ".join(missing_sections))

    combined = "\n".join(
        path.read_text(encoding="utf-8", errors="strict")
        for path in source_files()
    ).lower()
    findings = [text for text in BLOCKED_TEXT if text.lower() in combined]
    if findings:
        fail("public-safety text found: " + ", ".join(findings))


def check_download() -> None:
    expected_payload = build_bytes()
    try:
        actual_payload = ARCHIVE.read_bytes()
        actual_checksum = CHECKSUM.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"download missing: {exc}")

    if actual_payload != expected_payload:
        fail("download does not match the source template")
    if actual_checksum != checksum_text(expected_payload):
        fail("download checksum does not match")

    expected_names = {archive_name(path) for path in source_files()}
    with zipfile.ZipFile(ARCHIVE) as bundle:
        actual_names = set(bundle.namelist())
        if actual_names != expected_names:
            fail("archive contents differ from the source template")
        if bundle.testzip() is not None:
            fail("archive integrity check failed")
        with tempfile.TemporaryDirectory(prefix="recurring-work-starter-") as temp:
            destination = Path(temp)
            bundle.extractall(destination)
            extracted = destination / ARCHIVE_ROOT
            if not extracted.is_dir():
                fail("archive does not extract into one starter folder")
            if not (extracted / "README.md").is_file():
                fail("extracted starter has no README")

    digest = hashlib.sha256(actual_payload).hexdigest()
    if not actual_checksum.startswith(digest):
        fail("published checksum does not name the archive digest")


def main() -> int:
    check_source()
    print("PASS starter_source")
    check_download()
    print("PASS starter_archive")
    print("PASS clean_folder_shape")
    print("PASS public_safe_starter")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
