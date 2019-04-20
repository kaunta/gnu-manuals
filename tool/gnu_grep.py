#!/usr/bin/env python3

import datetime
import json
import sys

import gnu_manuals_utilities as gmu

if __name__ == "__main__":
    doc = json.load(sys.stdin)

    gmu.set_title_author_date(doc,
        title = "Grep Reference Manual v3.3",
        author = "The GNU Project",
        date = datetime.date(2018, 12, 29)
    )

    gmu.remove_table_of_contents(doc)
    gmu.remove_navigation_headers(doc)

    gmu.handle_multiline_dl_terms(doc)

    json.dump(doc, sys.stdout)
