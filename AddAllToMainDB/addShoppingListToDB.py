import sqlite3

connection = sqlite3.connect('instance/MainDB.db')
cursor = connection.cursor()

table = '''CREATE TABLE ShopList (
                ID INTEGER PRIMARY KEY,
                UserID INTEGER,
                IngredientName varchar(255),
                FOREIGN KEY(UserID) REFERENCES User(id),
                FOREIGN KEY(IngredientName) REFERENCES Ingredient(Ingredient_name)
            )'''

cursor.execute(table)

connection.commit()
connection.close()
print('done')