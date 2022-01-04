

import json
people_string = '''

{
    "people":[
        {
            "name": "kumar",
            "mail": ["kumar@gmail.com"],
        },
        {
           "name": "bala",
           "mail": ["bala@gmail.com"], 

        }
        }
    ]
}
'''
data = json.loads(people_string)
print(data)