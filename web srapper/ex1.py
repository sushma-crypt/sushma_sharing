from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.ca/GIGABYTE/BrandStore/ID-1314"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



prices = doc.find_all(text="$")

parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)