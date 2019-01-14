title = input("Website title: ")
websitetitle = input("Website title: ")
keywords = input("Website keywords: ")
metaDescription = input("Website meta description :")
h1 = input("H1 text: ")
filename = input("Output HTML Filename: ")


# Write Data Output to a HTML file
def htmloutput():
    f = open((filename) + ".html","w")
    f.write(
    f"""
    <html>
    <body>
    <title>{title}<title>
    <meta name="keywords" content"{keywords}">
    <meta name="description" content="{metaDescription}"
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </body>
    </html>
    """
    )
    print("Created " + filename + ".html")
htmloutput()