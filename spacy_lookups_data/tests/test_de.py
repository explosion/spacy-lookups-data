import pytest


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("Abgehängten", "Abgehängte"),
        ("engagierte", "engagieren"),
        ("schließt", "schließen"),
        ("vorgebenden", "vorgebend"),
        ("die", "der"),
        ("Die", "der"),
    ],
)
def test_de_lemmatizer_lookup_assigns(de_nlp, string, lemma):
    tokens = de_nlp(string)
    assert tokens[0].lemma_ == lemma


@pytest.mark.parametrize(
    "text,norms", [("vor'm", ["vor", "dem"]), ("du's", ["du", "es"])]
)
def test_de_nlp_norm_exceptions(de_nlp, text, norms):
    tokens = de_nlp(text)
    assert [token.norm_ for token in tokens] == norms


@pytest.mark.parametrize("text,norm", [("daß", "dass")])
def test_de_lex_attrs_norm_exceptions(de_nlp, text, norm):
    tokens = de_nlp(text)
    assert tokens[0].norm_ == norm
