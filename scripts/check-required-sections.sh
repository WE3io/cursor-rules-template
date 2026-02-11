#!/usr/bin/env bash
# Check that backlog work items have required sections: Outcome, Constraints, Acceptance Checks.
# Scope: backlog/active/*.md (excluding README.md)

set -e

REQUIRED=("1. Outcome" "2. Constraints" "3. Acceptance Checks")
FAILED=0

for f in backlog/active/*.md; do
  [[ -f "$f" ]] || continue
  [[ "$(basename "$f")" == "README.md" ]] && continue

  MISSING=()
  for section in "${REQUIRED[@]}"; do
    if ! grep -q "^## .*${section}" "$f"; then
      MISSING+=("$section")
    fi
  done

  if [[ ${#MISSING[@]} -gt 0 ]]; then
    echo "FAIL: $f missing sections: ${MISSING[*]}"
    FAILED=1
  fi
done

if [[ $FAILED -eq 1 ]]; then
  exit 1
fi

echo "Required sections check passed."
