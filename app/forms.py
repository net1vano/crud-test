from flask_wtf import FlaskForm
from wtforms import TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class Buttons(FlaskForm):
  uid = TextAreaField('Input id')
  create = SubmitField('POST')
  read = SubmitField('GET')
  update = SubmitField('UPDATE')
  delete = SubmitField('DELETE')
