import sqlite3

class database_base_model:
    def l_tuple_to_list(self,tuplee):                       #function to change a list of tuples to a normal list
        listt =[]
        for item in tuplee:
            for itemm in item:
                listt.append(itemm)        # all the ingredients are now in a normal list
        return listt    
    def __init__(self, database_name):
        self.database_name = database_name
    def establish_connection(self):
        self.connection = sqlite3.connect(self.database_name, timeout = 5000)
    def cursor(self):
        return self.connection.cursor()
    def close(self):
        return self.connection.close()
    def commit(self):
        return self.connection.commit()
    def fetch_all(self, table_name):
        data = self.cursor().execute(f'select * from {table_name}')
        return data.fetchall()

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
    
    def get_user(self, user_id):
        query = f'Select * from User where id = {user_id}'
        cursor=self.cursor().execute(query)
        data=cursor.fetchall()                          
        data=self.l_tuple_to_list(data)                
        return data

    def delete_user(self, user_id):
        found = self.find_user(user_id)
        if found:
            query = 'delete from User where id = ?'
            self.cursor().execute(query, (user_id,))
            self.commit()
            return "User deleted"
        return "User not found"

    def change_password(self, user_id, new_password):
        query = 'update User set password = ? where id = ?'
        try:
            self.cursor().execute(query, (new_password, user_id))
            self.commit()
        except Exception as e:
            print(f"Error changing password: {e}")
            # Add additional logging or raise the exception if needed
        finally:
            self.close()
    
    def change_name(self, user_id, newfirstname, newlastname):
        query = 'update User set first_name = ?, last_name = ? where id = ?'
        try:
            self.cursor().execute(query, (newfirstname, newlastname, user_id))
            self.commit()
        except Exception as e:
            print(f"Error changing name: {e}")
        finally:
            self.close()

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
    
class favorite_recipe(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()

    def add_favorite_recipe(self, recipe_name, user_id):
        query = 'insert into Favorite values (?, ?)'
        try:
            self.cursor().execute(query, (user_id, recipe_name))
            self.commit()
        except Exception as e:
            print(f"Error adding favorite recipe: {e}")
        finally:
            self.close()

    
    # returns a list of the user's favorite recipe
    def display_favorite_recipe(self, id_user):
        query = 'select Recipe_name from Favorite where id = ?'
        data = self.cursor().execute(query, (id_user,))
        list_recipes = []
        for recipe in data.fetchall():
            list_recipes.append(recipe[0])
        return list_recipes

    def remove_favorite_recipe(self, user_id, recipe_name):
        query = 'delete from Favorite where id = ? and Recipe_name = ?'
        try:
            self.cursor().execute(query, (user_id, recipe_name))
            self.commit()
        except Exception as e:
            print(f"Error removing favorite recipe: {e}")
            # Add additional logging or raise the exception if needed
        finally:
            self.close()


class shopping_list_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()
    
    def add_item(self, user_id, ingredient_name):
        query = 'insert into ShopList values (?, ?)'
        try:
            self.cursor().execute(query, (user_id, ingredient_name))
            self.commit()
        except Exception as e:
            print(f"Error adding shopping item: {e}")
        finally:
            self.close()
    
    def display_shopping_list(self, user_id):
        query = 'select * from ShopList where UserID = ?'
        data = self.cursor().execute(query, (user_id,))
        ingredients_tuple = data.fetchall()
        list_ingredients = []
        for ingredient in ingredients_tuple:
            list_ingredients.append(ingredient[1])
        return list_ingredients
    
    def remove_item(self, user_id, ingredient_name):
        query = 'delete from ShopList where UserID = ? and IngredientName = ?'
        try:
            self.cursor().execute(query, (user_id, ingredient_name))
            self.commit()
        except Exception as e:
            print(f"Error removing shopping item: {e}")
            # Add additional logging or raise the exception if needed
        finally:
            self.close()

        
class pantry_database(database_base_model):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.establish_connection()

    def l_tuple_to_list(self,tuplee):                       #function to change a list of tuples to a normal list
        listt =[]
        for item in tuplee:
            for itemm in item:
                listt.append(itemm)        # all the ingredients are now in a normal list
        return listt
    
    def return_all_recipe_names(self):
        cursor=self.cursor().execute("Select Distinct Recipe_name from Recipes")
        recipe_t=cursor.fetchall()                            #recipe list of tuples
        recipe_l=self.l_tuple_to_list(recipe_t)                #list of recipe names
        return recipe_l
    
    def get_similar_recipes(self, recipename):
        cursor=self.cursor().execute("SELECT DISTINCT Recipe_name FROM Recipes WHERE Recipe_name LIKE ?", ('%' + recipename + '%',))
        recipe_t=cursor.fetchall()                          
        recipe_l=self.l_tuple_to_list(recipe_t)                
        return recipe_l
    
    def get_recipe_info(self,recipe_n):
        cursor=self.cursor().execute("Select Ingredient from Recipes where Recipe_name = ?", ([recipe_n]))
        ingredients=cursor.fetchall()
        ingredients=self.l_tuple_to_list(ingredients) 
        return ingredients
    
    def return_ingredient_list(self):
        cursor=self.cursor().execute("Select Distinct Ingredient from Recipes")
        ingredient_list_of_tuples=cursor.fetchall()                 #the database returns a list of tuples.
        ingredients_list=self.l_tuple_to_list(ingredient_list_of_tuples)
        return ingredients_list