# Markdown external link finder
[![CircleCI](https://circleci.com/gh/MatMoore/markdown-external-link-finder.svg?style=svg)](https://circleci.com/gh/MatMoore/markdown-external-link-finder)

This tool looks for external links in markdown files.

Currently this identifies external URLs that are linked to in a markdown file, ignoring any relative URLs.

## Installing
This tool requires Python 3.6 or later. To install with pip:

`pip install markdown-external-link-finder`

## Usage
Run `python -m markdown_external_link_finder` in the directory you want to search.

This outputs a list of URLs, one per line.

## Python API
`extract_markdown_links` takes a list of filenames and returns a list of URLs.

Example usage:

```python
from markdown_external_link_finder.extract import extract_markdown_links

for url in extract_markdown_links(['/path/to/file.md']):
    print(url)
```

## Versioning
This project follows [Semantic Versioning](https://semver.org/).

### Releasing a new version

1. Update the changelog (TODO: add the changelog)
2. Update the version in `setup.py`
3. Tag the repo with `vX.Y.Z` where X.Y.Z is the version
4. CircleCI will automatically build the package and release to PyPI

## Licence
MIT
