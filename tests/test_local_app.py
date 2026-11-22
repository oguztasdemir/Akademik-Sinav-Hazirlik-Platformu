import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APP_DIR = ROOT / "Mobil App"


def test_mobil_app_index_exists():
    index = APP_DIR / "index.html"
    assert index.exists()
    assert "<html" in index.read_text(encoding="utf-8", errors="ignore").lower()


def test_all_js_files_valid_syntax():
    node = shutil.which("node")
    if not node:
        return
    js_files = [p for p in APP_DIR.rglob("*.js") if "node_modules" not in p.parts]
    assert js_files, "No JS files found under Mobil App/"
    for js_file in js_files:
        proc = subprocess.run([node, "--check", str(js_file)], capture_output=True, text=True)
        assert proc.returncode == 0, f"JS syntax error in {js_file.name}: {proc.stderr}"
