# Input user data for website
title = input("Website title: ")
keywords = input("Website keywords: ")
metaDescription = input("Website meta description :")
h1 = input("H1 text: ")
article = input("Article text: ")
filename = input("Output HTML Filename: ")


# Write Data Output to a HTML file
def htmloutput():
    f = open((filename) + ".html","w+")
    f.write(
    f"""
    <html>
    <title>{title}<title>
    <meta name="keywords" content"{keywords}">
    <meta name="description" content="{metaDescription}"
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <body>
    <main>
	<header>{title}</header>
	<nav>Nav bar...</nav>
	<article>{article}</article>
	<footer>Copyright 2019 - Yourdomain.com</footer>
	</main>
    </body>
    </html>
    """
    )
    print("Created " + filename + ".html")
htmloutput()
