import requests
import webbrowser
from bs4 import BeautifulSoup

very_simple_html ="""
 
<!DOCTYPE html>
<html>
    <head>
        <title>web scrape</title>
    </head>

    <body>
        <h1>Welcome to the scrapping world!</h1>

        <div>
        <select id="city" name="country">
        <option value="africa">AFRICA</option>
        <option value="india">INDIA</option>
        <option value="australia">AUSTRALIA</option>
        <option value="china">CHINA</option>
        </select>
        </div>
         <div>
        <span>
            <select id="town">
                <option value="asia">ASIA</option>
                <option value="america">AMERICA</option>
                <option value="south korea">SOUTH KOREA</option>
                <option value="canada">CANADA</option>
                <option value="japan">JAPAN</option>
            </select>
        </span>
    </div>
    <span>
        <select id="town">
            <option value="asia">ASIA</option>
            <option value="america">AMERICA</option>
            <option value="south korea">SOUTH KOREA</option>
            <option value="canada">CANADA</option>
            <option value="japan">JAPAN</option>
        </select>
    </span>
    <div>
        <select id="number">
            <option value="567">567</option>
            <option value="568">568</option>
            <option value="569">569</option>
        </select>
    </div>

    </body>
</html>

         

"""
soup = BeautifulSoup(very_simple_html, 'lxml')
#print(soup.prettify())
items = soup.find_all("option")
total_id =" "

for i in items:
    id = i.get('id')
    total_id = total_id + "\n" + str(id)


print(items)
         