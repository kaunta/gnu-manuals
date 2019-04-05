#!/usr/bin/env python3

import itertools

def remove_table_of_contents(doc):
    assert tuple(doc["pandoc-api-version"]) == (1, 17, 5, 4)

    # Remove table-of-contents heading
    def like_toc_heading(block):
        try:
            return block["t"] == "Header" and block["c"][1][0] == "table-of-contents"
        except:
            return False

    doc["blocks"] = list(itertools.filterfalse(like_toc_heading, doc["blocks"]))

    # Remove table-of-contents div
    def like_toc_div(block):
        try:
            return block["t"] == "Div" and block["c"][0][1][0] == "contents"
        except:
            return False

    doc["blocks"] = list(itertools.filterfalse(like_toc_div, doc["blocks"]))

def remove_navigation_headers(doc):
    def like_navigation_header(block):
        try:
            return block["t"] == "Div" and block["c"][0][1][0] == "header"
        except:
            return False

    doc["blocks"] = list(itertools.filterfalse(like_navigation_header, doc["blocks"]))
