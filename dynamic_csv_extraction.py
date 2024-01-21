import os
import pandas as pd
from datetime import datetime

def dynamic_csv_extraction(filename, folder_path=None):
    extracted_data = pd.read_csv(filename)
    
    # Ensure 'date' column is in datetime format
    extracted_data['date'] = pd.to_datetime(extracted_data['date'])
    
    for year_month, group in extracted_data.groupby(extracted_data['date'].dt.strftime('%Y-%m')):
        # Extract year and month from year_month
        year, month = year_month.split('-')

        # Determine the folder path
        if folder_path is None:
            specific_folder_path = os.path.join('datasets/orders', year)
        else:
            specific_folder_path = os.path.join(folder_path, year)

        # Create folders if they don't exist
        os.makedirs(specific_folder_path, exist_ok=True)
        
        # Create a separate CSV file for each year_month
        output_filename = os.path.join(specific_folder_path, f'orders_{year_month}.csv')
        group.to_csv(output_filename, index=False)
        #print(f"CSV file created: {output_filename}")
        
    nrows = extracted_data.shape[0]
    ncols = extracted_data.shape[1]
    print("Finished transformation and data load at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))

# Usage 1: With a specified folder_path
filename = 'datasets/orders.csv'
folder_path = 'datasets/reporting/'
dynamic_csv_extraction(filename, folder_path)

# Usage 2: Without specifying folder_path (it will use the default path)
#filename = 'datasets/orders.csv'
#dynamic_csv_extraction(filename)
