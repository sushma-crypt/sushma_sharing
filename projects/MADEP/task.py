
from bs4 import BeautifulSoup
import requests

url = 'https://eeaonline.eea.state.ma.us/Portal/#!/search/inspections'
html =requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
#print(soup.prettify())



items = soup.find(attrs={'id' :'town'})
items_box =items.find(attrs={'class' :'input ng-scope'})
name = items_box.text
print(name)

#print(items.prettify())
#for i  in items:
 #   print(i.text)

print("completed")

