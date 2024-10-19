from datetime import date
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from website import db

from website.models import organiseactivity, organiseactivityForm

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/bookactivity')
@login_required
def bookactivity():
    return render_template("bookactivity.html", user=current_user)

@views.route('/organiseactivity', methods=['GET','POST'])
@login_required
def organiseactivity_view():
    form = organiseactivityForm()
    today_date = date.today().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        new_activity = organiseactivity(
            activityname=form.activityname.data,
            activitydate=form.activitydate.data,
            activitytime = form.activitytime.data
        )
        
        db.session.add(new_activity)
        db.session.commit()
    return render_template("organiseactivity.html", user = current_user, form=form, today_date=today_date)