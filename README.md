<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# spaCy lookups data

This repository contains additional data files to be used with
[spaCy](https://spacy.io) v2.2+. When it's installed in the same environment as
spaCy, this package makes the resources for each language available as an entry
point, which spaCy checks when setting up the `Vocab` and `Lookups`.

Feel free to submit pull requests to update the data. For issues related to the
data, lookups and integration, please use the
[spaCy issue tracker](https://github.com/explosion/spaCy/issues).

[![tests](https://github.com/explosion/spacy-lookups-data/actions/workflows/tests.yml/badge.svg)](https://github.com/explosion/spacy-lookups-data/actions/workflows/tests.yml)
[![Current Release Version](https://img.shields.io/github/release/explosion/spacy-lookups-data.svg?include_prereleases&style=flat-square&logo=github)](https://github.com/explosion/spacy-lookups-data/releases)
[![pypi Version](https://img.shields.io/pypi/v/spacy-lookups-data.svg?style=flat-square&logo=pypi&logoColor=white)](https://pypi.org/project/spacy-lookups-data/)
[![conda Version](https://img.shields.io/conda/vn/conda-forge/spacy-lookups-data.svg?style=flat-square&logo=conda-forge&logoColor=white)](https://anaconda.org/conda-forge/spacy-lookups-data)

## FAQ

### Why does this exist?

The main purpose of this package is to make the default spaCy installation
smaller and not force every user to download large data files for _all_
languages by default. Lookups data is now either provided **via the pre-trained
models** (which serialize out their vocabulary and lookup tables) or by
**explicitly installing this package** or `spacy[lookups]`.

### When should I install this?

You should install this package if you want to use lemmatization for languages
that don't yet have a [pretrained model](https://spacy.io/models) available for
download and don't rely on third-party libraries for lemmatization – for example
for **Serbian** or **Turkish** ([see data files](spacy_lookups_data/data)).

If you are training new models with spaCy, you should probably install this,
since it contains lemmatization and normalization data for 25+ languages that is
no longer included as part of the main spaCy library. In particular, you should
install it if you're creating a **blank model** and you want it to include
lemmatization and normalization data. Once you've saved out the model (e.g. via
`nlp.to_disk`), it will include the lookup tables as part of its `Vocab`.

### Is this package only for lemmatization?

This package used to only be for lemmatization, but it has been extended to
include normalization data for many languages. As of v0.3.1 it also includes
optional probability and Brown cluster data that used to be distributed with
provided models in spaCy v2.2 but is no longer included in spaCy v2.3. In the
future it may include other lookup lists and tables as well, e.g. large
tokenizer exception files.

## Running tests

This package now also includes all
[data-specific tests](spacy_lookups_data/tests). The test suite depends on
spaCy.

```bash
pip install -r requirements.txt
python -m pytest spacy_lookups_data
```

If you've installed the package in your spaCy environment, you can also run the
tests like this:

```bash
python -m pytest --pyargs spacy_lookups_data
```

## Bug reports and other issues

Please use [spaCy's issue tracker](https://github.com/explosion/spaCy/issues) to
report a bug, or open a new thread on the
[discussion board](https://github.com/explosion/spaCy/discussions) for any other
issue.
