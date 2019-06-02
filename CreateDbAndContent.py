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
    description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, ",
    price="7.50",
    categorie_id=Categorie1.id)
db.session.add(CategorieItem2)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id, name="Ball", description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel",
                               price="2.99", categorie_id=Categorie1.id)

db.session.add(CategorieItem2)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id, name="Shirt", description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, e",
                               price="5.50", categorie_id=Categorie1.id)

db.session.add(CategorieItem2)
db.session.commit()

# Menu for Super Stir Fry
Categorie2 = Categorie(user_id=user1.id, name="Basketball")

db.session.add(Categorie2)
db.session.commit()

CategorieItem1 = CategorieItem(user_id=user1.id, name="Ball", description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, ",
                               price="7.99", categorie_id=Categorie2.id)

db.session.add(CategorieItem1)
db.session.commit()

CategorieItem2 = CategorieItem(user_id=user1.id,
                               name="Bulls-Shirt", description="Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, ", price="25", categorie_id=Categorie2.id)

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

Categorie2 = Categorie(user_id=user1.id, name="Baseball")
db.session.add(Categorie2)

Categorie2 = Categorie(user_id=user1.id, name="Snowboarding")
db.session.add(Categorie2)

Categorie2 = Categorie(user_id=user1.id, name="Rock Climbing")
db.session.add(Categorie2)

Categorie2 = Categorie(user_id=user1.id, name="Skating")
db.session.add(Categorie2)

Categorie2 = Categorie(user_id=user1.id, name="Hockey")
db.session.add(Categorie2)

db.session.commit()

print("added menu items!")
