from wtforms import DateField, StringField, SubmitField, TimeField
from website import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired


class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    # Additional fields as needed

class organiseactivity(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    activityname = db.Column(db.String(150), nullable=False)
    activitydate = db.Column(db.Date, nullable=False)
    activitytime = db.Column(db.Time, nullable=False)
    

class organiseactivityForm(FlaskForm):  # Example form using Flask-WTF
    activityname = StringField('Activity Name', validators=[DataRequired()])
    activitydate = DateField('Activity Date', validators=[DataRequired()])
    activitytime = TimeField('Activity Time', validators=[DataRequired()])
    submit = SubmitField('Organise Activity')
