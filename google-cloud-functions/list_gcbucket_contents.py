from google.cloud.storage import Client
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