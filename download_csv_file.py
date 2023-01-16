import requests
import glob
import pathlib
import pandas as pd


def download_file():
    url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/bachelorette/bachelorette.csv'
    # Define the local filename to save data
    local_file = 'datasets/bachelorette.csv'

    # Make http request for remote file data
    data = requests.get(url)

    # Save file data to local copy
    with open(local_file, 'wb') as file:
        file.write(data.content)
    return local_file

#download_file()

def extract_from_csv(): 
    fname = download_file()
    if pathlib.Path(fname).is_file(): # Check if file exists
        extracted_data = pd.read_csv(fname, skiprows=0)
        return extracted_data


extract_from_csv()

