from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms import InputRequired, Optional,URL, NumberRange

default_image_url = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=800"


class AddPetForm(FlaskForm):

    name = StringField("Pet name")
    species = RadioField("Species",choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')])
    photo_url = StringField("Photo URL",validators=[URL(message="please enter a valid URL")],default=default_image_url)
    age = IntegerField("Age",validators=[(NumberRange(min=0,max=30))])
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL",validators=[URL(message="please enter a valid URL")],default=default_image_url)
    notes = StringField("Notes")
    available = BooleanField('Is Available',default=True)
