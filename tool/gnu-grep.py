#!/usr/bin/env python3

import sys
import json

import gnu_manuals_utilities as gmu

if __name__ == "__main__":
    doc = json.load(sys.stdin)

    gmu.remove_table_of_contents(doc)
    gmu.remove_navigation_headers(doc)

    gmu.handle_multiline_dl_terms(doc)

    json.dump(doc, sys.stdout)
