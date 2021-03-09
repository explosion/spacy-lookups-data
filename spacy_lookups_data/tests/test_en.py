import pytest
from spacy.tokens import Doc


@pytest.mark.parametrize("text", ["faster", "fastest", "better", "best"])
def test_en_lemmatizer_handles_irreg_adverbs(en_lookup_nlp, text):
    tokens = en_lookup_nlp(text)
    assert tokens[0].lemma_ in ["fast", "well"]


def test_issue4104(en_lookup_nlp):
    """Test that English lookup lemmatization of spun & dry are correct
    expected mapping = {'dry': 'dry', 'spun': 'spin', 'spun-dry': 'spin-dry'}
    """
    words = ["dry", "spun", "spun-dry"]
    doc = Doc(en_lookup_nlp.vocab, words=words)
    lemmatizer = en_lookup_nlp.get_pipe("lemmatizer")
    doc = lemmatizer(doc)
    assert [token.lemma_ for token in doc] == ["dry", "spin", "spin-dry"]

def test_issue7306(en_lookup_nlp):
    """Test that English lookup lemmatization of singing is sing."""
    doc = Doc(en_lookup_nlp.vocab, words=["singing"])
    lemmatizer = en_lookup_nlp.get_pipe("lemmatizer")
    doc = lemmatizer(doc)
    assert doc[0].lemma_ == "sing"


@pytest.mark.parametrize(
    "text,norms", [("I'm", ["i", "am"]), ("shan't", ["shall", "not"])]
)
def test_en_tokenizer_norm_exceptions(en_nlp, text, norms):
    tokens = en_nlp(text)
    assert [token.norm_ for token in tokens] == norms
