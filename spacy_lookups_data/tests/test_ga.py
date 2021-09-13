import pytest


def test_ga_lemmatizer(ga_lookup_nlp):
    tokens = ga_lookup_nlp("chonaic abacais abaraigh")
    assert tokens[0].lemma_ == "feic"
    assert tokens[1].lemma_ == "abacas"
    assert tokens[2].lemma_ == "abarach"
