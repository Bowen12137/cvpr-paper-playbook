#!/usr/bin/env python3
"""Install the instruction-only skill, refusing silent overwrites."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
NAME = "cvpr-paper-playbook"


def install(dest_dir, replace=False, source=None):
    source = Path(source or ROOT / "skills" / NAME)
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source SKILL.md is missing")
    if any(p.is_symlink() for p in source.rglob("*")) or source.is_symlink():
        raise ValueError("Source must be self-contained, without symbolic links")
    dest_dir = Path(dest_dir).expanduser().resolve()
    target = dest_dir / NAME
    if target.is_symlink():
        raise ValueError("Refusing to replace a symlinked installation")
    if source.resolve() == target.resolve():
        raise ValueError("Source and destination are identical")
    if target.exists() and not target.is_dir():
        raise ValueError("Destination exists and is not a directory")
    if target.exists() and not replace:
        raise FileExistsError("Skill already exists; use --replace to back up and upgrade")
    dest_dir.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=dest_dir) as tmp:
        staged = Path(tmp) / NAME
        shutil.copytree(source, staged)
        if target.exists():
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup_root = dest_dir.parent / "skill-backups"
            backup_root.mkdir(parents=True, exist_ok=True)
            backup = backup_root / f"{NAME}-{stamp}-{uuid.uuid4().hex[:8]}"
            target.rename(backup)
        try:
            staged.rename(target)
        except OSError:
            if backup is not None:
                backup.rename(target)
            raise
    return target, backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest-dir", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--replace", action="store_true", help="Back up any old installation before replacing")
    args = parser.parse_args()
    try:
        target, backup = install(args.dest_dir, args.replace)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Install failed: {exc}\n")
    print(f"Installed: {target}")
    if backup:
        print(f"Previous version: {backup}")


if __name__ == "__main__":
    main()
