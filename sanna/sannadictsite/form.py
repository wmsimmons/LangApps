from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, TextAreaField, SubmitField
 
class requestForm(FlaskForm):
  name = TextField("Name")
  email = TextField("Email")
  message = TextAreaField("Message")
  checkbox = BooleanField("Request to add/modify a word?")
  submit = SubmitField("Submit")
