from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional,URL, NumberRange

default_image_url = "https://images.pexels.com/photos/1108099/pexels-photo-1108099.jpeg?auto=compress&cs=tinysrgb&w=800"


class AddPetForm(FlaskForm):

    name = StringField("Pet name",validators=[InputRequired(message="Please provide a name")])
    species = RadioField("Species",choices=[('cat','cat'),('dog','dog'),('porcupine','porcupine')], validators=[InputRequired()])
    photo_url = StringField("Photo URL",validators=[Optional(), URL()],default=default_image_url)
    age = IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes = StringField("Notes",validators=[Optional()])

class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL",validators=[Optional(), URL()],default=default_image_url)
    notes = StringField("Notes",validators=[Optional()])
    available = BooleanField('Is Available',default=True)
