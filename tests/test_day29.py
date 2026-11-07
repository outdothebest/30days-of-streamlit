"""Exercise the published Day 29 example without credentials or API charges.

Run inside the provided tutorial image with the repository mounted read-only.
The live authenticated Hugging Face service is deliberately not mocked as tested.
"""
import re
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests
from streamlit.testing.v1 import AppTest

SOURCE = Path(__file__).resolve().parents[1] / "content/ko/Day29.md"
CODE = re.findall(r"```python\n(.*?)```", SOURCE.read_text(encoding="utf-8"), re.S)[0]
API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"
RESULT = [
    {"label": "refund", "score": 0.8},
    {"label": "delivery", "score": 0.15},
    {"label": "product", "score": 0.05},
]


class Day29Test(unittest.TestCase):
    def app(self, token="test-token-not-valid", labels="refund, delivery, product", text=None):
        app = AppTest.from_string(CODE).run()
        self.assertEqual(len(app.exception), 0)
        app.text_input[0].set_value(token)
        app.text_input[1].set_value(labels)
        if text is not None:
            app.text_area[0].set_value(text)
        return app

    def assert_clean(self, app):
        self.assertEqual(len(app.exception), 0)

    @patch("requests.post")
    def test_no_request_before_submit(self, post):
        app = self.app().run()
        post.assert_not_called()
        self.assert_clean(app)
        field = app.text_input[0].proto
        kind = field.DESCRIPTOR.fields_by_name["type"].enum_type
        self.assertEqual(kind.values_by_number[field.type].name, "PASSWORD")

    @patch("requests.post")
    def test_missing_token(self, post):
        app = self.app(token="").button[0].click().run()
        post.assert_not_called()
        self.assertEqual(len(app.warning), 1)
        self.assert_clean(app)

    @patch("requests.post")
    def test_invalid_input(self, post):
        for labels, text in [("refund, refund", "hello"), ("a,b", " "),
                             (",".join(map(str, range(11))), "hello")]:
            with self.subTest(labels=labels, text=text):
                app = self.app(labels=labels, text=text).button[0].click().run()
                post.assert_not_called()
                self.assertEqual(len(app.warning), 1)
                self.assert_clean(app)

    @patch("requests.post")
    def test_success_contract_and_deduplication(self, post):
        response = Mock()
        response.json.return_value = RESULT
        post.return_value = response
        app = self.app(labels=" refund, delivery, refund, product, ").button[0].click().run()
        post.assert_called_once_with(
            API_URL, headers={"Authorization": "Bearer test-token-not-valid"},
            json={"inputs": "I would like a refund for my order.",
                  "parameters": {"candidate_labels": ["refund", "delivery", "product"]}},
            timeout=30,
        )
        response.raise_for_status.assert_called_once()
        self.assert_clean(app)
        self.assertEqual(len(app.error), 0)
        self.assertEqual(app.dataframe[0].value.to_dict("records"), RESULT)
        self.assertEqual(len(app.get("arrow_vega_lite_chart")), 1)

    @patch("requests.post")
    def test_network_errors_do_not_expose_details(self, post):
        for error in [requests.Timeout("private-detail"), requests.ConnectionError("private-detail")]:
            with self.subTest(error=type(error).__name__):
                post.side_effect = error
                app = self.app().button[0].click().run()
                self.assert_clean(app)
                self.assertEqual(len(app.error), 1)
                self.assertNotIn("private-detail", app.error[0].value)
                self.assertEqual(len(app.dataframe), 0)

    @patch("requests.post")
    def test_http_errors(self, post):
        response = Mock()
        response.raise_for_status.side_effect = requests.HTTPError("private-detail")
        post.return_value = response
        app = self.app().button[0].click().run()
        self.assert_clean(app)
        self.assertEqual(len(app.error), 1)
        self.assertNotIn("private-detail", app.error[0].value)
        response.json.assert_not_called()

    @patch("requests.post")
    def test_bad_responses(self, post):
        for result in [[], {}, [RESULT[0], 1], [{"label": "refund"}],
                       [{"label": "other", "score": 0.5}],
                       [dict(row, score=2) for row in RESULT]]:
            with self.subTest(result=result):
                response = Mock()
                response.json.return_value = result
                post.return_value = response
                app = self.app().button[0].click().run()
                self.assert_clean(app)
                self.assertEqual(len(app.error), 1)
                self.assertEqual(len(app.dataframe), 0)

    @patch("requests.post")
    def test_invalid_json(self, post):
        response = Mock()
        response.json.side_effect = ValueError("private-detail")
        post.return_value = response
        app = self.app().button[0].click().run()
        self.assert_clean(app)
        self.assertEqual(len(app.error), 1)
        self.assertNotIn("private-detail", app.error[0].value)


if __name__ == "__main__":
    unittest.main()
