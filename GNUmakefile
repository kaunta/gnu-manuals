PANDOC=pandoc
PYTHON3=python3

# "--toc-depth=6" because
#
# (1) I want all headings to appear in the table of contents.
# (2) I assume the maximum heading depth is 6 deep.
#
PANDOC_EPUB_OPTS= \
	--table-of-contents \
	--toc-depth=6 \
	--number-sections

MANUALS := gnu_bash gnu_grep gnu_sed

gnu_manuals_release.tgz: $(patsubst %, build/%.epub, $(MANUALS))
	tar czvf $@ build

build: ; mkdir $@
source: ; mkdir $@
manual_json: ; mkdir $@

build/%.epub: source/%.markdown | build
	$(PANDOC) $(PANDOC_EPUB_OPTS) $< -o $@

source/%.markdown: manual_json/%.json tool/%.py tool/gnu_manuals_utilities.py | source
	cat $< | $(PYTHON3) tool/$*.py | $(PANDOC) -f json -t markdown > $@

manual_json/gnu_sed.json: | manual_json
	$(PANDOC) -f html -t json -o $@ https://www.gnu.org/software/sed/manual/sed.html

manual_json/gnu_grep.json: | manual_json
	$(PANDOC) -f html -t json -o $@ https://www.gnu.org/software/grep/manual/grep.html
