from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from .models import User
from .views import views
from .auth import auth
from .extensions import db
from os import urandom
DB_NAME = "MainDB.db"

def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY'] = 'heythisisconanthedetector'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    secret_key = urandom(24)
    app.config["SECRET_KEY"] = secret_key
    app.config["RECAPTCHA_USE_SSL"] = False
    app.config["RECAPTCHA_PUBLIC_KEY"] = "6Lfer0kpAAAAAJnXGODihTewNcf3RDCXgc5FE7XY"
    app.config["RECAPTCHA_PRIVATE_KEY"] = "6Lfer0kpAAAAAEAtPP1igzvVEtUySFK8UpOCN57X"
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