import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("câini", "câine"),
        ("expedițiilor", "expediție"),
        ("pensete", "pensetă"),
        ("erau", "fi"),
    ],
)
def test_ro_lemmatizer_lookup_assigns(ro_nlp, string, lemma):
    tokens = ro_nlp(string)
    assert tokens[0].lemma_ == lemma
