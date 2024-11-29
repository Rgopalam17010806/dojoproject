from website import db
from flask_login import UserMixin
from sqlalchemy.orm import relationship

class User(db.Model, UserMixin):  
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(1000), nullable=False)
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    type = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(10), default='user')
    fcm_token = db.Column(db.String(250))

class BookActivity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    activity_id = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', foreign_keys='BookActivity.user_id')