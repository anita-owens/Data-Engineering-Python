import pandas as pd
import json

response = {
  "businesses": [
    {
      "id": "ivA6aV3QZW22Jok-sb7CQg",
      "alias": "dockside-seafood-restaurant-jacksonville-beach",
      "name": "Dockside Seafood Restaurant",
      "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/8Yr_Fsn1Kq8b0GGpGnajZg/o.jpg",
      "is_closed": 'false',
      "url": "https://www.yelp.com/biz/dockside-seafood-restaurant-jacksonville-beach?adjust_creative=rdtjBtOkzZQE7_XzbAcBmQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=rdtjBtOkzZQE7_XzbAcBmQ",
      "review_count": 1296,
      "categories": [
        {
          "alias": "seafood",
          "title": "Seafood"
        },
        {
          "alias": "tradamerican",
          "title": "American (Traditional)"
        },
        {
          "alias": "seafoodmarkets",
          "title": "Seafood Markets"
        }
      ],
      "rating": 4.5,
      "coordinates": {
        "latitude": 30.289963721428,
        "longitude": -81.4195933781741
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "2510 2nd Ave N",
        "address2": "",
        "address3": "",
        "city": "Jacksonville Beach",
        "zip_code": "32250",
        "country": "US",
        "state": "FL",
        "display_address": [
          "2510 2nd Ave N",
          "Jacksonville Beach, FL 32250"
        ]
      },
      "phone": "+19044793474",
      "display_phone": "(904) 479-3474",
      "distance": 1805.6627591502283
    },
    {
      "id": "9eU0ov9Hpw5ok-Od9PKLHw",
      "alias": "tacolu-jacksonville-beach",
      "name": "TacoLu",
      "image_url": "https://s3-media2.fl.yelpcdn.com/bphoto/vsz0ras3HtVG3RKcI3ugIw/o.jpg",
      "is_closed": 'false',
      "url": "https://www.yelp.com/biz/tacolu-jacksonville-beach?adjust_creative=rdtjBtOkzZQE7_XzbAcBmQ&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=rdtjBtOkzZQE7_XzbAcBmQ",
      "review_count": 1318,
      "categories": [
        {
          "alias": "mexican",
          "title": "Mexican"
        },
        {
          "alias": "tex-mex",
          "title": "Tex-Mex"
        },
        {
          "alias": "breakfast_brunch",
          "title": "Breakfast & Brunch"
        }
      ],
      "rating": 4,
      "coordinates": {
        "latitude": 30.28749,
        "longitude": -81.4101
      },
      "transactions": [
        "delivery"
      ],
      "price": "$$",
      "location": {
        "address1": "1712 Beach Blvd",
        "address2": "",
        "address3": "",
        "city": "Jacksonville Beach",
        "zip_code": "32250",
        "country": "US",
        "state": "FL",
        "display_address": [
          "1712 Beach Blvd",
          "Jacksonville Beach, FL 32250"
        ]
      },
      "phone": "+19042498226",
      "display_phone": "(904) 249-8226",
      "distance": 996.5808578588375
    }
  ],
  "total": 614,
  "region": {
    "center": {
      "longitude": -81.40491485595703,
      "latitude": 30.279813222227695
    }
  }
}

type(response)

## Method that doesn't work
#This doesn't work since it's not a JSON object. It's still a dict.
df = pd.json_normalize(response)
print(df)

## METHOD: 1 OF UNPACKING
#Convert response into a JSON string object
json_string_obj = json.dumps(response)
response = json_string_obj  # Paste the Yelp API response here
data = json.loads(response)

#More efficient way of doing above
data = json.loads(json.dumps(response))

# Extract information about each business
for business in data['businesses']:
    print('Name:', business['name'])
    print('Rating:', business['rating'])
    print('Address:', ', '.join(business['location']['display_address']))
    print('Categories:', ', '.join([c['title'] for c in business['categories']]))
    print('Phone:', business['phone'])
    print('URL:', business['url'])
    print('---')

# Extract the total number of businesses and the region center
total = data['total']
center = data['region']['center']
print('Total businesses:', total)
print('Region center:', center['latitude'], center['longitude'])



## METHOD2: UNFLATTEN USING 
# ITERATE THROUGH LIST OF BUSINESSES AND POPULATE A NEW TABLE BUT THE RESULT WILL BE A LIST
'''
businesses, total and region are top level keys
categories contains a dict object
coordinates contains a dict
'''

#After turning response into a string object
#MUST POP transactions, location, coordinates, display address, categories
results = data['businesses']

business_table = []
bus_cat_join_table = []

for result in results:
  result.pop("transactions", None)

  # UN-NEST SOME OF THE KEYS
  location = result.pop("location", None)
  result.update(location)

  coordinates = result.pop("coordinates", None)
  result.update(coordinates)

  result.pop("display_address", None)

  # BUILD LISTS FOR EACH TABLE
  business_table.append(result)

  categories = result.pop("categories", None)

  for category in categories:

    bus_cat = category.copy()
    bus_cat['id'] = result['id']
    bus_cat.pop("title")
    bus_cat_join_table.append(bus_cat)


# ASSEMBLE THE TABLES FOR INSERT
state = business_table[-1]['id']
insert = {
        "businesses": business_table,
        "business_category": bus_cat_join_table
    }

print(business_table)
type(business_table)
type(state)






