import os
from google.cloud import secretmanager
# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()
# The secret_name should match the name of the secret you created in # the Secret Manager console
secret_name = "server"
# Your GCP project id
project_id = os.environ["PROJECT_ID"]
# Build the resource name of the secret version.
request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
response = client.access_secret_version(request)
# Access the secret version.
secret_payload = response.payload.data.decode("UTF-8")


def get_secret(request):
    return secret_payload
    server_name = secret_payload
    print(server_name)
