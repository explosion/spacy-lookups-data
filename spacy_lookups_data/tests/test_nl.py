import pytest


noun_irreg_lemmatization_cases = [
    ("volkeren", "volk"),
    ("vaatje", "vat"),
    ("verboden", "verbod"),
    ("ijsje", "ijsje"),
    ("slagen", "slag"),
    ("verdragen", "verdrag"),
    ("verloven", "verlof"),
    ("gebeden", "gebed"),
    ("gaten", "gat"),
    ("staven", "staf"),
    ("aquariums", "aquarium"),
    ("podia", "podium"),
    ("holen", "hol"),
    ("lammeren", "lam"),
    ("bevelen", "bevel"),
    ("wegen", "weg"),
    ("moeilijkheden", "moeilijkheid"),
    ("aanwezigheden", "aanwezigheid"),
    ("goden", "god"),
    ("loten", "lot"),
    ("kaarsen", "kaars"),
    ("leden", "lid"),
    ("glaasje", "glas"),
    ("eieren", "ei"),
    ("vatten", "vat"),
    ("kalveren", "kalf"),
    ("padden", "pad"),
    ("smeden", "smid"),
    ("genen", "gen"),
    ("beenderen", "been"),
]


verb_irreg_lemmatization_cases = [
    ("liep", "lopen"),
    ("hief", "heffen"),
    ("begon", "beginnen"),
    ("sla", "slaan"),
    ("aangekomen", "aankomen"),
    ("sproot", "spruiten"),
    ("waart", "zijn"),
    ("snoof", "snuiven"),
    ("spoot", "spuiten"),
    ("ontbeet", "ontbijten"),
    ("gehouwen", "houwen"),
    ("afgewassen", "afwassen"),
    ("deed", "doen"),
    ("schoven", "schuiven"),
    ("gelogen", "liegen"),
    ("woog", "wegen"),
    ("gebraden", "braden"),
    ("smolten", "smelten"),
    ("riep", "roepen"),
    ("aangedaan", "aandoen"),
    ("vermeden", "vermijden"),
    ("stootten", "stoten"),
    ("ging", "gaan"),
    ("geschoren", "scheren"),
    ("gesponnen", "spinnen"),
    ("reden", "rijden"),
    ("zochten", "zoeken"),
    ("leed", "lijden"),
    ("verzonnen", "verzinnen"),
]


@pytest.mark.skip
@pytest.mark.parametrize("text,lemma", noun_irreg_lemmatization_cases)
def test_nl_lemmatizer_noun_lemmas_irreg(nl_lemmatizer, text, lemma):
    pos = "noun"
    lemmas_pred = nl_lemmatizer(text, pos)
    assert lemma == sorted(lemmas_pred)[0]


@pytest.mark.skip
@pytest.mark.parametrize("text,lemma", verb_irreg_lemmatization_cases)
def test_nl_lemmatizer_verb_lemmas_irreg(nl_lookup_nlp, text, lemma):
    pos = "verb"
    lemmas_pred = nl_lemmatizer(text, pos)
    assert lemma == sorted(lemmas_pred)[0]


# Using the lemma lookup table only
@pytest.mark.parametrize("text,lemma", noun_irreg_lemmatization_cases)
def test_nl_lemmatizer_lookup_noun(nl_lookup_nlp, text, lemma):
    doc = nl_lookup_nlp(text)
    assert doc[0].lemma_ in (lemma, text)


@pytest.mark.parametrize("text,lemma", verb_irreg_lemmatization_cases)
def test_nl_lemmatizer_lookup_verb(nl_lookup_nlp, text, lemma):
    doc = nl_lookup_nlp(text)
    assert doc[0].lemma_ in (lemma, text)
