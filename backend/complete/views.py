#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Blueprint, render_template, request, url_for, redirect, flash, send_file
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
import sqlalchemy
import sqlite3
from logging import Formatter, FileHandler
from .forms import *
from flask_login import login_required, current_user, logout_user
from controllers.database import pantry_database, shopping_list_database, user_database, favorite_recipe, reviews_database
from Models.validation import Reviews
import base64
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

views = Blueprint('views', __name__)


#db = SQLAlchemy(app)

# Automatically tear down SQLAlchemy.
'''
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()
'''

# Login required decorator.
'''
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap
'''
#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@views.route('/')
# @login_required
def home():
    return render_template('pages/HomePage.html',  user=current_user)

@views.route('/Recipes', methods=["POST", "GET"])
def about():
    object = pantry_database("instance\MainDB.db")
    if request.method == "GET":
        recipes= object.return_all_recipe_names()
        return render_template('pages/Recipes.html', recipelist=recipes)
    else:
        rname= request.form.get("recipename")
        #print(rname)
        recipesearch= object.get_similar_recipes(rname)
        return render_template('pages/Recipes.html', recipelist=recipesearch)

@views.route('/delete_account/<userid>', methods=["POST"])
def delete_account(userid):
    user_db = user_database("instance\MainDB.db")
    result = user_db.delete_user(userid)

    if result == "User deleted":
        # Log the user out and redirect to the home page
        logout_user()
        return redirect(url_for('views.home'))
    else:
        flash("Error deleting account.")
        return redirect(url_for('views.userprofile', userid=userid))

@views.route('/change_name/<userid>', methods=["POST"])
def change_name(userid):
    user_db = user_database("instance\MainDB.db")

    if request.method == 'POST':
        new_firstname = request.form.get("new_firstname")
        new_lastname = request.form.get("new_lastname")

        if new_firstname and new_lastname:
            user_db.change_name(userid, new_firstname, new_lastname)
            flash("Name changed successfully.")
        else:
            flash("Both first and last names are required.")

    return redirect(url_for('views.userprofile', userid=userid))

@views.route('/change_password/<userid>', methods=["POST"])
def change_password(userid):
    user_db = user_database("instance\MainDB.db")

    if request.method == 'POST':
        new_password = request.form.get("new_password")
        print(f"User ID: {userid}, New Password: {new_password}")

        if new_password:
            user_db.change_password(userid, new_password)
            flash("Password changed successfully.")
        else:
            flash("New password cannot be empty.")

    return redirect(url_for('views.userprofile', userid=userid))


@views.route('/add_favorite/<rname>', methods=["GET", "POST"])
def add_favorite(rname):
    user = current_user 
    if request.method == 'POST':
        object_favorite = favorite_recipe("instance\MainDB.db")
        object_favorite.add_favorite_recipe(rname, user.id)
        return redirect(url_for('views.userprofile', userid=user.id))
    else:
        pantry_object = pantry_database("instance\MainDB.db")
        image_data = pantry_object.get_recipe_image(rname)
        if image_data:
            image = image_data[0]
            image_data_base64 = base64.b64encode(image).decode('utf-8')
            return render_template('pages/Recipes.html', image_data_base64=image_data_base64)
    

@views.route('/remove_favorite/<recipe_name>', methods=["POST"])
def remove_favorite(recipe_name):
    user = current_user
    if request.method == 'POST':
        object_favorite = favorite_recipe("instance\MainDB.db")
        object_favorite.remove_favorite_recipe(user.id, recipe_name)

    return redirect(url_for('views.userprofile', userid=user.id))

@views.route('/get_recipe_image/<rname>', methods=["GET", "POST"])
def get_recipe_image(rname):
    pantry_object = pantry_database("instance\MainDB.db")
    image_data = pantry_object.get_recipe_image(rname)

    if image_data:
        image = image_data[0]
        image_data_base64 = base64.b64encode(image).decode('utf-8')
        return render_template('pages/Recipes.html', image_data_base64=image_data_base64)
    else:
        return 'Image not found', 404

    

        
