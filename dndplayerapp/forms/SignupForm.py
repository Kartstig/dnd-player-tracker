from wtforms import Form, BooleanField, StringField, validators

class SignupForm(Form):
    username		= StringField('Email Address*', 
    	[validators.InputRequired(), validators.Email(message="Invalid Email")])
    password		= StringField('Password*', [validators.InputRequired()])
    first_name		= StringField('First Name')
    last_name		= StringField('Last Name')
    phone_number	= StringField('Phone Number')
