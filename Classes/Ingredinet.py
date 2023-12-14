import sqlite3
import json

def from_json_to_sql(path, id):
    try:
        with open(path, "r") as infile:
            data = json.load(infile)
            for ingredient in data:
                if ingredient.get("Ingredient ID") == id:
                    return ingredient.get("Ingredient")
            return f"No ingredient found with this id: {id}"
    except FileNotFoundError:
        return f"File not found: {path}"
    except json.JSONDecodeError:
        return f"Error decoding json in file: {path}"


class Ingredients:
    def __init__(self, ingredient_name, ingredient_category):
        self.ingredient_name = ingredient_name
        self.ingredient_category = ingredient_category

    def get_ingredient_from_database(self, database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        data = cursor.execute('select * from Ingredient') 
        # then print the ingredients
        for row in data:
            print(row)
        connection.commit()
        connection.close()

    def delete_ingredient(self, connection, id):
        cursor = connection.cursor()
        cursor.execute('delete from Ingredient where Ingredient_id = ?', (id))
        connection.commit()

Ingredient_object = Ingredients('Salt', 'Seasoning')
database_name = "Tasty.db"
Ingredient_object.Get_Ingredient_from_database("Tasty.db")
connection = sqlite3.connect(database_name)
Ingredient_object.Delete_Ingredient(connectio, 1)
connection.close()

