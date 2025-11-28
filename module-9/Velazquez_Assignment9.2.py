import requests
response = requests.get('https://swapi.dev/api/planets/2/')

import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
jprint(response.json())