from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.recaptcha import RecaptchaField

class Reviews(FlaskForm):
    review = TextAreaField('Comment', validators=[DataRequired()])
    recaptcha = RecaptchaField()
