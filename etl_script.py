import pandas as pd
import os
from datetime import datetime
# Give the location of your file -
#file_to_process = ('datasets/Dinner.xlsx')
print(os.getcwd())

file_to_process = 'datasets/creditunion.csv'


def extract_from_csv(): 
    extracted_data = pd.read_csv(file_to_process) 
    return extracted_data

#extract_from_csv('file_path)

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
    print("Finished at {}. Uploaded {} rows and {} columns".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    #return data

load_data()