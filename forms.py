from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email,EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired(),Length(min=11,max=11)])
    email = StringField('Email', validators=[DataRequired(),Email('Wrong Email')])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])
    btn = SubmitField('Signup')
    

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6)])
    remember = BooleanField('Remeber Me')
    btn = SubmitField('Login')
    