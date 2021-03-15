import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("летах", "лета"),
        ("рассортируют", "рассортировать"),
    ],
)
def test_lemmatizer_lookup_assigns(ru_lookup_nlp, string, lemma):
    print(string, lemma)
    tokens = ru_lookup_nlp(string)
    print([t.text for t in tokens], [t.lemma_ for t in tokens])
    assert tokens[0].lemma_ == lemma
