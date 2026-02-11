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
    enforcement_stage = data.get("enforcement_stage", "unspecified")
    fail_on_gap = set(data.get("fail_on_gap", []))
    fail_on_partial = set(data.get("fail_on_partial", []))
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

    # Report
    findings_by_tool = {}
    lines = ["# Parity Report\n"]
    lines.append(f"Enforcement stage: {enforcement_stage}\n")
    lines.append(
        "Policy: "
        f"fail_on_gap={sorted(fail_on_gap)}, "
        f"fail_on_partial={sorted(fail_on_partial)}\n\n"
    )

    for tool in tools:
        gaps = gaps_by_tool[tool]
        partials = partials_by_tool[tool]
        ok = ok_by_tool[tool]

        gap_fail = len(gaps) if tool in fail_on_gap else 0
        gap_warn = len(gaps) - gap_fail
        partial_fail = len(partials) if tool in fail_on_partial else 0
        partial_warn = len(partials) - partial_fail

        tool_fail_count = gap_fail + partial_fail
        tool_warn_count = gap_warn + partial_warn
        fail_count += tool_fail_count
        warn_count += tool_warn_count

        severity = "FAIL" if tool_fail_count else ("WARN" if tool_warn_count else "OK")
        findings_by_tool[tool] = {
            "severity": severity,
            "fail_count": tool_fail_count,
            "warn_count": tool_warn_count,
            "gap": {"fail": gap_fail, "warn": gap_warn},
            "partial": {"fail": partial_fail, "warn": partial_warn},
        }

        lines.append(f"## {tool} ({severity})\n")
        lines.append(
            f"Status counts: ok={len(ok)}, partial={len(partials)}, gap={len(gaps)}\n"
        )
        lines.append(f"Findings: fail={tool_fail_count}, warn={tool_warn_count}\n")
        if partials:
            partial_label = "FAIL" if tool in fail_on_partial else "WARN"
            lines.append(f"Partial coverage ({partial_label}, {len(partials)}):\n")
            for pid in partials:
                lines.append(f"- {pid}\n")
        if gaps:
            gap_label = "FAIL" if tool in fail_on_gap else "WARN"
            lines.append(f"Gaps ({gap_label}, {len(gaps)}):\n")
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
        "enforcement_stage": enforcement_stage,
        "fail_on_gap": sorted(fail_on_gap),
        "fail_on_partial": sorted(fail_on_partial),
        "gaps_by_tool": gaps_by_tool,
        "partials_by_tool": partials_by_tool,
        "ok_by_tool": ok_by_tool,
        "findings_by_tool": findings_by_tool,
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
