from datetime import date, datetime
from functools import wraps
from flask import Blueprint, redirect, render_template, flash, url_for
from flask_login import login_required, current_user
from website import db
from website.models import OrganiseActivity, OrganiseActivityForm

views = Blueprint('views', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.role != 'ADMIN':  # Check if user is authenticated
            flash('You need to be an administrator.')
            return redirect(url_for('views.home'))  # Redirect to login if not authenticated
        return f(*args, **kwargs)
    return decorated_function

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/myactivities')
@login_required
def myactivites():
    return render_template("myactivities.html")


@views.route('/bookactivity')
@login_required
def bookactivity():
    today = datetime.today().date()
    activities = OrganiseActivity.query.filter(OrganiseActivity.activity_date >= today).all()

    return render_template("bookactivity.html", user=current_user, activities=activities)

@views.route('/myactivities')
@login_required
def myactivities():
    return render_template("myactivities.html", user=current_user)

@views.route('/organiseactivity', methods=['GET','POST'])
@login_required
@admin_required
def organiseactivity_view():
    form = OrganiseActivityForm()
    today_date = date.today().strftime('%Y-%m-%d')
    if form.validate_on_submit():
        new_activity = OrganiseActivity(
            activity_name=form.activityname.data,
            activity_date=form.activitydate.data,
            activity_time = form.activitytime.data
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