from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/bookactivity')
@login_required
def bookactivity():
    return render_template("bookactivity.html", user=current_user)

@views.route('/organiseactivity')
@login_required
def organiseactivity():
    return render_template("organiseactivity.html", user = current_user)