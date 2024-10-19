from wtforms import DateField, StringField, SubmitField, TimeField
from website import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    type = db.Column(db.String(10))


class organiseactivity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activityname = db.Column(db.String(150), nullable=False)
    activitydate = db.Column(db.Date, nullable=False)
    activitytime = db.Column(db.Time, nullable=False)


class organiseactivityForm(FlaskForm):
    activityname = StringField('Name of the activity', validators=[DataRequired()])
    activitydate = DateField('Date of Activity', format='%Y-%m-%d', validators=[DataRequired()])
    activitytime = TimeField('Time of Activity', format='%H:%M', validators=[DataRequired()])
    submit = SubmitField("Submit")

