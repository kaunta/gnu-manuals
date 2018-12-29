PANDOC=pandoc

# "--toc-depth=6" because
#
# (1) I want all headings to appear in the table of contents.
# (2) I assume the maximum heading depth is 6 deep.
#
PANDOC_EPUB_OPTS= \
	--table-of-contents \
	--toc-depth=6

%.epub: %.markdown
	$(PANDOC) $(PANDOC_EPUB_OPTS) $< -o $@
