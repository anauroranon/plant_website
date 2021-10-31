from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired

from config import Config

config = Config()


class cutenessForm(FlaskForm):
    name = SelectField('name', choices=config.plant_names, validators=[DataRequired()])
    adjective = SelectField('adjective', choices=config.plant_adjectives, validators=[DataRequired()])
    submit = SubmitField('Submit')

