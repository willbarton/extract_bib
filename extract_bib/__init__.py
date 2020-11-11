#!/usr/bin/env python3
# Inspired by David Sanson"s extract_bib.rb script:
# https://gist.github.com/dsanson/1383132

import argparse
import os
import re
import subprocess
import shutil


def extract_references(markdown_file, bib_file, out_file):
    bibtool_path = shutil.which("bibtool")
    if bibtool_path is None:
        raise OSError(
            "Unable to find BibTool. "
            "Please ensure it is installed and in the PATH."
        )

    markdown = markdown_file.read()
    citations = re.findall("@(.*?)[\\.,;\\] ]", markdown)
    reg = " ".join(['-X "{0}"'.format(i) for i in citations])
    response = subprocess.run(
        [bibtool_path, reg, "-i", bib_file, "-o", out_file],
        shell=True,
    )
    return response


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Generate a BibTeX file containing only the entries cited in a "
            "Pandoc Markdown file."
        ),
    )
    parser.add_argument(
        "--bibtex-file",
        type=str,
        help="Path to BibTeX file containing references",
    )
    parser.add_argument(
        "file",
        type=argparse.FileType("r"),
        help="The Markdown file containing citations",
    )
    parser.add_argument(
        "out_file",
        type=str,
        help="Path to the output file for cited references",
    )
    args = parser.parse_args()

    extract_references(
        args.file,
        os.path.abspath(args.bibtex_file),
        os.path.abspath(args.out_file),
    )


if __name__ == "__main__":  # pragma: no cover
    main()
