from datetime import datetime
from wtforms import DateField, StringField, SubmitField, TimeField
from website import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import pytz



class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    type = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(10), default='user')

class OrganiseActivity(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(150), nullable=False)
    activity_date = db.Column(db.Date, nullable=False)
    activity_time = db.Column(db.Time, nullable=False)
    

class OrganiseActivityForm(FlaskForm):  # Example form using Flask-WTF
    activity_name = StringField('Activity Name', validators=[DataRequired()])
    activity_date = DateField('Activity Date', validators=[DataRequired()])
    activity_time = TimeField('Activity Time', validators=[DataRequired()])
    submit = SubmitField('Organise Activity')

