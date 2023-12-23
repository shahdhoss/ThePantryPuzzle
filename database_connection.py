import sqlite3
import json

connection = sqlite3.connect("instance\\MainDB.db", timeout=5000)                                  #add the database name as it is saved on ur laptop
cursor = connection.cursor() 

# with open("D:\\Downloads\\chicken_queryIngredients.json", 'r') as json_file:     #add ur own json file path
#     file = json.load(json_file)

# to insert into the recipes table using the json file
def insert_recipes_intotable(file):                                  
    for recipe in file:
        templist=file[recipe]
        for ingredientt in templist: 
            connection.execute("insert into Recipes (Recipe_name, Ingredient) VALUES (?, ?)", (str(recipe),str(ingredientt)))
            connection.commit()

# #use when testing whether the database got the data or not::
# insert_recipes_intotable(file)
cursor.execute("select * from Recipes")       
mydata=cursor.fetchall()
#fetch all function gets whats stored in the database

connection.close()

