from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Passwords must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register!')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError('Your email has been registered already!')

    def validate_username(self, username):
        if User.query.filter_by(username=username.data).first():
            raise ValidationError('Your username has been registered already!')

class UpdateUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('UserName', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')
