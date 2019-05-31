from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Required
from Catalog.models import Categorie

MyCategories = Categorie.query.order_by(Categorie.name).all()

class DollarField(DecimalField):
    def process_formdata(self, valuelist):
        if len(valuelist) == 1:
            self.data = [valuelist[0].strip('$').replace(',', '')]
        else:
            self.data = []

        # Calls "process_formdata" on the parent types of "DollarField",
        # which includes "DecimalField"
       # super(DollarField).process_formdata(self.data)

class ItemForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Content', validators=[DataRequired()])
    categorie = SelectField('Categorie', choices=[(c.id, c.name) for c in MyCategories],coerce=int, validators=[DataRequired()])
    price = DollarField('Price', validators=[DataRequired()])
    # picture
    submit = SubmitField('Create new Item')

