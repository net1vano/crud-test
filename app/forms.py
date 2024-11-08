from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class ButtonForm(FlaskForm):
  button_get = SubmitField('GET')
  button_read = SubmitField('READ')
  button_update = SubmitField('UPDATE')
  button_delete = SubmitField('DELETE')
