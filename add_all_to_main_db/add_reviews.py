import sqlite3

create_table = """
    create table Reviews(
        User_ID int,
        comment varchar(255)
    )
"""
drop_table = "drop table Reviews"

add_recipe = "alter table Reviews add Recipe_Name varchar(50)"
connection = sqlite3.Connection("instance\MainDB.db")
cursor = connection.cursor()

cursor.execute(add_recipe)

connection.commit()
connection.close()