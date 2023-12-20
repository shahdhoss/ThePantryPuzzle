from .extensions import db
import sqlite3
import json
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    isChef = db.Column(db.String, default='off')

class Ingredients:
    def get_ingredient_from_database(self, database_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        data = cursor.execute('select * from Ingredient where Ingredient_name is not null') 
        ingredient_list = []
        # then print the ingredients
        for row in data:
            ingredient_list.append(row)
        connection.commit()
        connection.close()
        return ingredient_list

    def delete_ingredient(self, connection, ingredient_name):
        cursor = connection.cursor()
        cursor.execute('delete from Ingredient where Ingredient_name = ?', (ingredient_name))
        connection.commit()

    def fetch_nutrients_from_database(self, database_name, ingredient_name):
        connection = sqlite3.connect(database_name)
        cursor = connection.cursor()
        cursor.execute('select Nutrients from Nutrients where Ingredient_name = ?', (ingredient_name,))
        data = cursor.fetchone()
        connection.commit()
        connection.close()
        return data

    def display_nutrients(self, ingredient_name, database_name):
        ingredient_list = self.get_ingredient_from_database(database_name)
        for tuple_ingredient in ingredient_list:
            for ingredient in tuple_ingredient:
                if ingredient == ingredient_name:
                    nutrient_data = self.fetch_nutrients_from_database(database_name, ingredient)
                    return nutrient_data[0]
        return "Ingredient not found." 
