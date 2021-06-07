import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("летах", "лета"),
        ("рассортируют", "рассортировать"),
    ],
)
def test_lemmatizer_lookup_assigns(ru_lookup_nlp, string, lemma):
    tokens = ru_lookup_nlp(string)
    assert tokens[0].lemma_ == lemma
