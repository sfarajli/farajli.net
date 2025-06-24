POSTS = $(filter-out content/posts/index.md, $(wildcard content/posts/*.md))
GENERATEDMD  = content/posts/index.md

content/posts/index.md: $(POSTS)
	scripts/generate_post_index > $@
