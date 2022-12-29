import pandas as pd
import os
from datetime import datetime
import glob
import time
import pathlib



dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
print(dt)

dt1 = dt.tz_localize('UTC')

timezone = "Europe/Stockholm"
dtz = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f") + " " + timezone
print(dtz)

# Give the location of your file
#file_to_process = 'datasets/creditunion.csv'

def intro():
    csv_files_list = glob.glob('datasets/*')
    csv_files = []
    for file in csv_files_list:
        csv_files.append(file.replace('datasets/', ''))
    print('Hello. Your datasets folder contains the following files: ' + str(csv_files))
    print('\nEnter the csv file name from the list output that you wish to load: ')
    file_to_process = input()
    print('The file you have chosen is: ' + file_to_process)
    time.sleep(2)
    file_to_read = 'datasets/' + file_to_process + ('.csv')
    return file_to_read

def extract_from_csv(): 
    fname = intro()
    if pathlib.Path(fname).is_file(): # Check if file exists
        print('Getting ready to preview file load now')
        time.sleep(2)
        extracted_data = pd.read_csv(fname, skiprows=0)
        print(extracted_data.head(3))
        return extracted_data
  
def transform_data():
    rows = extract_from_csv()
    df = pd.DataFrame(rows)
    df['year'] = 1990
    df['date_string'] = df['year'].astype(str) + df['MONTH'].astype(str) + df['DAYMON'].astype(str)
    return df

def load_data():
    data = transform_data()
    nrows = data.shape[0]
    ncols = data.shape[1]
    print("Finished transformation and data load at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    return data

load_data()
