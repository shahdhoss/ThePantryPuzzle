import uuid
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    isChef = db.Column(db.String, default='off')