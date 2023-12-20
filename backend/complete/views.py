#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Blueprint, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
import sqlalchemy
import sqlite3
from logging import Formatter, FileHandler
from .forms import *
from flask_login import login_required, current_user
from controllers.database import pantry_database, user_database

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

@views.route('/home2')
@login_required
def home2():
    return render_template('pages/HomePage.html',  user=current_user)


@views.route('/Recipes', methods=["POST", "GET"])
def about():
    object = pantry_database("instance\\MainDB.db")
    if request.method == "GET":
        recipes= object.return_all_recipe_names()
        return render_template('pages/Recipes.html', recipelist=recipes)
    else:
        rname= request.form.get("recipename")
        #print(rname)
        recipesearch= object.get_similar_recipes(rname)
        return render_template('pages/Recipes.html', recipelist=recipesearch)

        
@views.route('/RecipeInfo/<rname>', methods=["POST", "GET"])
def recipeinfo(rname):
    recipename = rname
    object = pantry_database("instance\\MainDB.db")
    ingredients=object.get_recipe_info(recipename)
    return render_template('pages/RecipeInfo.html', ingredientlist=ingredients, Recipe=recipename)

@views.route('/userprofile/<userid>')
def userprofile(userid):
    object = user_database("instance\\MainDB.db")
    userinfo= object.get_user(int(userid))
    return render_template('pages/userprofile.html', item=userinfo)

@views.route('/useredit/<userid>')
def useredit(userid):
    object = user_database("instance\\MainDB.db")
    userinfo= object.get_user(int(userid))

    return render_template('pages/useredit.html',item=userinfo)

# @views.route('/useredit')
# def useredit():





# @app.route('/forgot')
# def forgot():
#     form = ForgotForm(request.form)
#     return render_template('forms/forgot.html', form=form)

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
