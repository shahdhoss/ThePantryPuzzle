import database    
mypantry=database.pantry_database("D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db")

Recipes_and_Ingredients_Dict={}
recipe_l = mypantry.return_all_recipe_names()

# dictionary containing the recipe name and all its ingredients in a list
for recipe in recipe_l:
    ingredients_t=mypantry.get_recipe_info(recipe)
    ingredients_l=mypantry.l_tuple_to_list(ingredients_t)
    Recipes_and_Ingredients_Dict[recipe]=ingredients_l

IngredientsList=mypantry.return_ingredient_list()
class pantry():
    def _init_(self):
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
