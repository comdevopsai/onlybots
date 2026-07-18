#!/usr/bin/env python3
"""Minimal repo convention check used as a required status check on PRs.

Validates that README.md contains the expected sections. Intentionally
lightweight — this is scaffolding CI, not product testing. Fails (exit 1)
if a required section is missing so the branch-protection rule blocks merge.
"""
import sys
from pathlib import Path

REQUIRED_SECTIONS = ["# onlybots", "## License", "## Contact"]
CONTACT_LINE = "commondevops.com"

readme = Path("README.md")
if not readme.exists():
    print("FAIL: README.md not found")
    sys.exit(1)

text = readme.read_text(encoding="utf-8")

missing = [s for s in REQUIRED_SECTIONS if s not in text]
if missing:
    print(f"FAIL: missing README sections: {missing}")
    sys.exit(1)

if CONTACT_LINE not in text:
    print(f"FAIL: README Contact section does not mention {CONTACT_LINE!r}")
    sys.exit(1)

print("PASS: README conventions satisfied")
sys.exit(0)
