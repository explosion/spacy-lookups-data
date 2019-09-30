# coding: utf8
from __future__ import unicode_literals

import pkg_resources
import os

from .about import __version__  # noqa: F401


def get_file(filename):
    return pkg_resources.resource_filename(__name__, os.path.join("data", filename))


hr = {"lemma_lookup": get_file("hr_lemma_lookup.json")}
pt = {"lemma_lookup": get_file("pt_lemma_lookup.json")}
sv = {
    "lemma_lookup": get_file("sv_lemma_lookup.json"),
    "lemma_rules": get_file("sv_lemma_rules.json"),
}
da = {"lemma_lookup": get_file("da_lemma_lookup.json")}
ca = {"lemma_lookup": get_file("ca_lemma_lookup.json")}
es = {"lemma_lookup": get_file("es_lemma_lookup.json")}
fr = {
    "lemma_rules": get_file("fr_lemma_rules.json"),
    "lemma_index": get_file("fr_lemma_index.json"),
    "lemma_exc": get_file("fr_lemma_exc.json"),
    "lemma_lookup": get_file("fr_lemma_lookup.json"),
}
nb = {
    "lemma_lookup": get_file("nb_lemma_lookup.json"),
    "lemma_exc": get_file("nb_lemma_exc.json"),
    "lemma_rules": get_file("nb_lemma_rules.json"),
}
tr = {"lemma_lookup": get_file("tr_lemma_lookup.json")}
de = {"lemma_lookup": get_file("de_lemma_lookup.json")}
it = {"lemma_lookup": get_file("it_lemma_lookup.json")}
lt = {"lemma_lookup": get_file("lt_lemma_lookup.json")}
nl = {
    "lemma_rules": get_file("nl_lemma_rules.json"),
    "lemma_index": get_file("nl_lemma_index.json"),
    "lemma_exc": get_file("nl_lemma_exc.json"),
    "lemma_lookup": get_file("nl_lemma_lookup.json"),
}
ro = {"lemma_lookup": get_file("ro_lemma_lookup.json")}
sr = {"lemma_lookup": get_file("sr_lemma_lookup.json")}
id_ = {"lemma_lookup": get_file("id_lemma_lookup.json")}
hu = {"lemma_lookup": get_file("hu_lemma_lookup.json")}
fa = {
    "lemma_rules": get_file("fa_lemma_rules.json"),
    "lemma_index": get_file("fa_lemma_index.json"),
    "lemma_exc": get_file("fa_lemma_exc.json"),
}
en = {
    "lemma_lookup": get_file("en_lemma_lookup.json"),
    "lemma_rules": get_file("en_lemma_rules.json"),
    "lemma_index": get_file("en_lemma_index.json"),
    "lemma_exc": get_file("en_lemma_exc.json"),
}
el = {
    "lemma_index": get_file("el_lemma_index.json"),
    "lemma_exc": get_file("el_lemma_exc.json"),
    "lemma_rules": get_file("el_lemma_rules.json"),
}
bn = {"lemma_rules": get_file("bn_lemma_rules.json")}
tl = {"lemma_lookup": get_file("tl_lemma_lookup.json")}
ur = {"lemma_lookup": get_file("ur_lemma_lookup.json")}
