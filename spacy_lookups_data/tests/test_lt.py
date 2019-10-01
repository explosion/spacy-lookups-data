# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.lt import Lithuanian
import pytest


@pytest.fixture(scope="session")
def lt_lemmatizer():
    lookups = Lithuanian.Defaults.create_lookups()
    return Lithuanian.Defaults.create_lemmatizer(lookups=lookups)


# fmt: off
TEST_CASES = [
    (["Galime", "vadinti", "gerovės", "valstybe", ",", "turime", "išvystytą", "socialinę", "apsaugą", ",",
      "sveikatos", "apsaugą", "ir", "prieinamą", "švietimą", "."],
     ["galėti", "vadintas", "gerovė", "valstybė", ",", "turėti", "išvystytas", "socialinis",
      "apsauga", ",", "sveikata", "apsauga", "ir", "prieinamas", "švietimas", "."]),
    (["taip", ",", "uoliai", "tyrinėjau", "ir", "pasirinkau", "geriausią", "variantą", "."],
     ["taip", ",", "uolus", "tyrinėti", "ir", "pasirinkti", "geras", "variantas", "."])
]
# fmt: on


@pytest.mark.parametrize("tokens,lemmas", TEST_CASES)
def test_lt_lemmatizer(lt_lemmatizer, tokens, lemmas):
    assert lemmas == [lt_lemmatizer.lookup(token) for token in tokens]
