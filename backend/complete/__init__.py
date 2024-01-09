from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .models import User
from .views import views
from .auth import auth
from .extensions import db

DB_NAME = "MainDB.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'heythisisconanthedetector'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view= 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)
    
    create_database(app)

    return app

# with views.app_context():
#     db.create_all()
#     login_manager = LoginManager()
#     login_manager.login_view= 'auth.login'
#     login_manager.init_app(views)

#     @login_manager.user_loader
#     def load_user(id):
#         return User.query.get(int(id))
#         return views

def create_database(app):
    with app.app_context():
        db.create_all()
        print('DB created successfully')