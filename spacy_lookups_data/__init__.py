import pkg_resources
import os

from .about import __version__  # noqa: F401


def get_file(filename):
    return pkg_resources.resource_filename(__name__, os.path.join("data", filename))


mk = {
    "lemma_lookup": get_file("mk_lemma_lookup.json"),
    "lemma_rules": get_file("mk_lemma_rules.json"),
    "lemma_index": get_file("mk_lemma_index.json"),
    "lemma_exc": get_file("mk_lemma_exc.json"),
    "lexeme_norm": get_file("mk_lexeme_norm.json"),
}
hr = {"lemma_lookup": get_file("hr_lemma_lookup.json")}
pt = {
    "lemma_lookup": get_file("pt_lemma_lookup.json"),
    "lexeme_norm": get_file("pt_lexeme_norm.json"),
}
sv = {
    "lemma_lookup": get_file("sv_lemma_lookup.json"),
    "lemma_rules": get_file("sv_lemma_rules.json"),
}
da = {
    "lemma_lookup": get_file("da_lemma_lookup.json"),
    "lexeme_norm": get_file("da_lexeme_norm.json"),
}
ca = {
    "lemma_lookup": get_file("ca_lemma_lookup.json"),
    "lemma_exc": get_file("ca_lemma_exc.json"),
    "lemma_index": get_file("ca_lemma_index.json"),
    "lemma_rules": get_file("ca_lemma_rules.json"),
}
es = {
    "lemma_lookup": get_file("es_lemma_lookup.json"),
    "lemma_exc": get_file("es_lemma_exc.json"),
    "lemma_index": get_file("es_lemma_index.json"),
    "lemma_rules": get_file("es_lemma_rules.json"),
    "lemma_rules_groups": get_file("es_lemma_rules_groups.json"),
    "lexeme_cluster": get_file("es_lexeme_cluster.json"),
    "lexeme_prob": get_file("es_lexeme_prob.json"),
    "lexeme_settings": get_file("es_lexeme_settings.json"),
}
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
de = {
    "lemma_lookup": get_file("de_lemma_lookup.json"),
    "lexeme_norm": get_file("de_lexeme_norm.json"),
    "lexeme_cluster": get_file("de_lexeme_cluster.json"),
    "lexeme_prob": get_file("de_lexeme_prob.json"),
    "lexeme_settings": get_file("de_lexeme_settings.json"),
    "orth_variants": get_file("de_orth_variants.json"),
}
it = {
    "lemma_lookup": get_file("it_lemma_lookup.json"),
    "lemma_lookup_num": get_file("it_lemma_lookup_num.json"),
    "lemma_lookup_det": get_file("it_lemma_lookup_det.json"),
    "lemma_lookup_adp": get_file("it_lemma_lookup_adp.json"),
    "lemma_lookup_adj": get_file("it_lemma_lookup_adj.json"),
    "lemma_lookup_noun": get_file("it_lemma_lookup_noun.json"),
    "lemma_lookup_pron": get_file("it_lemma_lookup_pron.json"),
    "lemma_lookup_verb": get_file("it_lemma_lookup_verb.json"),
    "lemma_lookup_aux": get_file("it_lemma_lookup_aux.json"),
    "lemma_lookup_adv": get_file("it_lemma_lookup_adv.json"),
    "lemma_lookup_other": get_file("it_lemma_lookup_other.json"),
}
lt = {"lemma_lookup": get_file("lt_lemma_lookup.json")}
nl = {
    "lemma_rules": get_file("nl_lemma_rules.json"),
    "lemma_index": get_file("nl_lemma_index.json"),
    "lemma_exc": get_file("nl_lemma_exc.json"),
    "lemma_lookup": get_file("nl_lemma_lookup.json"),
}
ro = {"lemma_lookup": get_file("ro_lemma_lookup.json")}
sr = {
    "lemma_lookup": get_file("sr_lemma_lookup.json"),
    "lexeme_norm": get_file("sr_lexeme_norm.json"),
}
id_ = {
    "lemma_lookup": get_file("id_lemma_lookup.json"),
    "lexeme_norm": get_file("id_lexeme_norm.json"),
}
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
    "lexeme_norm": get_file("en_lexeme_norm.json"),
    "lexeme_cluster": get_file("en_lexeme_cluster.json"),
    "lexeme_prob": get_file("en_lexeme_prob.json"),
    "lexeme_settings": get_file("en_lexeme_settings.json"),
    "orth_variants": get_file("en_orth_variants.json"),
}
el = {
    "lemma_index": get_file("el_lemma_index.json"),
    "lemma_exc": get_file("el_lemma_exc.json"),
    "lemma_rules": get_file("el_lemma_rules.json"),
    "lexeme_norm": get_file("el_lexeme_norm.json"),
    "lexeme_prob": get_file("el_lexeme_prob.json"),
    "lexeme_settings": get_file("el_lexeme_settings.json"),
}
bn = {"lemma_rules": get_file("bn_lemma_rules.json")}
tl = {"lemma_lookup": get_file("tl_lemma_lookup.json")}
ur = {"lemma_lookup": get_file("ur_lemma_lookup.json")}
lb = {
    "lemma_lookup": get_file("lb_lemma_lookup.json"),
    "lexeme_norm": get_file("lb_lexeme_norm.json"),
}
ru = {
    "lexeme_norm": get_file("ru_lexeme_norm.json"),
    "lemma_lookup": get_file("ru_lemma_lookup.json"),
}
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
cs = {
    "lemma_lookup": get_file("cs_lemma_lookup.json"),
    "lexeme_norm": get_file("cs_lexeme_norm.json"),
}
