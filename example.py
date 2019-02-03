# Input user data for website
websitename = input("Website name: ")
title = input("Website title: ")
keywords = input("Website keywords: ")
metaDescription = input("Website meta description :")
h1 = input("H1 text: ")
h2 = input("H2 text: ")
article = input("Article text: ")
article2 = input("Article text: ")
affiliatelink = input("Affiliate link: ")
affiliateimage = input("Affiliate image: ")
article2h2 = input("Article2 H2 text: ")
buttontext = input("Affiliate Buy Button Text: ")

filename = input("Output HTML Filename: ")


# Write Data Output to a HTML file
def htmloutput():
    f = open((filename) + ".html","w+")
    f.write(
    f"""
 
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{metaDescription}">
<link rel="stylesheet" href="css/style.css">
<link rel="icon" href="img/favicon.png" type="image/png" sizes="16x16"> 

 </head>
  <!-- Top Ad Sticky Banner -->

<div id="topad">
    <div id="om-sxwhvgxkaya7iualjy5l" class="CampaignTypefloating">


<div class="CampaignalphaLayer">
<div class="Campaign__bravoLayer">
<div class="Campaign__content">
<div class="Row">
<div id="Row_content">
<div class="Column"><div class="Column__content">
<div class="insideColumn"><div class="Element"><div class="Element__content">
<div class="detroit-CountdownElement--wrapper">
<div id="detroit-CountdownElement--jnaysnms" class="detroit-CountdownElement--content" data-omcd-time="13313" data-omcd-type="dynamic" data-omcd-id="jnaysnms" data-omcd-local="true">
<div class="detroit-hours">
<span class="number-stringnumber-hours">

<!-- Display the countdown timer in an element -->
<p id="demo"></p>
</div></div></div></div></div></div></div></div>

<div class="Column">
<div class="Column__content">
<div class="insideContent">
<div class="Element">
<div class="ement__content">
<div class="detroit-TextElement--wrapper">
<div class="detroit-TextElement--content">
<p>
<span class="newbox">
<strong>SPECIAL OFFER </strong>- Save 20% OFF Fiverr - Limited Time Deal!</span></p>
</div></div></div></div></div></div></div>
</div></div></div></div>
<div></div>
</div></div>
<div id="website">
<div id="websites">
<div id="banner"><div id="site-logo">
<h1>{websitename}</h1>
</div></div></div>
<!-- Right sidebar for menu -->
<div id="sidebar">

<!-- Right Sidebar Ad -->
<a href="{affiliatelink}" Target="_Top"><img border="0" src="{affiliateimage}" width="160" height="600"></a>
</div>

<!-- Left Sidebar Ad -->
<div id="leftsidebar">
<a href="{affiliatelink}" Target="_Top"><img border="0" src="{affiliateimage}" width="160" height="600"></a>

</div>

<!-- Article in the middle -->
<div id="article">
            <br><br><br><br>
<h2>{h2}</h2><p></p>
{article}
<div id="article2">
<br>
<h2>{article2h2}</h2><p></p>
{article2}
<center><a href="{affiliatelink}"><button>{buttontext}</button></a></center>

<p></div>

<div id=footer>Copyright 2019 - {websitename}<p>
THIS WEBSITE WAS NOT CREATED BY FIVERR, BUT ARE JUST AN AFFILIATE FIVERR WEBSITE WHICH OFFERS A DISCOUNT
</div></div></div></div>
<script src="js/javascript.js"></script> 
</body>
</html>
   """
)
print("Created " + filename + ".html")
htmloutput()
