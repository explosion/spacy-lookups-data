import os
import spacy


def test_all_entry_points():
    entry_points = spacy.registry.lookups.get_all()
    for lang, tables in spacy.registry.lookups.get_all().items():
        for name, filename in tables.items():
            spacy.util.load_language_data(filename)
