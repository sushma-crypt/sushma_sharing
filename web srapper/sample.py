from bs4 import BeautifulSoup

with open("dum.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

print(doc.prettify())  

tag = doc.h1
tag.string = "python world"
print(doc)