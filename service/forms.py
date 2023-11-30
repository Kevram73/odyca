
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(min=4)], render_kw={"placeholder": "Nom d'utilisateur", "class":"form-control"})
    password = PasswordField(validators=[InputRequired(), Length(min=4)], render_kw={"placeholder": "Mot de passe", "class":"form-control"})
    submit = SubmitField("Login")