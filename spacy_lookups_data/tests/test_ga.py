import pytest


@pytest.mark.skip(reason="Enable after spaCy v3.2.0 release")
def test_ga_lemmatizer(ga_lookup_nlp):
    doc = Doc(ga_lookup_nlp.vocab, words=["chonaic", "abacais", "abaraigh"], pos=["VERB", "NOUN", "ADJ"])
    doc = ga_lookup_nlp.get_pipe("lemmatizer")(doc)
    assert doc[0].lemma_ == "feic"
    assert doc[1].lemma_ == "abacas"
    assert doc[2].lemma_ == "abarach"
