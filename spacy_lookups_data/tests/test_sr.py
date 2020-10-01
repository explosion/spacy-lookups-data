import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("најадекватнији", "адекватан"),
        ("матурирао", "матурирати"),
        ("планираћемо", "планирати"),
        ("певају", "певати"),
        ("нама", "ми"),
        ("се", "себе"),
    ],
)
def test_sr_lemmatizer_lookup_assigns(sr_nlp, string, lemma):
    tokens = sr_nlp(string)
    assert tokens[0].lemma_ == lemma
