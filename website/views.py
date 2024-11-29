from functools import wraps
import os
from flask import Blueprint, json, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, current_user
from website import db
from website.models import BookActivity

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
    json_url = os.path.join(SITE_ROOT, "static/data", "activites.json")
    with open(json_url) as activity_file:
        return json.load(activity_file)

@views.route('/bookactivity')
@login_required
def bookactivity():
    menu = load_menu()
    return render_template("bookactivity.html", user=current_user, activities=menu["activities"])

@views.route('/unregisteractivity', methods=['POST'])
@login_required
def unregisteractivity():
    booking_id = request.form.get("booking_id")
    booking_activity = BookActivity.query.get(booking_id)
    db.session.delete(booking_activity)
    db.session.commit()
    flash('Activity is un registered.')
    return render_template("home.html", user=current_user)

@views.route('/joinactivity', methods=['POST'])
@login_required
def joinactivity():
    activity_id = request.form.get("activity_id")
    booking_activity = BookActivity(activity_id=activity_id, user_id=current_user.id)
    db.session.add(booking_activity)
    db.session.commit()
    flash('Booked succesfully.')
    return render_template("home.html", user=current_user)

@views.route('/myactivities')
@login_required
def myactivities():
    menu = load_menu()
    user_id = current_user.id
    activities = BookActivity.query.filter(BookActivity.user_id==user_id).all()
    enriched_activities=[]
    for act in activities:
        menu_activity = next((item for item in menu["activities"] if item['id'] == act.activity_id), None)
        enriched = {
            "id": act.id,
            "activity_id": menu_activity["id"],
            "name": menu_activity["name"],
            "skills": menu_activity["skills"],
            "description": menu_activity["description"],
            "teacher": menu_activity["teacher"],
            "date": menu_activity["date"],
            "start_time": menu_activity["start_time"],
            "end_time": menu_activity["end_time"],
            "image_url": menu_activity["image_url"]
        }
        enriched_activities.append(enriched)
    return render_template("myactivities.html", user=current_user, my_activities=enriched_activities)

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