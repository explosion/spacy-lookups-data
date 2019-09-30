# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.ro import Romanian
import pytest


@pytest.fixture(scope="session")
def ro_nlp():
    return Romanian()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("câini", "câine"),
        ("expedițiilor", "expediție"),
        ("pensete", "pensetă"),
        ("erau", "fi"),
    ],
)
def test_ro_lemmatizer_lookup_assigns(ro_nlp, string, lemma):
    tokens = ro_nlp(string)
    assert tokens[0].lemma_ == lemma
