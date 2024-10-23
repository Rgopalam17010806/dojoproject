from datetime import date
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_required, current_user, login_user
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
    if login_user(current_user.id).role !='admin':
        flash('Sorry but this is only for admins','error')
        return redirect(url_for('home'))
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


@views.route('/contactus')
def contactus():
    return render_template("contactus.html")

@views.route('/forgotpassword')
def forgotpassword():
    return render_template("forgotpassword.html")

@views.route('/resetpassword')
def resetpassword():
    return render_template("resetpassword.html")

@views.route('/viewourupcomingsessions')
def viewourupcomingsessions():
    return render_template("viewourupcomingsessions.html")

@views.route('/viewyourbookings')
def viewyourbookings():
    return render_template("viewyourbookings.html")

@views.route('/waitlist')
def waitlist():
    return render_template("waitlist.html")