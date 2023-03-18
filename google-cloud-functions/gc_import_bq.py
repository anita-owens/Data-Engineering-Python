"""pandas==1.5.2
pandas-gbq==0.18.1
google-cloud-storage==2.7.0
wget==3.2"""



import os
from datetime import datetime
from google.cloud import storage
from google.cloud.storage import Client
from google.cloud import bigquery

def bq_load(request):
  # Construct a BigQuery client object.
    client = bigquery.Client()
    now_ts = datetime.today()

    # TODO(developer): Set table_id to the ID of the table to create.
    #table_id = "my-project-39149-2020.cloud_functions.gcf_data"
    table_id = os.environ.get('TABLE_ID')

    # Set the encryption key to use for the destination.
    # TODO: Replace this key with a key you have created in KMS.
    # kms_key_name = "projects/{}/locations/{}/keyRings/{}/cryptoKeys/{}".format(
    #     "cloud-samples-tests", "us", "test", "test"
    # )
    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        # The source format defaults to CSV, so the line below is optional.
        source_format=bigquery.SourceFormat.CSV,)
    #uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"
    #uri = "https://storage.cloud.google.com/gcf-data-sink/college-majors.csv"
    uri = os.environ.get('URI')
    load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)  # Make an API request.
    load_job.result()  # Waits for the job to complete.
    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))
    return 'OK ' + str(now_ts)