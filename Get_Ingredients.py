import requests
import json
import ipdb

APP_ID = 'df476c39'
APP_KEY = '879f8b246313c4c27dcf09a547c1b393'
ENDPOINT_URL = 'https://api.edamam.com/api/recipes/v2'

params = {
    'q': 'meat',
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'type': 'public'
}

response = requests.get(ENDPOINT_URL, params=params)

if response.status_code == 200:
    data = response.json()
    ingredients_list = []
    for hit in data['hits']:
        for recipe in hit['recipe']['ingredients']:
            ingredient_name = recipe['food']
            ingredients_list.append({
                "Ingredient Name": ingredient_name,
            })
            
ipdb.set_trace()
json_object = json.dumps(ingredients_list, indent = 1)

with open("meat.json", "w") as outfile:
    outfile.write(json_object)

print('done')
