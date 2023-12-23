import json
import requests         
APP_ID = 'ecaee9c8'
APP_KEY = '7d375fc3797be0325bcc8a0decb1a623'
ENDPOINT_URL = 'https://api.edamam.com/api/recipes/v2'
params = {
    'q':'chicken',
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
        # temp_list.append(hit['recipe']['images']['REGULAR']['url'])    #for getting the pictures
        # food_list[hit['recipe']['label']]=temp_list
        # temp_list=[]


        # for recipe in hit['recipe']['instructionLines']:     #for getting recipe steps and instructions
        #     temp_list.append(recipe)
        #     food_list[hit['recipe']['label']]=temp_list
        # temp_list=[]

        # for recipe in hit['recipe']['ingredients']:           # for getting the measurement of every ingredient
        #     temp_list.append(recipe['text'])
        #     food_list[hit['recipe']['label']]=temp_list
        # temp_list=[]

        # for recipe in hit['recipe']['ingredients']:           #for getting the recipe name and their ingredients 
        #     temp_list.append(recipe['food'])
        #     food_list[hit['recipe']['label']]=temp_list
        # temp_list=[]

# print(food_list)
# json_object = json.dumps(food_list, indent=4)
# with open("F:\downloads\cake_queryIngredients.json", "w") as outfile:
#     outfile.write(json_object)