PANDOC=pandoc

PANDOC_EPUB_OPTS= \
	--table-of-contents

%.epub: %.markdown
	$(PANDOC) $(PANDOC_EPUB_OPTS) $< -o $@
