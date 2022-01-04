from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver



url = "https://keen-northcutt-0b6b90.netlify.app/"
driver = webdriver.Chrome("C://webdrivers/chromedriver.exe")
driver.get(url)
soup = BeautifulSoup(driver.page_source, "html.parser")

for tag in soup.find_all("div", class_="container aos-init aos-animate"):
  print(tag.get_text(separator=" "))




    
driver.close()