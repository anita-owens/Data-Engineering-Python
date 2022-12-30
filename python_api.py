# Import requests package
import requests

api_key = '72bc447a'
movie_title = 'the+social+network'

# Assign URL to variable: url
#url = 'http://www.omdbapi.com?apikey=72bc447a&t=the+social+network'
url = 'http://www.omdbapi.com?apikey={api_key}&t={movie_title}'
#url = "http://www.omdbapi.com?apikey={api_key}&t={movie_title}"

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)
