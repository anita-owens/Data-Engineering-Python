#https://stackoverflow.com/questions/49541026/how-do-i-unzip-a-zip-file-in-google-cloud-storage
import io
from io import BytesIO
from zipfile import ZipFile, is_zipfile
from google.cloud import storage

from google.cloud.storage import Client
import pandas as pd
import pandas_gbq
from datetime import datetime

def zipextract():
    bucketname = 'gcf-data-sink'
    zipfilename_with_path = 'archive.zip' # if the file is gs://mybucket/path/file.zip

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketname)

    destination_blob_pathname = zipfilename_with_path
        
    blob = bucket.blob(destination_blob_pathname)
    zipbytes = io.BytesIO(blob.download_as_bytes())

    #if is_zipfile(zipbytes):
    with ZipFile(zipbytes, 'r') as myzip:
        for contentfilename in myzip.namelist():
            contentfile = myzip.read(contentfilename)
            blob = bucket.blob("unzipped_contents" + "/" + contentfilename)
            blob.upload_from_string(contentfile)
            if ".csv" in blob.name:
                file_data = blob.download_as_bytes()
                df = pd.read_csv(BytesIO(file_data), encoding='latin-1')
                return df
                

def load(request):
    table_id = 'cloud_functions.sales_data'
    project_id =  os.environ.get['PROJECT_ID']
    data = zipextract()
    nrows = data.shape[0]
    ncols = data.shape[1]
    pandas_gbq.to_gbq(data, table_id, project_id=project_id, if_exists='replace')
    print("Finished at {}. Uploaded {} rows and {} columns.".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S"), nrows, ncols))
    return 'Executed Successfully ' + str(datetime.today())