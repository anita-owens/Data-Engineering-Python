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
location = "Chicago"
type = "makerspaces"
url = "{0}?location={1}&categories={2}".format(root_url, location, type)
headers = {"Authorization": "Bearer {0}".format(api_key)}
response = requests.request("GET", url, headers=headers)
print(response.status_code)
json_data = response.json()
print(json_data)

df = pd.json_normalize(json_data)
print(df)

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

#This doesn't work since it's not a JSON object. It's still a dict.
df = pd.json_normalize(response)
print(df)

#Convert response into a JSON string object
json_string_obj = json.dumps(response)

# +
import json

response = json_string_obj  # Paste the Yelp API response here
data = json.loads(response)

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


# +
import pandas as pd

#response = json_string_obj  # Paste the Yelp API response here
#data = json.loads(response)

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

# -


