import pytest


@pytest.mark.xfail
@pytest.mark.parametrize(
    "string,lemma",
    [
        ("DNA-profilernas", "DNA-profil"),
        ("Elfenbenskustens", "Elfenbenskusten"),
        ("abortmotståndarens", "abortmotståndare"),
        ("kolesterols", "kolesterol"),
        ("portionssnusernas", "portionssnus"),
        ("åsyns", "åsyn"),
    ],
)
def test_lemmatizer_lookup_assigns(sv_nlp, string, lemma):
    tokens = sv_nlp(string)
    assert tokens[0].lemma_ == lemma
