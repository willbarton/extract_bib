# extract_bib

![Test](https://github.com/willbarton/extract_bib/workflows/Test/badge.svg)

A small utility that uses [BibTool](https://github.com/ge-ne/bibtool) to extract only the works cited in a Pandoc Markdown file from a BibTeX file.

If your workflow involves writing in Markdown and converting that Markdown to TeX with Pandoc, and you keep a large bibliography in a single BibTeX file, this utility will allow you to extract only the works cited in the Markdown file into a separate BibTeX file for distribution/portability.

It is intended as part of a transparent, plain text academic workflow.

It is based on [this ruby Gist](https://gist.github.com/dsanson/1383132).

## Installation

Ensure that [BibTool](https://github.com/ge-ne/bibtool) is installed.

```shell
pip install extract_bib
```

## Usage


To extract the references in `great_paper.md` that you keep in your `~/Documents/references.bib` and place them in `great_paper.bib`, run:

```shell
extract_bib --bibtex-file ~/Documents/references.bib great_paper.md great_paper.bib
```
