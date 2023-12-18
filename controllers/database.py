import sqlite3


class database_base_model:
    def __init__(self, database_name):
        self.database_name = database_name
    def establish_connection(self):
        self.connection = sqlite3.connect(self.database_name)
    def cursor(self):
        return self.connection.cursor()
    def close(self):
        return self.connection.close()
    def commit(self):
        return self.connection.commit()


class user_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    
    def create_user(self, user_id, email, password, first_name, last_name, is_chef):
        query = 'insert into User values (?, ?, ?, ?, ?, ?)'
        self.cursor().execute(query, (user_id, email, password, first_name, last_name, is_chef))

    def find_user(self, user_id):
        query = 'select * from User where id = ?'
        data = self.cursor().execute(query, (user_id,))
        if data.fetchone() is None:
            return False
        return True
        
    def delete_user(self, user_id):
        found = self.find_user(user_id)
        if found:
            query = 'delete from User where id = ?'
            self.cursor().execute(query, (user_id,))
            return "User deleted"
        return "User not found"

    def tuple_to_dict(self, user_tuple):
        user_info = user_tuple.fetchone()
        if user_info:
            dictionary = {
                "Id": user_info[0],
                "Email": user_info[1],
                "Password" :user_info[2],
                "First name" : user_info[3],
                "Last name" : user_info[4]
            }
            return dictionary
        else:
            return None
    
    def fetch_all(self):
        data = self.cursor().execute('select * from User')
        return data.fetchall()
        


db_path = "D:\\SWE - project\\ThePantryPuzzle\\instance\\MainDB.db"
objectt = database_base_model(db_path)

user_object = user_database(db_path)
# user_object.create_user(2, 'q@gmail.com', '1233', 'hamada', 'galal', 'off')

# print(user_object.tuple_to_dict(data))

# print(user_object.get_user_by_id(2))

# print(user_object.delete_user(2))

print(user_object.fetch_all())
user_object.commit()
user_object.close()
print('done')