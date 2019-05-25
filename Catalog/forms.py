from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RestaurantForm(FlaskForm):
    
    name = StringField('Name',validators=[DataRequired(), Length(min=2, max=40)])
    submit = SubmitField('Create')