import pytest


def test_it_lemmatizer(it_lookup_nlp):
    tokens = it_lookup_nlp("abati inferi zurliniani")
    assert tokens[0].lemma_ == "abate"
    assert tokens[1].lemma_ == "infero"
    assert tokens[2].lemma_ == "zurliniano"
