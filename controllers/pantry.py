import database

mydatabase = database.database_base_model("ThePantryPuzzle\instance\MainDB.db")
mydatabase.establish_connection()

def l_tuple_to_list(tuplee):                       #function to change a list of tuples to a normal list
    listt =[]
    for item in tuplee:
        for itemm in item:
            listt.append(itemm)        # all the ingredients are now in a normal list
    return listt

def get_recipe_info(recipe_n):
        cursor=mydatabase.cursor().execute("Select Ingredient from Recipes where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        return ingredients

def return_all_recipe_names():
        cursor=mydatabase.cursor().execute("Select Distinct Recipe_name from Recipes")
        recipe_t=cursor.fetchall()           #recipe list of tuples
        recipe_l=Ltuple_toList(recipe_t)      #list of recipe names
        return recipe_l

def return_ingredient_list():
    cursor=mydatabase.cursor().execute("Select Distinct Ingredient from Recipes")
    ingredient_list_of_tuples=cursor.fetchall()                 #the database returns a list of tuples.
    ingredients_list=l_tuple_to_list(ingredient_list_of_tuples)
    return ingredients_list

Recipes_and_Ingredients_Dict={}
recipe_l = return_all_recipe_names()
# dictionary containing the recipe name and all its ingredients in a list
for recipe in recipe_l:
    ingredients_t=get_recipe_info(recipe)
    ingredients_t=l_tuple_to_list(ingredients_t)
    Recipes_and_Ingredients_Dict[recipe]=ingredients_l

IngredientsList=return_IngredientList()
class pantry():
    def __init__(self):
        self.pantry_list=[]

    def add_ingredient_to_pantry(self,ingredientt):
        for ingred1 in IngredientsList:
            if ingredientt==ingred1:
                self.pantry_list.append(ingredientt)
    # no need for returning a message that says the ingredient is not found, might switch it up to something else later

    def remove_ingredient_from_pantry(self, ingred):
        for ingred2 in self.pantry_list:
            if ingred == ingred2:
                self.pantry_list.remove(ingred)

    def display_pantry(self):
        for i in self.pantry_list:
            print(i)

    def recommend_recipes(self):
        recommendedrecipes = []
        for key in Recipes_and_Ingredients_Dict:
            available=[]
            navailable=[]
            for ingre1 in Recipes_and_Ingredients_Dict[key]:
                    for ingre2 in self.pantry_list:
                        if ingre1==ingre2:
                            available.append(ingre1)    
                    if ingre1 not in self.pantry_list:
                        navailable.append(ingre1)
            if len(available)==len(Recipes_and_Ingredients_Dict[key]) :       #if all the ingredients are available in the pantry
                recommendedrecipes.append(key)
            if len(Recipes_and_Ingredients_Dict[key])>=3:                     #if all are available except for one or two ingredients
                if 0<len(navailable)<=2:
                    recommendedrecipes.append(key)
        return recommendedrecipes

mypantry=pantry()
temp=["fruit cocktail","walnuts","fat-free milk","pound cake","Salt","Kosher salt","olive oil","garlic","carrots","dried oregano","dried basil","vegetables","honey"
    "unsalted butter","sugar","rice vinegar"]
for i in temp:
    mypantry.add_ingredient_to_pantry(i)
print(mypantry.recommend_recipes())
