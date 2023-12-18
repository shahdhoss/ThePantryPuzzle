import sqlite3


class database_base_model:
    def __init__(self,database_name):
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
    def create_user(self, user_id, email, password, first_name, last_name, is_chef):
        query = 'insert into User values (?, ?, ?, ?, ?, ?)'
        self.cursor().execute(query, (user_id, email, password, first_name, last_name, is_chef))
    def get_user_by_id(self, user_id):
        query = 'select * from User where id = ?'
        data = self.cursor().execute(query, (user_id))
        return data.fetchone()
    
    def delete_user(self, user_id):
        query = 'delete from User where id = ?'
        self.cursor().execute(query, user_id)

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


objectt = database_base_model("ThePantryPuzzle\\instance\\MainDB.db")

objectt.establish_connection()
cursor = objectt.cursor()


user_object = user_database(objectt)

print(user_object.get_user_by_id(1))

# print(data.fetchone()[1])
objectt.commit()
objectt.close()
print('done')