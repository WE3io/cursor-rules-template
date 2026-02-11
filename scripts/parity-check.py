#!/usr/bin/env python3
"""
Parity check: Report canonical-to-tool mapping coverage.
Reads ai-blindspots/canonical-tool-mapping.json, emits report, exits non-zero on configured failures.
"""

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MAPPING_FILE = REPO_ROOT / "ai-blindspots" / "canonical-tool-mapping.json"


def main():
    if not MAPPING_FILE.exists():
        print(f"Error: {MAPPING_FILE} not found", file=sys.stderr)
        sys.exit(2)

    with open(MAPPING_FILE) as f:
        data = json.load(f)

    tools = data.get("tools", [])
    fail_on_gap = set(data.get("fail_on_gap", []))
    principles = data.get("principles", [])

    gaps_by_tool = {t: [] for t in tools}
    partials_by_tool = {t: [] for t in tools}
    ok_by_tool = {t: [] for t in tools}
    fail_count = 0
    warn_count = 0

    for p in principles:
        pid = p.get("id", "?")
        for tool in tools:
            status = p.get(tool, "gap")
            if status == "ok":
                ok_by_tool[tool].append(pid)
            elif status == "partial":
                partials_by_tool[tool].append(pid)
            else:
                gaps_by_tool[tool].append(pid)
                if tool in fail_on_gap:
                    fail_count += 1
                else:
                    warn_count += 1

    # Report
    lines = ["# Parity Report\n"]
    for tool in tools:
        gaps = gaps_by_tool[tool]
        partials = partials_by_tool[tool]
        ok = ok_by_tool[tool]
        severity = "FAIL" if tool in fail_on_gap and gaps else "WARN"
        lines.append(f"## {tool} ({severity if gaps else 'OK'})\n")
        lines.append(
            f"Status counts: ok={len(ok)}, partial={len(partials)}, gap={len(gaps)}\n"
        )
        if partials:
            lines.append(f"Partial coverage ({len(partials)}):\n")
            for pid in partials:
                lines.append(f"- {pid}\n")
        if gaps:
            lines.append(f"Gaps ({len(gaps)}):\n")
            for pid in gaps:
                lines.append(f"- {pid}\n")
        if not partials and not gaps:
            lines.append("All principles covered.\n")
        lines.append("\n")

    report = "".join(lines)
    print(report)

    # JSON output for machine parsing
    json_file = REPO_ROOT / "parity-report.json"
    json_data = {
        "gaps_by_tool": gaps_by_tool,
        "partials_by_tool": partials_by_tool,
        "ok_by_tool": ok_by_tool,
        "status_counts_by_tool": {
            tool: {
                "ok": len(ok_by_tool[tool]),
                "partial": len(partials_by_tool[tool]),
                "gap": len(gaps_by_tool[tool]),
            }
            for tool in tools
        },
        "fail_count": fail_count,
        "warn_count": warn_count,
    }
    with open(json_file, "w") as f:
        json.dump(json_data, f, indent=2)

    if fail_count > 0:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
