"""requests==2.28.1
pandas==1.5.2
google-cloud-storage==2.7.0
requests==2.28.1
wget==3.2
pathlib==1.0.1
zipfile38==0.0.3"""


#https://stackoverflow.com/questions/49541026/how-do-i-unzip-a-zip-file-in-google-cloud-storage
import io
from zipfile import ZipFile, is_zipfile
from google.cloud import storage
from datetime import datetime

def zipextract(request):
    bucketname = 'gcf-data-sink'
    zipfilename_with_path = 'archive.zip' # if the file is gs://mybucket/path/file.zip

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucketname)
    print("Step 1 Completed")

    destination_blob_pathname = zipfilename_with_path
        
    blob = bucket.blob(destination_blob_pathname)
    zipbytes = io.BytesIO(blob.download_as_bytes())

    print("Step 2 Unzipping")
    with ZipFile(zipbytes, 'r') as myzip:
        for contentfilename in myzip.namelist():
            contentfile = myzip.read(contentfilename)
            #blob = bucket.blob(zipfilename_with_path + "/" + contentfilename)
            blob = bucket.blob("unzipped_folder" + "/" + contentfilename)
            blob.upload_from_string(contentfile)
        return 'Executed Successfully at ' + str(datetime.today())
