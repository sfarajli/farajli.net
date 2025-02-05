SRC := $(shell find . -name '*.md')
HTML = $(SRC:.md=.html)

all: $(HTML)

%.html: %.md build-page
	mkdir -p out/$$(dirname $@)
	sh build-page $< > out/$@

clean:
	rm -rf out/

.PHONY: all clean
