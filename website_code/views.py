from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/lessons')
def lessons():
    return render_template("lessons.html")

@views.route('/tracker')
def tracker():
    return render_template("tracker.html")

@views.route('/investing_lesson')
def investing_lesson():
    return render_template("investing_lesson.html")

@views.route('/phishing_lesson')
def phishing_lesson():
    return render_template("phishing_lesson.html")

@views.route('/savings_lesson')
def savings_lesson():
    return render_template("savings_lesson.html")

@views.route('/login')
def login():
    return render_template("login.html")
