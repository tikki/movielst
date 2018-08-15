from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired
from movielst import config


class SettingsForm(FlaskForm):
    omdb_api_key_field = StringField('OMDB API KEY', validators=[InputRequired()], default=config.get_setting('API', 'OMDb_API_key'))
    submit = SubmitField('Save')
