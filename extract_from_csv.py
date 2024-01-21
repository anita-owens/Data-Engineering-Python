import pandas as pd
from datetime import datetime

import os
import glob
import time
import pathlib

def extract_from_csv(): 
    fname = 'datasets/orders.csv'
    extracted_data = pd.read_csv(fname, skiprows=0)
    nrows = extracted_data.shape[0]
    ncols = extracted_data.shape[1]
    print("Finished transformation and data load at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    return extracted_data
 
def create_partition_csv():
    fname = 'datasets/orders.csv'
    extracted_data = pd.read_csv(fname)
    
    # Ensure 'date' column is in datetime format
    extracted_data['date'] = pd.to_datetime(extracted_data['date'])
    
    for year_month, group in extracted_data.groupby(extracted_data['date'].dt.strftime('%Y-%m')):
        # Create a separate CSV file for each year_month
        output_filename = f'datasets/orders_{year_month}.csv'
        group.to_csv(output_filename, index=False)
        
    nrows = extracted_data.shape[0]
    ncols = extracted_data.shape[1]
    print("Finished transformation and data load at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    
create_partition_csv()
