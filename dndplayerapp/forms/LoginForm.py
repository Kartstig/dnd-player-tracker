from wtforms import Form, BooleanField, StringField, validators

class LoginForm(Form):
    username	= StringField('Email Address', [validators.InputRequired()])
    password	= StringField('Password', [validators.InputRequired()])
