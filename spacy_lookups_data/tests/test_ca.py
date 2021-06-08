import pytest


def test_ca_lemmatizer(ca_lookup_nlp):
    tokens = ca_lookup_nlp("atapeïssen desaccentuéssiu úvules")
    assert tokens[0].lemma_ == "atapeir"
    assert tokens[1].lemma_ == "desaccentuar"
    assert tokens[2].lemma_ == "úvula"
