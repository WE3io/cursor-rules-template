#!/usr/bin/env bash
# Check backlog work items for required sections.
# Scope: backlog/active/*.md and backlog/done/*.md (excluding README.md).
# Done items must also include: **Completed:** YYYY-MM-DD

set -e

REQUIRED_SECTIONS=(
  "Outcome"
  "Constraints & References"
  "Acceptance Checks"
  "Explicit Non-Goals"
)
FAILED=0

check_file_sections() {
  local f="$1"
  local missing=()

  for section in "${REQUIRED_SECTIONS[@]}"; do
    # Allow optional section numbering in headings, e.g. "## 1. Outcome" or "## Outcome"
    if ! grep -Eq "^##[[:space:]]+([0-9]+\.[[:space:]]+)?${section}[[:space:]]*$" "$f"; then
      missing+=("$section")
    fi
  done

  if [[ ${#missing[@]} -gt 0 ]]; then
    echo "FAIL: $f missing sections: ${missing[*]}"
    FAILED=1
  fi
}

check_done_marker() {
  local f="$1"
  if ! grep -Eq "^\*\*Completed:\*\*[[:space:]]+[0-9]{4}-[0-9]{2}-[0-9]{2}" "$f"; then
    echo "FAIL: $f missing completion marker (**Completed:** YYYY-MM-DD)"
    FAILED=1
  fi
}

for f in backlog/active/*.md; do
  [[ -f "$f" ]] || continue
  [[ "$(basename "$f")" == "README.md" ]] && continue
  check_file_sections "$f"
done

for f in backlog/done/*.md; do
  [[ -f "$f" ]] || continue
  [[ "$(basename "$f")" == "README.md" ]] && continue
  check_file_sections "$f"
  check_done_marker "$f"
done

if [[ $FAILED -eq 1 ]]; then
  exit 1
fi

echo "Required sections check passed."
