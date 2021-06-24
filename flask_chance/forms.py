from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, DecimalField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_chance.models import User


class RegistrationForm(FlaskForm):
    name = StringField('Name',
                       validators=[DataRequired(), Length(min=2, max=40)])
    cpf = StringField('CPF', validators=[
                      DataRequired(), Length(min=10, max=12)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_cpf(self, cpf):
        user = User.query.filter_by(cpf=cpf.data).first()
        if user:
            raise ValidationError('That cpf is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class BuyForm(FlaskForm):
    id_cafe = StringField('Coffee Type', validators=[DataRequired()])
    quant_cafe = StringField('Quantity', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    qdata = DateField('Date')
    submit = SubmitField('Order')
