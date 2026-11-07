"""Run with python -m unittest discover -s tests in the viewer environment."""
import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest

from viewer_i18n import choose_language


class ViewerTests(unittest.TestCase):
    def test_browser_language(self):
        available = ["en", "ko", "ja"]
        self.assertEqual(choose_language(None, "fr;q=1,ko-KR;q=0.8,en;q=0.5", available), "ko")
        self.assertEqual(choose_language("ja", "ko-KR", available), "ja")
        self.assertEqual(choose_language("../ko", "ko;q=0,en;q=0.5", available), "en")
        self.assertEqual(choose_language(None, "ko;q=bad,*", available), "en")

    def test_languages_and_navigation(self):
        for language in sorted(path.name for path in Path("content").iterdir() if path.is_dir()):
            with self.subTest(language=language):
                app = AppTest.from_file("streamlit_app.py")
                app.query_params.update(language=language, challenge="Day27", extra="keep")
                app.run()
                self.assertFalse(app.exception)
                self.assertEqual(app.selectbox(key="language").value, language)
                self.assertEqual(app.selectbox(key="day").value, "Day27")
                app.selectbox(key="day").select("Day2").run()
                self.assertFalse(app.exception)
                self.assertEqual(app.query_params["challenge"], ["Day2"])
                self.assertEqual(app.query_params["extra"], ["keep"])
                app.selectbox(key="language").select("ko").run()
                self.assertFalse(app.exception)
                self.assertEqual(app.query_params["language"], ["ko"])
                self.assertEqual(app.selectbox(key="day").value, "Day2")
                self.assertTrue(any("스트림릿" in item.value or "Streamlit" in item.value for item in app.markdown))

    def test_invalid_link_and_session_isolation(self):
        app = AppTest.from_file("streamlit_app.py")
        app.query_params.update(language="../../etc", challenge="Day999")
        app.run()
        self.assertFalse(app.exception)
        self.assertEqual(app.selectbox(key="language").value, "en")
        self.assertEqual(app.selectbox(key="day").value, "Day1")
        app.selectbox(key="language").select("ko").run()
        self.assertTrue(any("30일" in item.value for item in app.markdown))
        other = AppTest.from_file("streamlit_app.py").run()
        self.assertEqual(other.selectbox(key="language").value, "en")


if __name__ == "__main__":
    unittest.main()
