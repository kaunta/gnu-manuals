#!/usr/bin/env python3

import datetime
import json
import sys

import gnu_manuals_utilities as gmu

def main():
    doc = json.load(sys.stdin)

    gmu.set_title_author_date(doc,
        title = "Sed Reference Manual v4.7",
        author = "The GNU Project",
        date = datetime.date(2018, 12, 29)
    )

    gmu.remove_table_of_contents(doc)
    gmu.remove_navigation_headers(doc)

    gmu.handle_multiline_dl_terms(doc)
    gmu.correct_numbered_headings(doc)

    remove_initial_headers(doc)
    fix_appendices_and_indices(doc)

    json.dump(doc, sys.stdout)

def remove_initial_headers(doc):
    """\
    Remove the initial headers "sed, a stream editor" and "GNU sed".
    """
    def match_heading_id(block, id):
        try:
            return (
                block["t"] == "Header" and
                block["c"][1][0] == id
            )
        except:
            return False

    doc["blocks"] = [
        block
        for block in doc["blocks"]
        if not (
            match_heading_id(block, "gnu-sed") or
            match_heading_id(block, "sed-a-stream-editor")
        )
    ]

def fix_appendices_and_indices(doc):
    """\
    Fix the heading level of Appendix A, the addendum, the indices, and the footnotes.
    """
    def match_heading_id(block, id):
        try:
            return (
                block["t"] == "Header" and
                block["c"][1][0] == id
            )
        except:
            return False

    for block in doc["blocks"]:
        if match_heading_id(block, "addendum-how-to-use-this-license-for-your-documents"):
            block["c"][0] = 2
        elif match_heading_id(block, "appendix-a-gnu-free-documentation-license"):
            block["c"][0] = 1
        elif match_heading_id(block, "concept-index"):
            block["c"][0] = 1
        elif match_heading_id(block, "command-and-option-index"):
            block["c"][0] = 1

if __name__ == "__main__":
    main()