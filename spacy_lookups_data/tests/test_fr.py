import pytest


@pytest.mark.skip(reason="Lemmas not set by tokenizer exceptions in v3")
def test_fr_lemmatizer_verb(fr_lookup_nlp):
    tokens = fr_lookup_nlp("Qu'est-ce que tu fais?")
    assert tokens[0].lemma_ == "que"
    assert tokens[1].lemma_ == "être"
    assert tokens[5].lemma_ == "faire"


def test_fr_lemmatizer_noun_verb_2(fr_lookup_nlp):
    tokens = fr_lookup_nlp("Les abaissements de température sont gênants.")
    assert tokens[4].lemma_ == "être"


@pytest.mark.xfail
def test_fr_lemmatizer_noun(fr_lookup_nlp):
    tokens = fr_lookup_nlp("il y a des Costaricienne.")
    assert tokens[4].lemma_ == "Costaricain"


def test_fr_lemmatizer_noun_2(fr_lookup_nlp):
    tokens = fr_lookup_nlp("Les abaissements de température sont gênants.")
    assert tokens[1].lemma_ == "abaissement"
    assert tokens[5].lemma_ == "gênant"
