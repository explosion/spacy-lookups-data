# coding: utf8
from __future__ import unicode_literals

import pkg_resources
import os

from .about import __version__  # noqa: F401


def get_file(filename):
    return pkg_resources.resource_filename(__name__, os.path.join("data", filename))


hr = {"lemma_lookup": get_file("hr_lemma_lookup.json")}
hr_lookups = lambda: hr
pt = {
    "lemma_lookup": get_file("pt_lemma_lookup.json"),
    "lexeme_norm": get_file("pt_lexeme_norm.json"),
}
pt_lookups = lambda: pt
sv = {
    "lemma_lookup": get_file("sv_lemma_lookup.json"),
    "lemma_rules": get_file("sv_lemma_rules.json"),
}
sv_lookups = lambda: sv
da = {
    "lemma_lookup": get_file("da_lemma_lookup.json"),
    "lexeme_norm": get_file("da_lexeme_norm.json"),
}
da_lookups = lambda: da
ca = {"lemma_lookup": get_file("ca_lemma_lookup.json")}
ca_lookups = lambda: ca
es = {"lemma_lookup": get_file("es_lemma_lookup.json")}
es_lookups = lambda: es
fr = {
    "lemma_rules": get_file("fr_lemma_rules.json"),
    "lemma_index": get_file("fr_lemma_index.json"),
    "lemma_exc": get_file("fr_lemma_exc.json"),
    "lemma_lookup": get_file("fr_lemma_lookup.json"),
}
fr_lookups = lambda: fr
nb = {
    "lemma_lookup": get_file("nb_lemma_lookup.json"),
    "lemma_exc": get_file("nb_lemma_exc.json"),
    "lemma_rules": get_file("nb_lemma_rules.json"),
}
nb_lookups = lambda: nb
tr = {"lemma_lookup": get_file("tr_lemma_lookup.json")}
tr_lookups = lambda: tr
de = {
    "lemma_lookup": get_file("de_lemma_lookup.json"),
    "lexeme_norm": get_file("de_lexeme_norm.json"),
}
de_lookups = lambda: de
it = {"lemma_lookup": get_file("it_lemma_lookup.json")}
it_lookups = lambda: it
lt = {"lemma_lookup": get_file("lt_lemma_lookup.json")}
lt_lookups = lambda: lt
nl = {
    "lemma_rules": get_file("nl_lemma_rules.json"),
    "lemma_index": get_file("nl_lemma_index.json"),
    "lemma_exc": get_file("nl_lemma_exc.json"),
    "lemma_lookup": get_file("nl_lemma_lookup.json"),
}
nl_lookups = lambda: nl
ro = {"lemma_lookup": get_file("ro_lemma_lookup.json")}
ro_lookups = lambda: ro
sr = {
    "lemma_lookup": get_file("sr_lemma_lookup.json"),
    "lexeme_norm": get_file("sr_lexeme_norm.json"),
}
sr_lookups = lambda: sr
id_ = {
    "lemma_lookup": get_file("id_lemma_lookup.json"),
    "lexeme_norm": get_file("id_lexeme_norm.json"),
}
id_lookups = lambda: id_
hu = {"lemma_lookup": get_file("hu_lemma_lookup.json")}
hu_lookups = lambda: hu
fa = {
    "lemma_rules": get_file("fa_lemma_rules.json"),
    "lemma_index": get_file("fa_lemma_index.json"),
    "lemma_exc": get_file("fa_lemma_exc.json"),
}
fa_lookups = lambda: fa
en = {
    "lemma_lookup": get_file("en_lemma_lookup.json"),
    "lemma_rules": get_file("en_lemma_rules.json"),
    "lemma_index": get_file("en_lemma_index.json"),
    "lemma_exc": get_file("en_lemma_exc.json"),
    "lexeme_norm": get_file("en_lexeme_norm.json"),
}
en_lookups = lambda: en
el = {
    "lemma_index": get_file("el_lemma_index.json"),
    "lemma_exc": get_file("el_lemma_exc.json"),
    "lemma_rules": get_file("el_lemma_rules.json"),
    "lexeme_norm": get_file("el_lexeme_norm.json"),
}
el_lookups = lambda: el
bn = {"lemma_rules": get_file("bn_lemma_rules.json")}
bn_lookups = lambda: bn
tl = {"lemma_lookup": get_file("tl_lemma_lookup.json")}
tl_lookups = lambda: tl
ur = {"lemma_lookup": get_file("ur_lemma_lookup.json")}
ur_lookups = lambda: ur
lb = {
    "lemma_lookup": get_file("lb_lemma_lookup.json"),
    "lexeme_norm": get_file("lb_lexeme_norm.json"),
}
lb_lookups = lambda: lb
ru = {"lexeme_norm": get_file("ru_lexeme_norm.json")}
ta = {"lexeme_norm": get_file("ta_lexeme_norm.json")}
th = {"lexeme_norm": get_file("th_lexeme_norm.json")}
pl = {
    "lemma_lookup_adj": get_file("pl_lemma_lookup_adj.json"),
    "lemma_lookup_adp": get_file("pl_lemma_lookup_adp.json"),
    "lemma_lookup_adv": get_file("pl_lemma_lookup_adv.json"),
    "lemma_lookup_aux": get_file("pl_lemma_lookup_aux.json"),
    "lemma_lookup_noun": get_file("pl_lemma_lookup_noun.json"),
    "lemma_lookup_num": get_file("pl_lemma_lookup_num.json"),
    "lemma_lookup_part": get_file("pl_lemma_lookup_part.json"),
    "lemma_lookup_pron": get_file("pl_lemma_lookup_pron.json"),
    "lemma_lookup_verb": get_file("pl_lemma_lookup_verb.json"),
}
pl_lookups = lambda: pl
de_extra = {
    "lexeme_cluster": get_file("de_lexeme_cluster.json"),
    "lexeme_prob": get_file("de_lexeme_prob.json"),
    "lexeme_settings": get_file("de_lexeme_settings.json"),
}
el_extra = {
    "lexeme_prob": get_file("el_lexeme_prob.json"),
    "lexeme_settings": get_file("el_lexeme_settings.json"),
}
en_extra = {
    "lexeme_cluster": get_file("en_lexeme_cluster.json"),
    "lexeme_prob": get_file("en_lexeme_prob.json"),
    "lexeme_settings": get_file("en_lexeme_settings.json"),
}
es_extra = {
    "lexeme_cluster": get_file("es_lexeme_cluster.json"),
    "lexeme_prob": get_file("es_lexeme_prob.json"),
    "lexeme_settings": get_file("es_lexeme_settings.json"),
}
