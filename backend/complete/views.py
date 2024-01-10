#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Blueprint, render_template, request, url_for, redirect, flash, send_file, Flask
import logging
import sqlalchemy
import sqlite3
from logging import Formatter, FileHandler
from .forms import *
from flask_login import login_required, current_user, logout_user
from controllers.database import pantry_database, shopping_list_database, user_database, favorite_recipe, reviews_database, dietary_prefernces_database, chef_database
import base64
from models.validation import Reviews
from urllib.parse import quote
from PIL import Image
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

views = Blueprint('views', __name__)

database_path = "ThePantryPuzzle\\instance\\MainDB.db"
user_profile = 'views.userprofile'
Page_Recipes = 'pages/Recipes.html'

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@views.route('/')
# @login_required
def home():
    return render_template('pages/HomePage.html',  user=current_user)

@views.route('/FAQs')
# @login_required
def faqs():
    return render_template('pages/FAQs.html',  user=current_user)

@views.route('/Recipes', methods=["POST", "GET"])
def about():
    objectt = pantry_database(database_path)
    if request.method == "GET":
        recipes= objectt.return_all_recipe_names()
        return render_template(Page_Recipes, recipelist=recipes)
    else:
        rname= request.form.get("recipename")
        #print(rname)
        recipesearch= objectt.get_similar_recipes(rname)
        return render_template(Page_Recipes, recipelist=recipesearch)

@views.route('/delete_account/<userid>', methods=["POST"])
def delete_account(userid):
    user_db = user_database(database_path)
    result = user_db.delete_user(userid)

    if result == "User deleted":
        # Log the user out and redirect to the home page
        logout_user()
        return redirect(url_for('views.home'))
    else:
        flash("Error deleting account.")
        return redirect(url_for(user_profile, userid=userid))

@views.route('/change_name/<userid>', methods=["POST"])
def change_name(userid):
    user_db = user_database(database_path)

    if request.method == 'POST':
        new_firstname = request.form.get("new_firstname")
        new_lastname = request.form.get("new_lastname")

        if new_firstname and new_lastname:
            user_db.change_name(userid, new_firstname, new_lastname)
            flash("Name changed successfully.")
        else:
            flash("Both first and last names are required.")

    return redirect(url_for(user_profile, userid=userid))

@views.route('/change_password/<userid>', methods=["POST"])
def change_password(userid):
    user_db = user_database(database_path)

    if request.method == 'POST':
        new_password = request.form.get("new_password")
        print(f"User ID: {userid}, New Password: {new_password}")

        if new_password:
            user_db.change_password(userid, new_password)
            flash("Password changed successfully.")
        else:
            flash("New password cannot be empty.")

    return redirect(url_for(user_profile, userid=userid))


@views.route('/add_favorite/<rname>', methods=["GET", "POST"])
def add_favorite(rname):
    user = current_user 
    if request.method == 'POST':
        objectt_favorite = favorite_recipe(database_path)
        objectt_favorite.add_favorite_recipe(rname, user.id)
        return redirect(url_for(user_profile, userid=user.id))
    else:
        pantry_objectt = pantry_database(database_path)
        image_data = pantry_objectt.get_recipe_image(rname)
        if image_data:
            image = image_data[0]
            image_data_base64 = base64.b64encode(image).decode('utf-8')
            return render_template(Page_Recipes, image_data_base64=image_data_base64)
    

@views.route('/remove_favorite/<recipe_name>', methods=["POST"])
def remove_favorite(recipe_name):
    user = current_user
    if request.method == 'POST':
        objectt_favorite = favorite_recipe(database_path)
        objectt_favorite.remove_favorite_recipe(user.id, recipe_name)

    return redirect(url_for(user_profile, userid=user.id))

@views.route('/get_recipe_image/<rname>', methods=["GET", "POST"])
def get_recipe_image(rname):
    pantry_objectt = pantry_database(database_path)
    image_data = pantry_objectt.get_recipe_image(rname)

    if image_data:
        image = image_data[0]
        image_data_base64 = base64.b64encode(image).decode('utf-8')
        return render_template(Page_Recipes, image_data_base64=image_data_base64)
    else:
        return 'Image not found', 404
        
@views.route('/RecipeInfo/<rname>/<userid>', methods=["POST", "GET"])
def recipeinfo(rname, userid):
    form = Reviews()
    reviews_db = reviews_database(database_path)
    if form.validate_on_submit():
        review_text = form.review.data
        reviews_db.add_review(userid, review_text, rname)
        return redirect(url_for('views.recipeinfo', rname=rname, userid=userid))

    objectt = pantry_database(database_path)
    ingredients=objectt.get_recipe_info(rname)
    image_data = objectt.get_recipe_image(rname)
    review_list = reviews_db.display_review(rname)
    image = image_data[0]
    image_data_base64 = base64.b64encode(image).decode('utf-8')

    return render_template('pages/RecipeInfo.html', ingredientlist=ingredients, Recipe=rname, image_data_base64=image_data_base64, form=form, review_list=review_list)
@views.route('/recipedirections/<rname>', methods=["POST", "GET"])
def recipe_directions(rname):
    recipename = rname
    objectt = pantry_database(database_path)
    ingredients=objectt.get_recipe_directions(recipename)
    return render_template('pages/recipedirections.html', ingredientlist=ingredients, Recipe=recipename)

