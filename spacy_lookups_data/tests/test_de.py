# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.de import German
import pytest


@pytest.fixture(scope="session")
def de_nlp():
    return German()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("Abgehängten", "Abgehängte"),
        ("engagierte", "engagieren"),
        ("schließt", "schließen"),
        ("vorgebenden", "vorgebend"),
        ("die", "der"),
        ("Die", "der"),
    ],
)
def test_de_lemmatizer_lookup_assigns(de_nlp, string, lemma):
    tokens = de_nlp(string)
    assert tokens[0].lemma_ == lemma
