SRC = $(shell find . -name '*.md')
HTML = $(patsubst ./%.md, %.html, $(SRC))

all: $(HTML)

%.html: %.md build-page
	sh build-page $< > $@

output/: $(HTML)
	echo $? | xargs -n 1 dirname | xargs -I _ mkdir -p $@_
	echo $? | xargs -n 1 | xargs -I _ cp _ 	$@_
	cp favicon.ico style.css $@

clean:
	rm -rf $(HTML) output/

.PHONY: all clean 
