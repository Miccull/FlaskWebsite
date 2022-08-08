# Baza de date cu cheile

from time import timezone
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    username = db.Column(db.String(128), unique=True)
    name = db.Column(db.String(128), nullable=True)
    surname = db.Column(db.String(128), nullable=True)
    job = db.Column(db.String(128), nullable=True)
    country= db.Column(db.String(128), nullable=True)
    notes = db.relationship('Note')

