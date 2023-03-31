import requests
#import json
import pandas as pd
#import pprint
#import flatdict
from pandas.io.json import json_normalize
import pandas_gbq
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
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()
        return data
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