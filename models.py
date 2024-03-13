from flask_sqlalchemy import SQLAlchemy 

default_image_url = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=800"

db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

class Pet(db.Model):
    """Pet Model"""
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text)
    photo_url = db.Column(db.Text,default=default_image_url)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)