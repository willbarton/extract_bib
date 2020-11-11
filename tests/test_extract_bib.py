import io
import os
from unittest import TestCase, mock
from extract_bib import main, extract_references


class TestExtractReferences(TestCase):
    @mock.patch("shutil.which")
    @mock.patch("subprocess.run")
    def test_extract_references(self, mock_run, mock_which):
        mock_which.return_value = "bibtool"

        markdown_file = io.StringIO("[@cicero:lorem]")
        extract_references(markdown_file, "test.bib", "out.bib")

        mock_run.assert_called_with(
            [
                "bibtool",
                '-X "cicero:lorem"',
                "-i",
                "test.bib",
                "-o",
                "out.bib",
            ],
            shell=True,
        )

    @mock.patch("shutil.which")
    def test_extract_references_no_bibtool(self, mock_which):
        mock_which.return_value = None

        markdown_file = io.StringIO("[@cicero:lorem]")

        with self.assertRaises(OSError):
            extract_references(markdown_file, "test.bib", "out.bib")

    @mock.patch("builtins.open", create=True)
    @mock.patch("extract_bib.extract_references")
    def test_main(self, mock_extract_references, mock_open):
        with mock.patch(
            "sys.argv",
            ["extract_bib", "--bibtex-file", "test.bib", "test.md", "out.bib"],
        ):
            main()
        mock_extract_references.assert_called_once()
