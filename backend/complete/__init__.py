from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .models import User
from .views import views
from .auth import auth
from .extensions import db
import os
DB_NAME = "MainDB.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    secret_key = os.urandom(24)
    app.config["SECRET_KEY"] = secret_key
    app.config["RECAPTCHA_USE_SSL"] = False
    app.config["RECAPTCHA_PUBLIC_KEY"] = "6Lfer0kpAAAAAJnXGODihTewNcf3RDCXgc5FE7XY"

    RECAPTCHA_PRIVATE_KEY = os.environ.get("RECAPTCHA_PRIVATE_KEY")
    print(f"RECAPTCHA_PRIVATE_KEY: {RECAPTCHA_PRIVATE_KEY}")
    
    if not RECAPTCHA_PRIVATE_KEY:
        raise ValueError("RECAPTCHA_PRIVATE_KEY environment variable is not set")
    app.config["RECAPTCHA_PRIVATE_KEY"] = RECAPTCHA_PRIVATE_KEY

    app.config["RECAPTCHA_OPTIONS"] = {'theme' : 'black'}
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

def create_database(app):
    with app.app_context():
        db.create_all()
        print('DB created successfully')