@views.route('/userprofile/<userid>')
@login_required
def userprofile(userid):
    objectt = user_database(database_path)
    favorite_recipe_instance = favorite_recipe(database_path)
    userinfo= objectt.get_user(userid)
    favorite_recipes = favorite_recipe_instance.display_favorite_recipe(userid)
    return render_template('pages/userprofile.html', item=userinfo, favorite_recipes=favorite_recipes)

@views.route('/useredit/<userid>')
@login_required
def useredit(userid):
    objectt = user_database(database_path)
    userinfo= objectt.get_user(userid)
    return render_template('pages/useredit.html',item=userinfo)

@views.route('/shoplist/<userid>')
@login_required
def shoppinglist(userid):
    objectt=shopping_list_database(database_path)
    listofingrients=objectt.display_shopping_list(userid)
    objectt = user_database(database_path)
    userinfo= objectt.get_user(userid)
    return render_template('pages/usershoppinglist.html',item=userinfo, shoplist=listofingrients)

@views.route('/newshoplist/<userid>/<rname>')
@login_required
def generateshoplist(userid, rname):
    objectt=pantry_database(database_path)
    ingredientslist=objectt.get_recipe_info(rname)
    objectt_shop=shopping_list_database(database_path)
    for item in ingredientslist:
        objectt_shop.add_item(userid, item)
    return shoppinglist(userid)

@views.route('/removeshoplist/<userid>/<removeingredient>', methods=["POST"])
@login_required
def removeshoplistitem(userid, removeingredient):
    objectt=shopping_list_database(database_path)
    objectt.remove_item(userid,removeingredient)
    return shoppinglist(userid)

@views.route('/pantry/<userid>', methods=["POST", "GET"])
@login_required
def viewpantry(userid):
    objectt = user_database(database_path)
    userinfo= objectt.get_user(userid)
    objectt = pantry_database(database_path)
    ingredients= objectt.display_pantry(userid)
    autofill = objectt.ingredient_list()
    return render_template('pages/pantryprofile.html', item= userinfo, pantrylist=ingredients, ingr=autofill)

@views.route('/pantryadd/<userid>/', methods=["POST", "GET"])
@login_required
def addtopantry(userid):
    objectt = pantry_database(database_path)
    ingredientt= request.form.get("ing")
    ingredientsinput = ingredientt.split()
    for item in ingredientsinput:
        objectt.insert_into_pantry(userid, item)
    return viewpantry(userid)
    
@views.route('/pantrydelete/<userid>/<ingredients>', methods=["POST", "GET"])
@login_required
def remove_from_pantry(userid, ingredients):
        objectt= pantry_database(database_path)
        objectt.remove_from_pantry(userid,ingredients)
        return viewpantry(userid)

@views.route('/pantrysearch/<userid>', methods=["POST", "GET"])
def pantrysearch(userid):
        useridd= userid
        objectt= pantry_database(database_path)
        recipes_from_pantry= objectt.recommend_recipes(userid)
        return render_template('pages/pantryRecipes.html',recipelist=recipes_from_pantry, userid = useridd)

@views.route('/keto', methods=['POST', 'GET'])
def keto():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Keto")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/lactose_free', methods=['POST', 'GET'])
def lactose_free():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Lactose-free")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/omnivorous', methods=['POST', 'GET'])
def omnivorous():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Omnivorous")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/pescatarian', methods=['POST', 'GET'])
def pescatarian():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Pescatarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/non_vegetarian', methods=['POST', 'GET'])
def non_vegetarian():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Non-Vegetarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/vegetarian', methods=['POST', 'GET'])
def vegetarian():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Vegetarian")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/vegan', methods=['POST', 'GET'])
def vegan():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Vegan")
    return render_template(Page_Recipes, recipelist=recipes)

@views.route('/gluten_free', methods=['POST', 'GET'])
def gluten_free():
    objectt= dietary_prefernces_database(database_path)
    recipes = objectt.get_recipes_dietary("Gluten-free")
    return render_template(Page_Recipes, recipelist=recipes)


@views.route('/addrecipe/<userid>', methods=["POST", "GET"])
def viewaddrecipe(userid):
    objectt = user_database(database_path)
    userinfo= objectt.get_user(userid)
    return render_template('pages/addrecipe.html', item=userinfo)

@views.route('/addedrecipe/<userid>', methods=["POST", "GET"])
def add_recipe(userid):
    objectt = user_database(database_path)
    userinfo= objectt.get_user(userid)
    if request.method == 'POST':
        recipe_name = request.form.get("recipe_name")
        objectt2=chef_database(database_path)
        objectt2.add_recipe_name(userid,recipe_name)
        quantities = request.form.get("quantities")
        instructions = request.form.get("instructions")
        recipeimage = request.files['recipe_image']
        recipeimag2=recipeimage.read()
        recipeimagebase64=base64.b64encode(recipeimag2)
        recipeimagebinary=base64.b64decode(recipeimagebase64)
        object2.add_recipe_quantites(recipe_name,quantities)
        object2.add_recipe_instructions(recipe_name,instructions)
        object2.add_picture(recipe_name,recipeimagebinary)
    return render_template('pages/addrecipe.html', item=userinfo)

# Error handlers.
@views.errorhandler(500)
def internal_error(error):
    #db_session.rollback()
    return render_template('errors/500.html'), 500


@views.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    views.run()

# Or specify port manually:
