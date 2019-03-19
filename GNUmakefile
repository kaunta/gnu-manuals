PANDOC=pandoc

# "--toc-depth=6" because
#
# (1) I want all headings to appear in the table of contents.
# (2) I assume the maximum heading depth is 6 deep.
#
PANDOC_EPUB_OPTS= \
	--table-of-contents \
	--toc-depth=6 \
	--number-sections

MANUALS := $(patsubst source/%.markdown, %, $(wildcard source/*.markdown))

build: ; mkdir $@

build/%.epub: source/%.markdown | build
	$(PANDOC) $(PANDOC_EPUB_OPTS) $< -o $@

gnu_manuals_release.tgz: $(patsubst %, build/%.epub, $(MANUALS))
	tar czvf $@ build
