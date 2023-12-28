
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_wtf import FlaskForm


class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4)], render_kw={"placeholder": "Adresse email", "class":"form-control"})
    password = PasswordField(validators=[InputRequired(), Length(min=4)], render_kw={"placeholder": "Mot de passe", "class":"form-control"})
    submit = SubmitField("Se connecter", render_kw={"class":"btn btn-primary btn-block", "style": "width: 100%"})
    
