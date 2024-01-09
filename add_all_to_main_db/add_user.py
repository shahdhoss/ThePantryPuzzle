import sqlite3

connection = sqlite3.connect("instance/MainDB.db")
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS User')

table = '''CREATE TABLE User (
                id VARCHAR(36) PRIMARY KEY,
                email VARCHAR(255),
                password VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                isChef VARCHAR(255) DEFAULT 'off'
            )'''
cursor.execute(table)

connection.commit()
connection.close()
