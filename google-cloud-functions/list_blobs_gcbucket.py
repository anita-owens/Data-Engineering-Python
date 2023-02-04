"""google-cloud-storage==2.7.0
pandas==1.5.2
pandas-gbq==0.18.1"""

from google.cloud.storage import Client
#import logging
#import pandas
#import pandas_gbq
from google.cloud import storage

def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    #bucket_name = "sql_datasets"
    bucket_name = "gcf-data-sink"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    # Note: The call returns a response only when the iterator is consumed.
    for blob in blobs:
        print(blob.name)
    
    return "ok"