@views.route('/RecipeInfo/<rname>', methods=["POST", "GET"])
def recipeinfo(rname):
    recipename = rname
    form = Reviews()
    reviews_db = reviews_database("instance\MainDB.db")
    if form.validate_on_submit():
        review_text = form.review.data
        user_id = current_user.id if current_user.is_authenticated else None
        reviews_db.add_review(user_id, review_text, recipename)
        return redirect(url_for('views.recipeinfo', rname=recipename))

    object = pantry_database("instance\MainDB.db")
    ingredients=object.get_recipe_info(recipename)
    image_data = object.get_recipe_image(rname)
    review_list = reviews_db.display_review(rname)
    image = image_data[0]
    image_data_base64 = base64.b64encode(image).decode('utf-8')

    return render_template('pages/RecipeInfo.html', ingredientlist=ingredients, Recipe=recipename, image_data_base64=image_data_base64, form=form, review_list=review_list)

@views.route('/userprofile/<userid>')
def userprofile(userid):
    object = user_database("instance\MainDB.db")
    favorite_recipe_instance = favorite_recipe("instance\MainDB.db")
    userinfo= object.get_user(userid)
    favorite_recipes = favorite_recipe_instance.display_favorite_recipe(userid)
    return render_template('pages/userprofile.html', item=userinfo, favorite_recipes=favorite_recipes)

@views.route('/useredit/<userid>')
def useredit(userid):
    object = user_database("instance\MainDB.db")
    userinfo= object.get_user(userid)
    return render_template('pages/useredit.html',item=userinfo)

@views.route('/shoplist/<userid>')
def shoppinglist(userid):
    object=shopping_list_database("instance\MainDB.db")
    listofingrients=object.display_shopping_list(userid)
    object = user_database("instance\MainDB.db")
    userinfo= object.get_user(userid)
    return render_template('pages/usershoppinglist.html',item=userinfo, shoplist=listofingrients)

@views.route('/newshoplist/<userid>/<rname>')
def generateshoplist(userid, rname):
    object=pantry_database("instance\MainDB.db")
    ingredientslist=object.get_recipe_info(rname)
    object= pantry_database("instance\MainDB.db")
    present=object.display_pantry(userid)
    object=shopping_list_database("instance\MainDB.db")
    for item in ingredientslist:
        object.add_item(userid, item)
    return shoppinglist(userid)

@views.route('/removeshoplist/<userid>/<removeingredient>')
def removeshoplistitem(userid, removeingredient):
    object=shopping_list_database("instance\MainDB.db")
    object.remove_item(userid,removeingredient)
    listofingrients=object.display_shopping_list(userid)
    return shoppinglist(userid)

@views.route('/pantry/<userid>', methods=["POST", "GET"])
def viewpantry(userid):
    object = user_database("instance\MainDB.db")
    userinfo= object.get_user(userid)
    object = pantry_database("instance\MainDB.db")
    ingredients= object.display_pantry(userid)
    autofill = object.ingredient_list()
    return render_template('pages/pantryprofile.html', item= userinfo, pantrylist=ingredients, ingr=autofill)

@views.route('/pantryadd/<userid>/', methods=["POST", "GET"])
def addtopantry(userid):
    object = pantry_database("instance\MainDB.db")
    ingredientt= request.form.get("ing")
    ingredientsinput = ingredientt.split()
    for item in ingredientsinput:
        object.insert_into_pantry(userid, item)
    return viewpantry(userid)
    
@views.route('/pantrydelete/<userid>/<ingredients>', methods=["POST", "GET"])
def remove_from_pantry(userid, ingredients):
        object= pantry_database("instance\MainDB.db")
        object.remove_from_pantry(userid,ingredients)
        return viewpantry(userid)

@views.route('/pantrysearch/<userid>', methods=["POST", "GET"])
def pantrysearch(userid):
        object= pantry_database("instance\MainDB.db")
        Recipesfrompantry= object.recommend_recipes(userid)
        return render_template('pages/pantryRecipes.html',recipelist=Recipesfrompantry)




# @views.route('/reviews', methods=['GET', 'POST'])
# def reviews():
#     form = Reviews()
#     if form.validate_on_submit():
#         return "Success"
#     return render_template("pages/RecipeInfo.html", form=form)


# Error handlers.
@views.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@views.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

# if not views.debug:
#     file_handler = FileHandler('error.log')
#     file_handler.setFormatter(
#         Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
#     )
#     views.logger.setLevel(logging.INFO)
#     file_handler.setLevel(logging.INFO)
#     views.logger.addHandler(file_handler)
#     views.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    views.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
