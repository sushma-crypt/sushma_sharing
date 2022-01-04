from selenium import webdriver
driver = webdriver.Chrome('C:\webdrivers')
url = 'https://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos'
driver.get(url)
item = driver.find_element_by_xpath('//*[@id="TownName"]/span')
item_data = item.find_elements_by_tag_name("select")
print(len(item_data))
driver.close