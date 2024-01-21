#from dotenv import load_dotenv
#https://github.com/theskumar/python-dotenv/issues/273
import os
import json
import requests
import pandas as pd

# load_dotenv()


def make_request():
    headers = {"accept": "application/json"}
    client_id = 'rdtjBtOkzZQE7_XzbAcBmQ'
    api_key = 'QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx'
    root_url = "https://api.yelp.com/v3/businesses/search"
    location = "Jacksonville+Beach"
    type = "makerspaces"
    url = "{0}?location={1}&categories={2}".format(root_url, location, type)
    headers = {"Authorization": "Bearer {0}".format(api_key)}
    try:
        response_text = requests.request("GET", url, headers=headers)
        #response = requests.get(root_url)
        #response.raise_for_status()
        #data = response.json()
        #print(response.status_code)
        return response_text
    except:
        print("ERROR: Failed to establish connection")


if __name__ == "__main__":
    make_request()


# which python
# pip freeze | grep dotenv

    """_summary_
    import requests

url = "https://api.yelp.com/v3/businesses/search?location=jacksonville%2Bbeach&sort_by=best_match&limit=20"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx"
}

response = requests.get(url, headers=headers)

print(response.text)
    """

headers = {"accept": "application/json"}
client_id = 'rdtjBtOkzZQE7_XzbAcBmQ'
api_key = 'QEUysp33WD-wU0kukuIW_gjWXRYWUhY14dnzS4eF9O2PxNUUMiUNYoFgkP_H43silSEmDjCPcx3ZtmEVFM-ugmXmCiljTxJdu1JZeccWtcPXGtqaNXYPD7SjPdseZHYx'
root_url = "https://api.yelp.com/v3/businesses/search"
location = "San+Francisco"
type = "makerspaces"
url = "{0}?location={1}&categories={2}".format(root_url, location, type)
headers = {"Authorization": "Bearer {0}".format(api_key)}
#response = requests.request("GET", url, headers=headers).json()
response = requests.request("GET", url, headers=headers)

##METHOD 1 UNFLATTEN WITH JSON_NORMALIZE
#print(response.status_code)
print(response)

json_data = response.json()
print(json_data)
df1 = pd.json_normalize(json_data)
print(df1.head())

## METHOD 2 UNFLATTEN WITH FOR LOOP AND POPULATING AN EMPTY DATAFRAME
# Create empty DataFrame with desired columns
df = pd.DataFrame(columns=['id', 'name', 'rating', 'review_count', 'price', 'latitude', 'longitude', 'address1', 'address2', 'city', 'zip_code', 'country', 'state', 'phone', 'distance'])

# Loop over businesses and extract data
for business in response['businesses']:
    data = {
        'id': business['id'],
        'name': business['name'],
        'rating': business['rating'],
        'review_count': business['review_count'],
        'price': business.get('price', None),
        'latitude': business['coordinates']['latitude'],
        'longitude': business['coordinates']['longitude'],
        'address1': business['location']['address1'],
        'address2': business['location'].get('address2', None),
        'city': business['location']['city'],
        'zip_code': business['location']['zip_code'],
        'country': business['location']['country'],
        'state': business['location']['state'],
        'phone': business['phone'],
        'distance': business['distance']
    }
    
    # Append data to DataFrame
    df = df.append(data, ignore_index=True)

## METHOD 3 UNFLATTEN USING 
# ITERATE THROUGH LIST OF BUSINESSES AND POPULATE A NEW TABLE BUT THE RESULT WILL BE A LIST
'''
businesses, total and region are top level keys
categories contains a dict object
coordinates contains a dict
'''
results = response['businesses']

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



##EXAMPLE RESPONSE OBJECT
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

for key in response.keys():
  print(key)

'''
The keys
1. businesses
2.total
3. region
'''
response["businesses"]

location # contains a list
coordinates
categories


