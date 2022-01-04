from selenium import webdriver



url = 'http://eeaonline.eea.state.ma.us/Portal/#!/search/asbestos'
driver = webdriver.Chrome()
driver.get(url)

items = driver.find_element_by_class_name('ng-scope ng-isolate-scope ng-empty')

for item in items:
    title = item.find_element_by_xpath('.//*[@id="TownName"]').text
    view = item.find_element_by_xpath('.//*[@id="TownName"]/option[1]').text
    data = item.find_element_by_xpath('.//*[@id="TownName"]/option[2]').text

    print(title,view,data)
    
        