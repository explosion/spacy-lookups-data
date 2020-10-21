import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("jsem", "být"),
        ("mám", "mít"),
        ("jdu", "jít"),
        ("pána", "pán"),
    ],
)
def test_cs_lemmatizer_lookup_assigns(cs_nlp, string, lemma):
    tokens = cs_nlp(string)
    assert tokens[0].lemma_ == lemma
