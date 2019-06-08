from flask_wtf.file import FileField, FileRequired, FileAllowed
from Catalog.models import Categorie
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required
from Catalog import app, photos
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField, SubmitField,
BooleanField, TextAreaField, SelectField, DecimalField

MyCategories = Categorie.query.order_by(Categorie.name).all()


class DollarField(DecimalField):
    def process_formdata(self, valuelist):
        if len(valuelist) == 1:
            self.data = [valuelist[0].strip('$').replace(',', '')]
        else:
            self.data = []


class ItemForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Content', validators=[DataRequired()])
    categorie = SelectField('Categorie', choices=[(
        c.id, c.name) for c in MyCategories], coerce=int,
        validators=[DataRequired()])
    price = DollarField('Price', validators=[DataRequired()])
    photo = FileField('Photo', validators=[
                      FileRequired(), FileAllowed(photos, 'Images only!')])
    submit = SubmitField('Save Item')
