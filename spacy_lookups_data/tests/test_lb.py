# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.lb import Luxembourgish
import pytest


@pytest.fixture(scope="session")
def lb_nlp():
    return Luxembourgish()


# @pytest.mark.parametrize
@pytest.mark.xfail(
    "string,lemma",
    [
        ("Dëscher", "Dësch"),
        ("engagéiers", "engagéieren"),
        ("goung", "goen"),
        ("neit", "nei"),
        ("déi", "déi"),
        ("Männer", "Mann"),
        ("Mënner", "Mond"),
        ("kritt", "kréien"),
    ],
)
def test_lb_lemmatizer_lookup_assigns(lb_tokenizer, string, lemma):
    tokens = lb_tokenizer(string)
    assert tokens[0].lemma_ == lemma
