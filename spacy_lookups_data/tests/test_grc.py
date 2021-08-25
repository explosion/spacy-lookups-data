import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("ἄνδρα", "ἀνήρ"),
        ("μοι", "ἐγώ"),
        ("ὃς", "ὅς"),
        ("πολλὰ", "πολύς"),
        ("καρδίαν", "καρδία"),
    ],
)
def test_grc_lemmatizer_lookup_assigns(grc_nlp, string, lemma):
    tokens = grc_nlp(string)
    assert tokens[0].lemma_ == lemma
