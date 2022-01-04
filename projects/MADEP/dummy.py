from lxml import html
import requests
dynamicUrl = "https://eeaonline.eea.state.ma.us/Portal/#!/search/inspections"
dynamicPage = requests.get(dynamicUrl)
dynamicHtml = html.fromstring(dynamicPage.text)
item = dynamicHtml.xpath('//*[@id="Town"]/select/option')
print(item)

