from flask_login import UserMixin
from . import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    role = db.Column(db.String(1000))

class TestCodes(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_code = db.Column(db.String(100), unique=True)
    client_name = db.Column(db.String(100))
    client_link = db.Column(db.String(100))
    client_username = db.Column(db.String(1000))
    client_password = db.Column(db.String(100))
    test_date_from = db.Column(db.String(100))
    test_date_to = db.Column(db.String(100))
    test_date = db.Column(db.String(100))
    test_month = db.Column(db.String(100))
    user_id = db.Column(db.Integer)
    test_modules = db.Column(db.String (100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False)

    