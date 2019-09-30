# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.en import English
from spacy.tokens import Doc
import pytest


@pytest.fixture(scope="session")
def en_nlp():
    return English()


@pytest.mark.parametrize("text", ["faster", "fastest", "better", "best"])
def test_en_lemmatizer_handles_irreg_adverbs(en_nlp, text):
    tokens = en_nlp(text)
    assert tokens[0].lemma_ in ["fast", "well"]


def test_issue4104(en_nlp):
    """Test that English lookup lemmatization of spun & dry are correct
    expected mapping = {'dry': 'dry', 'spun': 'spin', 'spun-dry': 'spin-dry'}
    """
    doc = Doc(en_nlp.vocab, words=["dry", "spun", "spun-dry"])
    assert [token.lemma_ for token in doc] == ["dry", "spin", "spin-dry"]
