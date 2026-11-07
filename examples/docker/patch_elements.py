"""Use Streamlit's native callback hook for the pinned Elements release.

Elements 0.1.0 patches a Streamlit module that stopped registering components
in Streamlit 1.34. Register its existing dispatcher through the public on_change
hook instead. Keep this compatibility fix inside the image, out of lesson code.
"""
from importlib.metadata import version
from importlib.util import find_spec
from pathlib import Path

assert version("streamlit") == "1.51.0"
assert version("streamlit-elements") == "0.1.0"
frame = Path(find_spec("streamlit_elements").origin).parent / "core" / "frame.py"
source = frame.read_text(encoding="utf-8")
old = 'render_component(js=javascript, key=key, default="{}")'
new = 'render_component(js=javascript, key=key, default="{}", on_change=frame._callback_manager.dispatch)'
assert source.count(old) == 1, "Recheck the Elements callback bridge before updating"
frame.write_text(source.replace(old, new), encoding="utf-8")
