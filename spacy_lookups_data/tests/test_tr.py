import pytest


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
