import flask
import sqlite3

class database:
    def __init__(self,databaseName):
        self.databaseName=databaseName
    def establish_connection(self):
        self.connection = sqlite3.connect(self.databaseName)
    def cursor(self):
        return self.connection.cursor()
    def close(self):
        return self.connection.close()
    def commit(self):
        return self.connection.commit()


