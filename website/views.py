from datetime import date, datetime
from functools import wraps
import os
from flask import Blueprint, json, redirect, render_template, flash, url_for
from flask_login import login_required, current_user
from website import db
from website.models import OrganiseActivity, OrganiseActivityForm

views = Blueprint('views', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or getattr(current_user, 'role', None) != 'ADMIN': # Check if user is authenticated
            flash('You need to be an administrator.')
            return redirect(url_for('views.home'))  # Redirect to login if not authenticated
        return f(*args, **kwargs)
    return decorated_function

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

def load_menu():
    SITE_ROOT = os.path.relpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "activities.json")
    with open(json_url) as activity_file:
        return json.load(activity_file)


@views.route('/bookactivity')
@login_required
def bookactivity():
    activity = load_menu()
    return redirect(url_for('bookactivity.html', activity))  # Redirect to the activities list




@views.route('/organiseactivity', methods=['GET','POST'])
@login_required
@admin_required
def organiseactivity_view():
    form = OrganiseActivityForm()
    today_date = date.today().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        new_activity = OrganiseActivity(
            activity_name=form.activity_name.data,
            activity_date=form.activity_date.data,
            activity_time = form.activity_time.data
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