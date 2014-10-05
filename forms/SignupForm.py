from wtforms import Form, BooleanField, StringField, validators

class SignupForm(Form):
    username		= StringField('Email Address*', [validators.InputRequired()])
    password		= StringField('Password*', [validators.InputRequired()])
    first_name		= StringField('First Name', [validators.InputRequired()])
    last_name		= StringField('Last Name', [validators.InputRequired()])
    phone_number	= StringField('Phone Number', [validators.InputRequired()])
