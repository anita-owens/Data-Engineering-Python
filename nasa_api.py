
#python 3.10.6 anaconda3

import requests

request = requests.get('http://api.open-notify.org')
print(request.status_code)

people = requests.get('http://api.open-notify.org/astros.json')
people_json  = people.json()

# ? To print the number of people in space
print("Number of people in space:",people_json['number'])

#To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])

# ! todo: do something

