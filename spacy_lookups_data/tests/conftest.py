import spacy
import pytest


INIT_LOOKUPS_CONFIG = {
    "@misc": "spacy.LookupsDataLoader.v1",
    "lang": "${nlp.lang}",
    "tables": ["lexeme_norm"],
}


@pytest.fixture(scope="session")
def da_nlp():
    nlp = spacy.blank("da")
    nlp.config["initialize"]["lookups"] = INIT_LOOKUPS_CONFIG
    nlp.add_pipe("lemmatizer")
    nlp.initialize()
    return nlp


@pytest.fixture(scope="session")
def de_nlp():
    nlp = spacy.blank("de")
    nlp.config["initialize"]["lookups"] = INIT_LOOKUPS_CONFIG
    nlp.add_pipe("lemmatizer")
    nlp.initialize()
    return nlp


@pytest.fixture(scope="session")
def en_nlp():
    nlp = spacy.blank("en")
    nlp.config["initialize"]["lookups"] = INIT_LOOKUPS_CONFIG
    nlp.add_pipe("lemmatizer")
    nlp.initialize()
    return nlp


@pytest.fixture(scope="session")
def fr_nlp():
    nlp = spacy.blank("fr")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def hr_nlp():
    nlp = spacy.blank("hr")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def lb_nlp():
    nlp = spacy.blank("lb")
    nlp.config["initialize"]["lookups"] = INIT_LOOKUPS_CONFIG
    nlp.add_pipe("lemmatizer")
    nlp.initialize()
    return nlp


@pytest.fixture(scope="session")
def lt_nlp():
    nlp = spacy.blank("lt")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def nl_nlp():
    nlp = spacy.blank("nl")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def ro_nlp():
    nlp = spacy.blank("ro")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def sr_nlp():
    nlp = spacy.blank("sr")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def sv_nlp():
    nlp = spacy.blank("sv")
    nlp.add_pipe("lemmatizer")
    return nlp


@pytest.fixture(scope="session")
def tr_nlp():
    nlp = spacy.blank("tr")
    nlp.add_pipe("lemmatizer")
    return nlp
