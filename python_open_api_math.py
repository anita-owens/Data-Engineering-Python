import requests

#Call the API and verify a response
response = requests.get("http://numbersapi.com/random/math")
print(response.status_code)

#Print random fact
print(response.text)