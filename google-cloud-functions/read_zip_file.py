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

now_ts = datetime.today()

def zipextract(request):
    bucketname = 'gcf-data-sink'
    zipfilename_with_path = 'archive.zip' 
    table_id = 'cloud_functions.sales_data'
    project_id =  os.environ.get['PROJECT_ID']

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketname)

    destination_blob_pathname = zipfilename_with_path
        
    blob = bucket.blob(destination_blob_pathname)
    zipbytes = io.BytesIO(blob.download_as_bytes())

    with ZipFile(zipbytes, 'r') as myzip:
        for contentfilename in myzip.namelist():
            contentfile = myzip.read(contentfilename)
            blob = bucket.blob("unzipped_contents" + "/" + contentfilename)
            blob.upload_from_string(contentfile)
            #print(blob.name)
            if ".csv" in blob.name:
                file_data = blob.download_as_bytes()
                
                df = pd.read_csv(BytesIO(file_data))
   
                pandas_gbq.to_gbq(df, table_id, project_id=project_id, if_exists='replace')
            return 'Executed Successfully ' + str(now_ts)