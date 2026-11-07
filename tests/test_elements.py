"""Exercise Elements callbacks through Streamlit's component widget lifecycle.

Run inside the tutorial image after its Elements compatibility patch is applied.
AppTest cannot drive a component frontend, so submit its native widget protobuf
through the script runner, without mocking component registration or dispatch.
"""
import json
import re
import unittest

from streamlit.proto.WidgetStates_pb2 import WidgetStates
from streamlit.testing.v1 import AppTest


APP = '''
import streamlit as st
from streamlit_elements import elements, mui, editor, lazy, sync

st.session_state.setdefault("calls", [])
st.session_state.setdefault("data", "initial")

def clicked(event):
    st.session_state.calls.append((event.target.value, st.session_state.data))

with elements("callbacks"):
    editor.Monaco(onChange=lazy(sync("data")))
    mui.Button("Apply", onClick=clicked)
st.text(st.session_state.data)
st.text(str(st.session_state.calls))
'''


class ElementsTest(unittest.TestCase):
    def test_native_component_callback_dispatch(self):
        app = AppTest.from_string(APP).run()
        self.assertEqual(len(app.exception), 0)
        component = app.get("component_instance")[0].proto
        javascript = json.loads(component.json_args)["js"]
        callback_ids = sorted(set(re.findall(
            r'"(streamlit_elements\.core\.frame\.elements_frame\.callbacks\d{8})":',
            javascript,
        )))
        self.assertEqual(len(callback_ids), 2)
        self.assertIn("window.lazyData=", javascript)
        self.assertEqual(app.session_state["calls"], [])

        # A frontend Apply click submits the pending lazy editor event together
        # with the click event. Reverse payload order to check ordered dispatch.
        states = WidgetStates()
        widget = states.widgets.add()
        widget.id = component.id
        # Elements sends a JSON string as its component value; the outer JSON
        # encoding belongs to Streamlit's widget transport.
        widget.json_value = json.dumps(json.dumps({
            callback_ids[1]: {"event": {"target": {"value": "clicked"}}},
            callback_ids[0]: {"data": "edited"},
        }))
        app._run(states)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.session_state["data"], "edited")
        self.assertEqual(app.session_state["calls"], [("clicked", "edited")])

        # Repeated component values must not re-dispatch on a plain rerun.
        app._run(states)
        self.assertEqual(len(app.exception), 0)
        self.assertEqual(app.session_state["calls"], [("clicked", "edited")])


if __name__ == "__main__":
    unittest.main()
