import requests
from requests.sessions import session
session = requests.Session()
parameters = {'Facility/Individual ':'Enter your detail','City/Town ':'select your city'}
r = requests.post("http://eeaonline.eea.state.ma.us/Portal/#!/search/inspections", data = parameters)

print(r.text)
print("complted")