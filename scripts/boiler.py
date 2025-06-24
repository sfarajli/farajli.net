import textwrap

def print_html_head(title, style=None):
    print(textwrap.dedent(f"""\
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    	<meta name="viewport" content="width=1024">
    	<link rel='stylesheet' type='text/css' href="/style.css">
    	<link rel="icon" type="image/x-icon" href="/favicon.ico">
    	<title>{title}</title>"""))

    if style:
        print(textwrap.dedent(f"""\
        <style>
        {style}
        </style>"""))

    print(textwrap.dedent("""\
    </head>
    <body>
    	<table id="bar">
    	<tr>
    		<td id='header-name'>Suleyman Farajli</td>
    		<td id='quote'></td>
    	</tr>
    	</table>
    	<script>
    		let quotes = ["Uncensored", "Oh mamma mia!", "Memento Mori!", "Oh là là!", "C'est légal parce que je le veux", "Sweet Dreams Are Made of This"];
    		let randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
    		document.getElementById("quote").innerText = randomQuote;
    	</script>

    	<hr class="separator">

    <div class="menu">
    	<a class="menu_item" href="/home/index.html">Home/</a>
    	<a class="menu_item" href="/posts/index.html">Posts/</a>
    	<a class="menu_item" href="/archive/index.html">Archive/</a>
    	<a class="menu_item" href="/keys/index.html">Keys/</a>
    	<a class="menu_item right_menu_item" href="https://git.farajli.net">Git</a>
    </div>
    <div class="text">"""))

def print_html_tail():
    print(textwrap.dedent("""\
    </div>
    <p>
      <a id="copyleft" href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener noreferrer">
        copyleft (c) 2024-2025 Suleyman Farajli
      </a>
    </p>
    </body>
    </html>"""))
