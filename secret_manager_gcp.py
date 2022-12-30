import os
from google.cloud import secretmanager
# Create the Secret Manager client.
client = secretmanager.SecretManagerServiceClient()

# The secret_name should match the name of the secret you created in # the Secret Manager console
#Server name value = 'server123'
secret_name = "server"

# Your GCP project id - As Environment variable
project_id = os.environ["PROJECT_ID"]
# Build the resource name of the secret version.
request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
response = client.access_secret_version(request)
# Access the secret version.
secret_payload = response.payload.data.decode("UTF-8")

#Test output returns value: $server123 and does not print to log
def get_secret(request):
    return secret_payload

#Test output returns value: $server123 and logs textPayload: "Function execution took 2467 ms, finished with status code: 200"
def get_secret(request):
    return secret_payload
    server_name = secret_payload

#Test output returns value: $server123 and logs textPayload: "Function execution took 2750 ms, finished with status code: 200"
def get_secret(request):
    return secret_payload
    server_name = secret_payload
    print(server_name)
