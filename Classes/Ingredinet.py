import sqlite3

class Ingredients:
    def __init__(self, Ingredient_Name, Ingredient_Category):
        self.Ingredient_Name = Ingredient_Name
        self.Ingredient_Category = Ingredient_Category

    def Get_Ingredient_from_database(database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        data = cursor.execute('select * from Ingredient') 
        # then print the ingredients
        for row in data:
            print(row)
        connection.commit()
        connection.close()

    def Delete_Ingredient(connection, id):
        cursor = connection.cursor()
        cursor.execute('delete from Ingredient where Ingredient_id = ?', (id))
        connection.commit()

g = Ingredient("garlic", "veg")
g.Get_Ingredient_from_database("Tasty.bd")
