"""
#Requirements Text
google-cloud-storage==2.7.0"""

import os
from datetime import datetime
from google.cloud import storage
from google.cloud.storage import Client


def delete_file(request):

    client = storage.Client()
    bucket = storage.Bucket(client, 'gcf-data-sink')

    str_files_to_delete_on_gcs = ['college-majors.csv']

    #Remove multiple files but keep folder
    for str_file in str_files_to_delete_on_gcs:
      blob = bucket.blob(str_file)
      blob.delete()
    
    #Need a return statement for Google Cloud function
    return 'OK ' + str(datetime.today())