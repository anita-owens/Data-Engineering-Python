import pandas
import pandas_gbq
import os
from datetime import datetime
from google.cloud import storage
from google.cloud.storage import Client
import wget
from google.cloud import bigquery

url = os.environ['URL']
bucket_name = os.environ['BUCKET'] #without gs://
file_name = os.environ['FILE_NAME']

cf_path = '/tmp/{}'.format(file_name)

project_id = os.environ.get('PROJECT_ID')
table_id = os.environ.get('TABLE_ID')
now_ts = datetime.today()

def import_file(request):

    # set storage client
    client = storage.Client()

    # get bucket
    bucket = client.get_bucket(bucket_name)

    # download the file to Cloud Function's tmp directory
    wget.download(url, cf_path)

    # set Blob
    blob = storage.Blob(file_name, bucket)
 
    # upload the file to GCS
    blob.upload_from_filename(cf_path)
    #return cf_path
    #print("""This Function was triggered by messageId {} published at {}""".format(context.event_id, context.timestamp))

    #load the blob
    file_data = blob.download_as_string()
    return file_data
    df = pandas.read_csv(file_data, encoding='utf-8', sep=",")
    #df = pandas.DataFrame() #remove this one
    pandas_gbq.to_gbq(df, table_id, project_id=projectid, if_exists='replace')
    return 'Success ' + str(now_ts)