
from bs4 import BeautifulSoup
import requests
url = 'https://eeaonline.eea.state.ma.us/Portal/#!/search/permits'
html_content = requests.get(url).text
soup = BeautifulSoup(html_content, "lxml")

#res = soup.span

#print(res.get_text())
items = soup.find_all("id=\"Town\"")
print(items)


