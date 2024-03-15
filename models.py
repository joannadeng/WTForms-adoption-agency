from flask_sqlalchemy import SQLAlchemy 

default_image_url = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=800"

porcupine_url = "https://thumbs.dreamstime.com/z/porcupine-19739927.jpg?w=768"

cat_url="https://cdn.pixabay.com/photo/2014/04/13/20/49/cat-323262_1280.jpg"

dog_url="https://img.freepik.com/free-photo/isolated-happy-smiling-dog-white-background-portrait-4_1562-693.jpg?w=2000&t=st=1710480405~exp=1710481005~hmac=8678a4348271c51ff5ee1f9857714ab104c6fd2cf0be42bb5faf10f3ba605a3e"




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