import json
import requests         
APP_ID = 'b3538033'
APP_KEY = '9de8443eb0e0bb0c320001cfced73adf	'
ENDPOINT_URL = 'https://api.edamam.com/api/recipes/v2'
params = {
    'q': 'cake',
    'app_id': APP_ID,
    'app_key': APP_KEY,
    'type': 'public'
}

response = requests.get(ENDPOINT_URL, params=params)
food_list={}
temp_list=[]
if response.status_code == 200:
    data = response.json()
    for hit in data['hits']:
        for recipe in hit['recipe']['ingredients']:
            temp_list.append(recipe['food'])
            food_list[hit['recipe']['label']]=temp_list
        temp_list=[]

# json_object = json.dumps(food_list, indent=4)
# with open("F:\downloads\cake_queryIngredients.json", "w") as outfile:
#     outfile.write(json_object)