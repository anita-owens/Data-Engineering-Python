#DOWNLOADS INTERNET FILE TO GOOGLE CLOUD BUCKET

import wget
import pandas
import os
from datetime import datetime
from google.cloud import storage
from google.cloud.storage import Client

url = os.environ['URL'] #URL of file
bucket_name = os.environ['BUCKET'] #Assumes bucket is already created
file_name = os.environ['FILE_NAME'] #What name to give to file once downloaded from internet
cf_path = '/tmp/{}'.format(file_name) #Cloud functions temporary directory
now_ts = datetime.today()

def import_file(request):

    # set storage client
    client = storage.Client()

    # get bucket & blobs
    bucket = client.get_bucket(bucket_name)
    blobs = client.list_blobs(bucket_name)

    # download the file to Cloud Function's tmp directory
    wget.download(url, cf_path)

    # set Blob
    blob = storage.Blob(file_name, bucket)
 
    # upload the file to GCS
    blob.upload_from_filename(cf_path)

    # Prints all files in bucket
    for blob in blobs:
        print(blob.name + " " + str(now_ts)) 
    
    #Need a return statement for Google Cloud function
    return 'OK'