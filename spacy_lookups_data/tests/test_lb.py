# coding: utf-8
from __future__ import unicode_literals

import pytest


@pytest.fixture(scope="session")
def lb_nlp():
    # TODO: move to top of file once Luxembourgish is shipped with spaCy
    from spacy.lang.lb import Luxembourgish

    return Luxembourgish()


@pytest.mark.xfail
@pytest.mark.parametrize(
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
def test_lb_lemmatizer_lookup_assigns(lb_nlp, string, lemma):
    tokens = lb_nlp(string)
    assert tokens[0].lemma_ == lemma
