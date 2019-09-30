# coding: utf-8
from __future__ import unicode_literals

from spacy.lang.tr import Turkish
import pytest


@pytest.fixture(scope="session")
def tr_nlp():
    return Turkish()


@pytest.mark.parametrize(
    "string,lemma",
    [
        ("evlerimizdeki", "ev"),
        ("işlerimizi", "iş"),
        ("biran", "biran"),
        ("bitirmeliyiz", "bitir"),
        ("isteklerimizi", "istek"),
        ("karşılaştırmamızın", "karşılaştır"),
        ("çoğulculuktan", "çoğulcu"),
    ],
)
def test_tr_lemmatizer_lookup_assigns(tr_nlp, string, lemma):
    tokens = tr_nlp(string)
    assert tokens[0].lemma_ == lemma
