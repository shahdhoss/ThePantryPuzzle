import sqlite3

connection = sqlite3.connect("D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db")
cursor = connection.cursor()
drop_table = 'drop table Recipes'
table = 'create table Recipes (Recipe_name varchar(255), Ingredient varchar(255))'

cursor.execute(table)


connection.commit()
connection.close()