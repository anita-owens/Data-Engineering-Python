import requests
#import json
import pandas as pd
#import pprint
#import flatdict
from pandas.io.json import json_normalize
#import pandas_gbq
import os
from datetime import datetime

base_url = 'https://ipapi.co/json'

"""
def request_data():
    response = requests.get(base_url)
    if response.status_code != 200:
        print("Failed to establish connection to server")
        sys.exit()
    else:
        data = response.json()
    return data
"""

def request_data():
    try:
        response = requests.get(base_url).json()
        return response
    except:
        print("ERROR: Failed to establish connection")

def normalize_data():
    data = request_data()
    #Flattens dict
    df = pd.json_normalize(data)
    print(df.head())
    return df

def load_data():
    project_id = os.environ.get('project_id')
    table_id = os.environ.get('table_id')
    data = normalize_data()
    nrows = data.shape[0]
    ncols = data.shape[1]
    pandas_gbq.to_gbq(data, table_id=table_id, project_id=project_id, if_exists='replace')
    print("Finished transformation and data load at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    return data

load_data()

base_url = 'https://ipapi.co/json'
try:
    response = requests.get(base_url).json()
except:
    print("ERROR: Failed to establish connection")

for item, key in response.items():
    print(item, key)

response = {'ip': '90.129.199.7',
 'network': '90.129.192.0/21',
 'version': 'IPv4',
 'city': 'Stockholm',
 'region': 'Stockholm County',
 'region_code': 'AB',
 'country': 'SE',
 'country_name': 'Sweden',
 'country_code': 'SE',
 'country_code_iso3': 'SWE',
 'country_capital': 'Stockholm',
 'country_tld': '.se',
 'continent_code': 'EU',
 'in_eu': True,
 'postal': '102 22',
 'latitude': 59.3287,
 'longitude': 18.0717,
 'timezone': 'Europe/Stockholm',
 'utc_offset': '+0200',
 'country_calling_code': '+46',
 'currency': 'SEK',
 'currency_name': 'Krona',
 'languages': 'sv-SE,se,sma,fi-SE',
 'country_area': 449964.0,
 'country_population': 10183175,
 'asn': 'AS1257',
 'org': 'Tele2 SWIPnet'}

## METHOD 1
data = response
# Function to flatten a nested dictionary
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                items.extend(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

# Flatten the dictionary
flat_dict = flatten_dict(data)

# Print the resulting flattened dictionary
print(flat_dict)


## METHOD 2
data = response

# Initialize an empty list to store the flattened rows
flattened_rows = []

# Loop over each partner dictionary and flatten it into a row
for item in data:
    row = {
        'ip': data['ip'],
        'network': data['network'],
        'version': data['version'],
        'city': data['city'],
        'region': data['region'],
        'region_code': data['region_code'],
        'country': data['country'],
        'country_capital': data['country_capital'],
        'continent_code': data['continent_code']
    }
    flattened_rows.append(row)

print(flattened_rows)

