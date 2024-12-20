SRC := $(shell find . -name '*.md')
HTML = $(SRC:.md=.html)

all: $(HTML) build-page

%.html: %.md
	sh build-page $< > $@

clean:
	rm -f $(HTML)

.PHONY: all clean
