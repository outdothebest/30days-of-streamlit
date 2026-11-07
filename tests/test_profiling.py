"""Exercise the profiling lesson with the Docker image's installed packages."""
import tempfile
import unittest
from pathlib import Path

import pandas as pd
from ydata_profiling import ProfileReport


class ProfilingTest(unittest.TestCase):
    def test_html_and_file_export(self):
        report = ProfileReport(
            pd.DataFrame({"value": [1, 2, 3, 4], "label": ["a", "b", "a", "b"]}),
            progress_bar=False,
        )
        self.assertIn("<html", report.to_html().lower())
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "report.html"
            report.to_file(path)
            self.assertIn("<html", path.read_text(encoding="utf-8").lower())


if __name__ == "__main__":
    unittest.main()
