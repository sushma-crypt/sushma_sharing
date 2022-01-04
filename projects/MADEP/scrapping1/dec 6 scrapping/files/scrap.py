import requests
import webbrowser
from bs4 import BeautifulSoup

very_simple_html ="""
<html>
    <head>
    <title>web scrapping</title>
    </head>


<body>

<p class="title">
    <b>the scrapping story</b>
</p>

<p class="story">
 once in a decade:
 <a href="http://example.com/elsie class="sister" id="link1">elsie</a>;   

</p>

<p class ="story">the scarpper</p>
</body>
</html>
"""
soup = BeautifulSoup(very_simple_html)
print(soup.prettify())

soup.body.parent.name
         