<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# spaCy lookups data

This repository contains additional data files to be used with
[spaCy](https://spacy.io) v2.2+. When it's installed in the same environment as
spaCy, this package makes the resources for each language available as an entry
point, which spaCy checks when setting up the `Vocab` and `Lookups`.

Feel free to submit pull requests to update the data. For issues related to the
data, lookups and integration, please use the
[spaCy issue tracker](https://github.com/explosion/spaCy/issues).

[![Azure Pipelines](<https://img.shields.io/azure-devops/build/explosion-ai/public/13/master.svg?logo=azure-pipelines&style=flat-square&label=build+(3.x)>)](https://dev.azure.com/explosion-ai/public/_build?definitionId=12)
[![Travis Build Status](<https://img.shields.io/travis/explosion/spacy-lookups-data/master.svg?style=flat-square&logo=travis-ci&logoColor=white&label=build+(2.7)>)](https://travis-ci.org/explosion/spacy-lookups-data)
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
download and don't rely on third-party libraries for lemmatization – for
example, **Turkish**, **Swedish** or **Croatian**
([see data files](spacy_lookups_data/data)). You should also install it if
you're creating a **blank model** and want it to include lemmatization data.
Once you've saved out the model (e.g. via `nlp.disk`), it will include the
lookup tables as part of its `Vocab`.

### Is this package only for lemmatization?

At the moment, yes. However, we are considering including other lookup lists and
tables as well, e.g. large tokenizer exception files.

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
