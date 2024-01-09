import sqlite3

connection = sqlite3.connect("ThePantryPuzzle\instance\MainDB.db")                                 
cursor = connection.cursor() 

# with open('F:\downloads\egetables_text.json', 'r') as json_file:     #add ur own json file path
#     file = json.load(json_file)

# to insert into the recipes table using the json file
def insert_recipes_intotable(file):                                  
    for recipe in file:
        templist=file[recipe]
        for ingredientt in templist: 
            connection.execute("insert into Recipes (Recipe_name, Ingredient) VALUES (?, ?)", (str(recipe),str(ingredientt)))
            connection.commit()


def insert_instructions_intotable(file):
    for recipee in file:
        instructions=file[recipee]
        for instruction in instructions:
            connection.execute("insert into Instructions (Recipe_name, Instruction) VALUES (?,?)", (str(recipee), str(instruction)))
            connection.commit()

def insert_quantities_intotable(file):
    for line in file:
        quantities=file[line]
        for quantity in quantities:
            connection.execute("insert into Quantities (Recipe_name, Quantity) VALUES(?,?)",(str(line),str(quantity)))
            connection.commit()


# #use when testing whether the database got the data or not::
# cursor.execute("select count(*) from User where id=12 and isChef = 'on' ")                             #change the Instructions with Quantites if u want display the quantites table     
cursor.execute("select * from Chef")
mydata=cursor.fetchall()
#fetch all function gets whats stored in the database
for i in mydata:             
    print(i)

# def get_recipeInfo(RecipeN):
#         cursor.execute("Select Ingredient from Recipes where Recipe_name = ?", ([RecipeN]))
#         ingredients=cursor.fetchall()
#         return ingredients

# ingredientss=get_recipeInfo("Meat Loaf")    #choose the recipe that u want to get the ingredients for
# for ingredient in ingredientss:
#     print(ingredient)

connection.close()