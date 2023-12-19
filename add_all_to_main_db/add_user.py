import sqlite3
import json

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()
table = '''CREATE TABLE User (
                id INTEGER PRIMARY KEY,
                email VARCHAR(255),
                password VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                isChef VARCHAR(255) DEFAULT 'off'
            )'''

cursor.execute(table)