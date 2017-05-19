from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField
from wtforms.fields import TextField, BooleanField
 
class requestForm(Form):
  email = TextField("Email")
  message = TextAreaField("Message")
  checkbox = BooleanField("Is this a request to add or update a word?")
  submit = SubmitField("Submit")
