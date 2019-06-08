from flask_login import UserMixin
import random
import string
import datetime
from Catalog import db, login_manager
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import
(TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


secret_key = ''.join(random.choice(
    string.ascii_uppercase + string.digits) for x in range(32))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Categorie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    categoriesItem = db.relationship(
        'CategorieItem', backref='categorie', lazy=True)
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

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

    def __repr__(self):
        return f"CategorieItem('{self.name}', '{self.description}',
                               '{self.id}', '{self.price}', '{self.course}',
                               '{self.created_at}')"


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    name = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(64))
    picture = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=False)
    items = db.relationship('CategorieItem', backref='author', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow())

    def hash_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(secret_key, expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            # Valid Token, but expired
            return None
        except BadSignature:
            # Invalid Token
            return None
        user_id = data['id']
        return user_id

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.id}')"
