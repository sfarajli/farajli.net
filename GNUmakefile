MD           = $(shell find content/ -name '*.md')
PROPERMD     = $(shell scripts/filter_proper_md $(MD))
HTML         = $(patsubst content/%.md, public/%.html, $(PROPERMD))
STATICASSETS = $(shell find static -type f)
PUBLICASSETS = $(patsubst static/%, public/%, $(STATICASSETS))

# Calling make is used for making sure that index pages are build first
all:
	$(MAKE) -f index_pages.mk
	$(MAKE) pages

pages: $(HTML) $(PUBLICASSETS)

public/%.html: content/%.md
	mkdir -p $$(dirname $@)
	scripts/build_page $< > $@

$(PUBLICASSETS): public/%: static/%
	mkdir -p $$(dirname $@)
	cp $< $@

clean:
	rm -rf public

.PHONY: all clean pages
