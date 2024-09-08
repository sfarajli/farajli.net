SRC := $(shell find . -name '*.md')
HTML = $(SRC:.md=.html)

all: $(HTML)

%.html: %.md
	sh build-page $< > $@

clean: 
	rm -f $(HTML)

.PHONY: clean
