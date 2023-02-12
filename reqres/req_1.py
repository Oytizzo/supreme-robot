# import requests module
import requests
from pprint import pprint
import json

# Making a get request
# response = requests.get('https://api.github.com')
response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities')

# print response
print(response.json())
pprint(response.json(), indent=4, depth=1)
