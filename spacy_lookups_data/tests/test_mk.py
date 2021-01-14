# coding: utf-8
from __future__ import unicode_literals

import pytest


@pytest.mark.parametrize("text", ["побрзо", "најбрзо", "подобро", "најдобро"])
def test_mk_lemmatizer_handles_irreg_adverbs(mk_lookup_nlp, text):
    for token in mk_lookup_nlp(text):
        assert token.lemma_ in ["брзо", "добро"]


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("најадекватен", "адекватен"),
        ("моите", "мое"),
        ("читавме", "чита"),
        ("изеде", "јаде"),
        ("изоди", "оди"),
        ("мислеше", "мисли")
    ],
)
def test_mk_lemmatizer_lookup_assigns(mk_lookup_nlp, string, lemma):
    assert mk_lookup_nlp(string)[0].lemma_ == lemma


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("Еј здр, как си? Јави се на мојот моб, бројот почиња со кец. Можит да дојдам со кола, позз.",
         ["еј", "здраво", ",", "како", "си", "?", "јави", "се", "на", "мојот", "мобилен", ",", "бројот", "започнува",
          "со", "единица", ".", "Може", "да", "дојдам", "со", "автомобил", ",", "поздрав", "."])
    ]
)
def test_mk_tokenizer_norm_exceptions(mk_lookup_nlp, string, lemma):
    assert [token.norm_ for token in mk_lookup_nlp(string)] == lemma
