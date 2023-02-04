#https://stackoverflow.com/questions/49541026/how-do-i-unzip-a-zip-file-in-google-cloud-storage
import io
from io import BytesIO
from zipfile import ZipFile
from google.cloud import storage
from google.cloud.storage import Client
import pandas as pd
import pandas_gbq
from datetime import datetime
import os

#Assumes bucket and zipped file exists in GCS
def zipextract():
    bucket_name = 'gcf-data-sink'
    zipfilename_with_path = 'archive.zip'

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    destination_blob_pathname = zipfilename_with_path
        
    blob = bucket.blob(destination_blob_pathname)
    zipbytes = io.BytesIO(blob.download_as_bytes())
    print("Starting unzipping process")

    with ZipFile(zipbytes, 'r') as myzip:
        for contentfilename in myzip.namelist():
            contentfile = myzip.read(contentfilename)
            blob = bucket.blob("unzipped_contents" + "/" + contentfilename)
            blob.upload_from_string(contentfile)
            print(blob.name)
            if ".csv" in blob.name:
                file_data = blob.download_as_bytes()
                df = pd.read_csv(BytesIO(file_data), encoding='latin-1')
                return df
                
def load(request):
    table_id = os.environ['TABLE_ID']
    project_id =  os.environ['PROJECT_ID']
    data = zipextract()
    nrows = data.shape[0]
    ncols = data.shape[1]
    pandas_gbq.to_gbq(data, table_id, project_id=project_id, if_exists='replace')
    print("Finished data load at {}. Uploaded {} rows and {} columns to Biquery table {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols, table_id))
    
    print("Starting deletion process")
    delete_files = delete_blob()
    return 'Function executed successfully ' + str(datetime.today())

def delete_blob():
    """Deletes a blob from the bucket."""
    bucket_name = 'gcf-data-sink'
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blob_name = "unzipped_contents/"
    blobs = bucket.list_blobs(prefix='unzipped_contents')
    
    for blob in blobs:
        print(f'Deleting file {blob.name}')
        blob.delete()
