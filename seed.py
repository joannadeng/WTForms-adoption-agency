from models import db, Pet, default_image_url, porcupine_url, cat_url, dog_url
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    Pet.query.delete()

    pet1 = Pet(name="cookie" , species="dog" , photo_url=dog_url , age=1, notes="very lovely", available=True)

    pet2 = Pet(name="strawberry" , species="cat" , photo_url=cat_url , age=1, notes="very clinging", available=True)

    pet3 = Pet(name="meatball" , species="porcupine" , photo_url=porcupine_url , age=0.5, notes="it's cute actually ", available=True)

    pets = [pet1,pet2,pet3]
    db.session.add_all(pets)
    db.session.commit()



    