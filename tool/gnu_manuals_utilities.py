#!/usr/bin/env python3

import itertools

def remove_table_of_contents(doc):
    """\
    Remove the table of contents from a GNU manual document.

    This is done by removing the table of contents heading, as well as the
    numbered list of the actual contents.
    """

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
    """\
    Remove the navigation headers in every section from a GNU manual document.

    This is done by removing divs with the class "header".
    """

    assert tuple(doc["pandoc-api-version"]) == (1, 17, 5, 4)

    def like_navigation_header(block):
        try:
            return block["t"] == "Div" and block["c"][0][1][0] == "header"
        except:
            return False

    doc["blocks"] = list(itertools.filterfalse(like_navigation_header, doc["blocks"]))

def handle_multiline_dl_terms(doc):
    """\
    Fix multiline definition list (dl) terms from a GNU manual document.

    Multiline definition list terms aren't supported in pandoc style markdown,
    so multiple lines are joined with a comma.
    """

    assert tuple(doc["pandoc-api-version"]) == (1, 17, 5, 4)

    def is_definition_list(block):
        try:
            return block["t"] == "DefinitionList"
        except:
            return False

    def single_line_definition_term(block):
        for b in block:
            if b == { "t": "LineBreak" }:
                yield { "t": "Str", "c": "," }
                yield { "t": "Space" }
            else:
                yield b

    def fix_multiline_definition_terms(block):
        if not is_definition_list(block):
            return

        block["c"] = [
            [ list(single_line_definition_term(term)), definition ]
            for term, definition in block["c"]
        ]

    for block in doc["blocks"]:
        fix_multiline_definition_terms(block)
