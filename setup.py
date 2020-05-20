#!/usr/bin/env python
from __future__ import unicode_literals

import os
import io
from setuptools import setup, find_packages


def gzip_language_data(root, source):
    print("Compressing language data")
    import gzip
    from pathlib import Path

    base = Path(root) / source
    for jsonfile in base.glob("**/*.json"):
        outfile = jsonfile.with_suffix(jsonfile.suffix + ".gz")
        if outfile.is_file() and outfile.stat().st_mtime > jsonfile.stat().st_mtime:
            # If the gz is newer it doesn't need updating
            print("Skipping {}, already compressed".format(jsonfile))
            continue
        with open(str(jsonfile), 'r', encoding="utf-8") as infileh, gzip.open(str(outfile), 'w') as outfileh:
            outfileh.write(infileh.read().encode("utf-8"))
        print("Compressed {}".format(jsonfile))


def setup_package():
    package_name = "spacy_lookups_data"
    root = os.path.abspath(os.path.dirname(__file__))

    # Read in package meta from about.py
    about_path = os.path.join(root, package_name, "about.py")
    with io.open(about_path, encoding="utf8") as f:
        about = {}
        exec(f.read(), about)

    if not os.path.exists(os.path.join(root, "PKG-INFO")):
        gzip_language_data(root, "spacy_lookups_data/data")

    setup(name=package_name, version=about["__version__"], packages=find_packages())


if __name__ == "__main__":
    setup_package()
