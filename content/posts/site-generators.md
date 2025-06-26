---
title: "About site generators."
slug: "site-generators"
created: 2025-06-24
description: "Explaining why I prefer to write my own site generator instead of using frameworks like Hugo."
tags: [Technology]
draft: false
---

Hugo is a static website generator. If you were to look at the source code of this very website,
you would see that its layout is also very similar to Hugo, yet it doesn't use it.

Hugo (and probably other site generators as well) is a little too complex for simple site generation.
You see, site generators like Hugo are designed to work on different websites, use complex directory layouts,
and are bundled with all these fancy features that you probably don't even need.
Of course, That's not a big problem, but I personally find it a little overkill, not elegant, and even ugly.

Not using Hugo means you would have to write your own site generator from scratch,
because writing plain HTML isn't really an option. Doing that isn't hard, and it has the added benefit of
being built into the repository itself along with all the content, making it way more flexible than Hugo,
and also dependent on less external software.

Using Hugo is fine, but I would rather use simple shell or Python scripts with
a basic Markdown compiler like [smu](https://github.com/Gottox/smu).
