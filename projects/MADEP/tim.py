from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos")


print(driver.title)
data = driver.find_element_by_class_id("TownName")
data.send_keys("test")
data.send_keys(keys.RETURN)
print(data.text)
time.sleep(5)

driver.quit()