import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.dest = self.root / "user" / "skills"

    def tearDown(self):
        self.temp.cleanup()

    def test_fresh_install_has_complete_skill(self):
        target, backup = installer.install(self.dest)
        self.assertIsNone(backup)
        source = ROOT / "skills" / installer.NAME
        originals = {str(p.relative_to(source)): p.read_bytes() for p in source.rglob("*") if p.is_file()}
        copies = {str(p.relative_to(target)): p.read_bytes() for p in target.rglob("*") if p.is_file()}
        self.assertEqual(originals, copies)

    def test_existing_user_edits_are_preserved_on_refusal(self):
        target, _ = installer.install(self.dest)
        (target / "SKILL.md").write_text("user edits", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            installer.install(self.dest)
        self.assertEqual((target / "SKILL.md").read_text(), "user edits")

    def test_upgrade_backs_up_outside_discovery_folder(self):
        target, _ = installer.install(self.dest)
        (target / "local-note.txt").write_text("keep", encoding="utf-8")
        target, backup = installer.install(self.dest, replace=True)
        self.assertFalse(backup.is_relative_to(self.dest))
        self.assertEqual((backup / "local-note.txt").read_text(), "keep")
        self.assertFalse((target / "local-note.txt").exists())
        self.assertTrue((target / "references/review.md").is_file())

    def test_symlink_target_is_not_overwritten(self):
        self.dest.mkdir(parents=True)
        external = self.root / "external"
        external.mkdir()
        (self.dest / installer.NAME).symlink_to(external, target_is_directory=True)
        with self.assertRaises(ValueError):
            installer.install(self.dest, replace=True)
        self.assertTrue((self.dest / installer.NAME).is_symlink())

    def test_failed_publication_restores_previous_version(self):
        target, _ = installer.install(self.dest)
        (target / "SKILL.md").write_text("previous", encoding="utf-8")
        original_rename = Path.rename

        def fail_staged(path, dst):
            if path.parent.name.startswith(".skill-install-"):
                raise OSError("injected rename failure")
            return original_rename(path, dst)

        with patch.object(Path, "rename", fail_staged):
            with self.assertRaises(OSError):
                installer.install(self.dest, replace=True)
        self.assertEqual((target / "SKILL.md").read_text(), "previous")


if __name__ == "__main__":
    unittest.main()
