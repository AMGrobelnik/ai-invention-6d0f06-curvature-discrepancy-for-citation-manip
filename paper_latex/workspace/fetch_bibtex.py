#!/usr/bin/env python3
import sys
import json
import os

# Add the skill directory to path
skill_dir = "/ai-inventor/.claude/skills/aii-semscholar-bib/scripts"
sys.path.insert(0, skill_dir)

# Import the function
from aii_semscholar_bib__fetch import core_semscholar_bib_fetch

# Load references from JSON file
with open("fetch_refs.json", "r") as f:
    data = json.load(f)

# Call the function
result = core_semscholar_bib_fetch(references=data["references"])

# Print the BibTeX
if result.get("success"):
    print(result["bib_text"])
    print("\n--- STATS ---", file=sys.stderr)
    print(f"Total: {result.get('total', 0)}", file=sys.stderr)
    print(f"Found: {result.get('found', 0)}", file=sys.stderr)
    print(f"Failed: {result.get('failed_count', 0)}", file=sys.stderr)
    if result.get("failed"):
        print("\nFailed references:", file=sys.stderr)
        for f in result["failed"]:
            print(f"  - {f}", file=sys.stderr)
else:
    print("ERROR:", result.get("error", "Unknown error"), file=sys.stderr)
    sys.exit(1)
