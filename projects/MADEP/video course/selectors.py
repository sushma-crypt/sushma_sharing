import requests
from bs4 import BeautifulSoup
import webbrowser

very_simple_html = """
<!DOCTYPE html>
<html>
   <head>
      <title>My Test Page</title>
   </head>
   <body>
	  <p>Simple Page to Test</p>
      <select id="select1">
		<option value="1">1</option>
		<option value="2">2</option>
		<option value="3">3</option>
      </select>
      <div id="div1">
         <select id="select2">
			<option value="4">4</option>
			<option value="5">5</option>
         </select>
      </div>
      <div id="div2">
         <span id="span1">
         <select id="select3">
			<option value="600">600</option>
			<option value="700">700</option>
         </select>
         </span>
      </div>
      <div id="div3">
         <div id="div4">
            <span id="span1">
            <select id="select4">
				<option value="800">800</option>
            </select>
            </span>
         </div>
      </div>
   </body>
</html> 
"""

soup = BeautifulSoup(very_simple_html, 'lxml')
#print(soup.prettify())

items = soup.find_all("select")
print(items)

items = soup.find_all("div")
print(items)



 