from Catalog import db
import datetime

class Categorie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    categoriesItem = db.relationship('CategorieItem', backref='categorie', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Categorie('{self.name}','{self.id}')"


class CategorieItem(db.Model):

    name = db.Column(db.String(20), unique=False, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    picture = db.Column(db.String(200))
    categorie_id = db.Column(db.Integer, db.ForeignKey(
        'categorie.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f"CategorieItem('{self.name}', '{self.description}', '{self.id}', '{self.price}','{self.course}','{self.created_at}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    picture = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.id}')"
