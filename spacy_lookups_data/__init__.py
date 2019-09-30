# coding: utf8
from __future__ import unicode_literals

from pathlib import Path

from .about import __version__  # noqa: F401

ROOT = Path(__file__).parent / "data"


hr = {"lemma_lookup": ROOT / "hr_lemma_lookup.json"}
pt = {"lemma_lookup": ROOT / "pt_lemma_lookup.json"}
sv = {
    "lemma_lookup": ROOT / "sv_lemma_lookup.json",
    "lemma_rules": ROOT / "sv_lemma_rules.json",
}
da = {"lemma_lookup": ROOT / "da_lemma_lookup.json"}
ca = {"lemma_lookup": ROOT / "ca_lemma_lookup.json"}
es = {"lemma_lookup": ROOT / "es_lemma_lookup.json"}
fr = {
    "lemma_rules": ROOT / "fr_lemma_rules.json",
    "lemma_index": ROOT / "fr_lemma_index.json",
    "lemma_exc": ROOT / "fr_lemma_exc.json",
    "lemma_lookup": ROOT / "fr_lemma_lookup.json",
}
nb = {
    "lemma_lookup": ROOT / "nb_lemma_lookup.json",
    "lemma_exc": ROOT / "nb_lemma_exc.json",
    "lemma_rules": ROOT / "nb_lemma_rules.json",
}
tr = {"lemma_lookup": ROOT / "tr_lemma_lookup.json"}
de = {"lemma_lookup": ROOT / "de_lemma_lookup.json"}
it = {"lemma_lookup": ROOT / "it_lemma_lookup.json"}
lt = {"lemma_lookup": ROOT / "lt_lemma_lookup.json"}
nl = {
    "lemma_rules": ROOT / "nl_lemma_rules.json",
    "lemma_index": ROOT / "nl_lemma_index.json",
    "lemma_exc": ROOT / "nl_lemma_exc.json",
    "lemma_lookup": ROOT / "nl_lemma_lookup.json",
}
ro = {"lemma_lookup": ROOT / "ro_lemma_lookup.json"}
sr = {"lemma_lookup": ROOT / "sr_lemma_lookup.json"}
id_ = {"lemma_lookup": ROOT / "id_lemma_lookup.json"}
hu = {"lemma_lookup": ROOT / "hu_lemma_lookup.json"}
fa = {
    "lemma_rules": ROOT / "fa_lemma_rules.json",
    "lemma_index": ROOT / "fa_lemma_index.json",
    "lemma_exc": ROOT / "fa_lemma_exc.json",
}
en = {
    "lemma_lookup": ROOT / "en_lemma_lookup.json",
    "lemma_rules": ROOT / "en_lemma_rules.json",
    "lemma_index": ROOT / "en_lemma_index.json",
    "lemma_exc": ROOT / "en_lemma_exc.json",
}
el = {
    "lemma_index": ROOT / "el_lemma_index.json",
    "lemma_exc": ROOT / "el_lemma_exc.json",
    "lemma_rules": ROOT / "el_lemma_rules.json",
}
bn = {"lemma_rules": ROOT / "bn_lemma_rules.json"}
tl = {"lemma_lookup": ROOT / "tl_lemma_lookup.json"}
ur = {"lemma_lookup": ROOT / "ur_lemma_lookup.json"}
