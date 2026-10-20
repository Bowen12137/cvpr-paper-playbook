#!/usr/bin/env python3
"""Check this repository's constrained metadata format, links and portability.

Not a general YAML parser, external URL checker, or LLM-quality evaluator.
"""
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
NAME = "cvpr-paper-playbook"


def validate(root=ROOT):
    root = Path(root).resolve()
    errors = []
    skill = root / "skills" / NAME
    manifest = skill / "SKILL.md"
    text = manifest.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        errors.append("SKILL.md: missing frontmatter")
    else:
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(":")
            if not sep:
                errors.append("SKILL.md: metadata must use single-line scalar fields")
                continue
            value = value.strip()
            try:
                fields[key] = json.loads(value) if value.startswith('"') else value
            except ValueError:
                errors.append(f"SKILL.md: invalid quoted value for {key}")
        if fields.get("name") != NAME or not fields.get("description"):
            errors.append("SKILL.md: invalid name or description")
    ui = (skill / "agents/openai.yaml").read_text(encoding="utf-8")
    ui_fields = {}
    for line in ui.splitlines():
        if line == "interface:":
            continue
        m = re.fullmatch(r"  ([a-z_]+): (\".*\")", line)
        if not m:
            errors.append("openai.yaml: expected interface and quoted scalar fields")
            continue
        try:
            ui_fields[m[1]] = json.loads(m[2])
        except ValueError:
            errors.append("openai.yaml: invalid quoted scalar")
    if "$" + NAME not in ui_fields.get("default_prompt", ""):
        errors.append("openai.yaml: default prompt must invoke the skill")
    if not 25 <= len(ui_fields.get("short_description", "")) <= 64:
        errors.append("openai.yaml: short_description must be 25-64 characters")
    for p in root.rglob("*"):
        if any(part in {".git", "__pycache__", ".venv"} for part in p.relative_to(root).parts):
            continue
        if p.is_symlink():
            errors.append(f"{p.relative_to(root)}: symlink not portable")
        if not p.is_file() or p.suffix != ".md":
            continue
        content = p.read_text(encoding="utf-8")
        if re.search(r"/Users/[^\s/]+/|/vepfs-|root@\d", content):
            errors.append(f"{p.relative_to(root)}: private machine path")
        if "[TODO:" in content:
            errors.append(f"{p.relative_to(root)}: unfinished scaffold")
        for link in re.findall(r"\]\(([^)]+)\)", content):
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            rel = unquote(link.split("#", 1)[0]).strip("<>")
            resolved = (p.parent / rel).resolve()
            if not resolved.is_relative_to(root) or not resolved.exists():
                errors.append(f"{p.relative_to(root)}: broken/nonportable link {link}")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("Metadata, internal file links, and portability checks passed.")
