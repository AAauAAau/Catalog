from Catalog import db
from Catalog.models import Categorie, CategorieItem, User

db.reflect()
db.drop_all()
db.create_all()
print(Categorie.query.all())

# Create dummy user
user1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
db.session.add(user1)
db.session.commit()
# Menu for UrbanBurger
Categorie1 = Categorie(user_id=user1.id, name="Soccer")

db.session.add(Categorie1)
db.session.commit()
CategorieItem2 = CategorieItem(
    user_id=user1.id,
    name="Soccer shoes",
    description="Juicy grilled veggie patty with tomato mayo and lettuce",
    price="7.50",
    categorie_id=Categorie1.id)
db.session.add(CategorieItem2)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id, name="Ball", description="with garlic and parmesan",
                               price="2.99", categorie_id=Categorie1.id)

db.session.add(CategorieItem2)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id, name="shirt", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                               price="5.50", categorie_id=Categorie1.id)

db.session.add(CategorieItem2)
db.session.commit()

# Menu for Super Stir Fry
Categorie2 = Categorie(user_id=user1.id, name="Basketball")

db.session.add(Categorie2)
db.session.commit()

CategorieItem1 = CategorieItem(user_id=user1.id, name="Ball", description="With your choice of noodles vegetables and sauces",
                               price="7.99", categorie_id=Categorie2.id)

db.session.add(CategorieItem1)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id,
                               name="Bullsshirt", description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price="25", categorie_id=Categorie2.id)

db.session.add(CategorieItem2)
db.session.commit()

CategorieItem3 = CategorieItem(user_id=user1.id, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                               price="15", categorie_id=Categorie2.id)

db.session.add(CategorieItem3)
db.session.commit()
Categorie2 = Categorie(user_id=user1.id, name="Baseball")

db.session.add(Categorie2)

Categorie2 = Categorie(user_id=user1.id, name="Frisbee")

db.session.add(Categorie2)
db.session.commit()

print("added menu items!")
