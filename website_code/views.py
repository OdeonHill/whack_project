from functools import wraps  # <-- Add this import
from flask import request, Response
from flask import Blueprint, render_template, make_response, jsonify
from flask_login import current_user
from .models import *

views = Blueprint('views', __name__)

# Define the no_cache decorator
def no_cache(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get the response from the wrapped function
        response = f(*args, **kwargs)
        
        # If the response is a string (e.g., from render_template), wrap it in a response object
        if isinstance(response, str):
            response = make_response(response)
        
        # Set cache-related headers
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        
        return response
    return decorated_function

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

@views.route('/lessons')
def lessons():
    user = current_user  # Assuming you're using Flask-Login and current_user is available
    lessons = Lessons.query.all()  # Get all lessons
    
    # Get the lessons that the current user has completed
    completed_lessons = [lesson.lesson_id for lesson in LessonsCompleted.query.filter_by(user_id=user.id).all()]

    return render_template("lessons.html", lessons=lessons, completed_lessons=completed_lessons)

@views.route('/tracker')
def tracker():
    return render_template("tracker.html")

@views.route('savings_progress')
def savings_progress():
    saving = Savings.query.filter_by(user_id=current_user.id).first()
    if not saving:
        return jsonify({
            'has_savings': False,
            'image': '/static/images/veryangy.gif'
        })
    progress = (saving.current_amount / saving.total_amount) * 100 if saving.total_amount > 0 else 0
    return jsonify({
        'has_savings': True,
        'goal': saving.total_amount,
        'current': saving.current_amount,
        'progress': round(progress,2)

    })
    

@views.route('/investing_lesson')
def investing_lesson():
    return render_template("investing_lesson.html")

@views.route('/phishing_lesson')
def phishing_lesson():
    return render_template("phishing_lesson.html")

@views.route('/savings_lesson')
def savings_lesson():
    return render_template("savings_lesson.html")

@views.route('/credit_lesson')
def credit_lesson():
    return render_template("credit_lesson.html")

@views.route('/login')
def login():
    return render_template("login.html")

@views.route('/budget_calculator')
def budget_calculator():
    return render_template("budget_calculator.html")

@views.route('/credit_score')
def credit_score():
    return render_template("credit_score.html")

@views.route('/phone_demo')
def phone_demo():
    return render_template("phone.html")
