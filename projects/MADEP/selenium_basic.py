from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select




url = "https://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos"
driver = webdriver.Chrome("C://webdrivers/chromedriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")
#print(soup.prettify())

#items = soup.find_all("select")

#print(items)

#for items in soup.find_all("span", class_="input ng-scope"):
 # print(items)

#for items in soup.find_all("select", id="TownName"):
 # print(items)



#for items in soup.find_all("select", id="TownName"):
 # print(items.get_text(separator=" "))

#for item in items:
#  if item.get_attribute("option value") =="ACTON":
#    print(items)

#select_city = select(driver.find_element_by_class_name("ng-scope ng-isolate-scope ng-empty"))
#select_city.select_by_value('ACTON')

#for option in select_city.options:
 # print(option.text)

#print(len(select_city.options))

select_tag = soup.find("select")
options = select_tag.find_all("option")
for option in options:
  print(option.text)



    
driver.close()