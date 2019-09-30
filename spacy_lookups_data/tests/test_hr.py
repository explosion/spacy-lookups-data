# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.hr import Croatian
import pytest


@pytest.fixture(scope="session")
def hr_nlp():
    return Croatian()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("trčao", "trčati"),
        ("adekvatnim", "adekvatan"),
        ("dekontaminacijama", "dekontaminacija"),
        ("filologovih", "filologov"),
        ("je", "biti"),
        ("se", "sebe"),
    ],
)
def test_hr_lemmatizer_lookup_assigns(hr_nlp, string, lemma):
    tokens = hr_nlp(string)
    assert tokens[0].lemma_ == lemma
