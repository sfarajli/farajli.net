SRC := $(shell find . -name '*.md')
HTML = $(SRC:.md=.html)

all: $(HTML)

%.html: %.md build-page
	sh build-page $< > $@

clean:
	rm -f $(HTML)

.PHONY: all clean
