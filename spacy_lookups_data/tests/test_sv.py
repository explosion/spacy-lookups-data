# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.sv import Swedish
import pytest


@pytest.fixture(scope="session")
def sv_nlp():
    return Swedish()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("DNA-profilernas", "DNA-profil"),
        ("Elfenbenskustens", "Elfenbenskusten"),
        ("abortmotståndarens", "abortmotståndare"),
        ("kolesterols", "kolesterol"),
        ("portionssnusernas", "portionssnus"),
        ("åsyns", "åsyn"),
    ],
)
def test_lemmatizer_lookup_assigns(sv_nlp, string, lemma):
    tokens = sv_nlp(string)
    assert tokens[0].lemma_ == lemma
