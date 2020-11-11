import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extract_bib",
    license="MIT",
    version="1.0.0",
    author="Will Barton",
    author_email="will@brtns.com",
    description=(
        "A small utility that uses BibTool to extract the references used in "
        "a Pandoc Markdown file."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/willbarton/extract_bib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "extract_bib = extract_bib:main",
        ]
    },
    extras_require={
        "testing": [
            "black",
            "check-manifest",
            "coverage",
            "flake8",
            "pytest",
        ],
    },
    test_suite="extract_bib.tests",
)
