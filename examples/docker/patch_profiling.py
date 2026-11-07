"""Read package versions without pkg_resources in the pinned profiling release."""
from importlib.metadata import version
from importlib.util import find_spec
from pathlib import Path

assert version("ydata-profiling") == "4.12.2"
report = Path(find_spec("ydata_profiling").origin).parent / "profile_report.py"
source = report.read_text(encoding="utf-8")
replacements = {
    "    import pkg_resources": "    from importlib.metadata import version",
    'pkg_resources.get_distribution("Pillow").version': 'version("Pillow")',
}
for old, new in replacements.items():
    assert source.count(old) == 1, "Recheck the profiling compatibility patch before updating"
    source = source.replace(old, new)
report.write_text(source, encoding="utf-8")
