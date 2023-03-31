import requests

base_url = 'https://api.datamuse.com/words'

parameters = {"rel_rhy":"single"}

response = requests.get(base_url, parameters)
print(response)

rhyme_json = request.json()


for i in rhyme_json[0:3]:
 print(i['word'])