from functools import wraps  # <-- Add this import
from flask import request, Response
from flask import Blueprint, render_template, make_response, jsonify
from flask_login import current_user, login_required
from .models import *
import os
import dotenv
from os import path


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
    total = saving.total_amount
    current = saving.current_amount

    progress = (current / total) * 100 if total > 0 else 0
    return jsonify({
        'has_savings': True,
        'goal': total,
        'current': current,
        'progress': round(progress, 2)

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

@views.route('/signup')
def signup():
    return render_template("signup.html")

@views.route('/submit_lesson', methods=['POST'])
def submit_lesson():
    # Get the data from the form submission
    element1 = request.form.get('element1')
    element2 = request.form.get('element2')
    element3 = request.form.get('element3')

    # Check if both elements contain the word "Correct!"
    if element1 == "Correct!" and element2 == "Correct!":
        # Example: You could check if the user is logged in or fetch user from session
        user_id = current_user.id  # Assuming the user_id is available (e.g., from session)
        lesson_id = element3  # Assuming the lesson ID is available (e.g., from the form or context)

        # Add a record to LessonsCompleted
        lesson_completed = LessonsCompleted(user_id=user_id, lesson_id=lesson_id)
        db.session.add(lesson_completed)
        db.session.commit()

        # Return a success message as JSON
        return jsonify({"message": "Lesson complete!"}), 200

@views.route('/interest_calculator')
def interest_calculator():
    return render_template("interest_calculator.html")

@views.route('/add_savings', methods=['POST'])
@login_required
def add_savings():
    data = request.get_json()
    amount = data.get('amount', 0)

    saving = Savings.query.filter_by(user_id=current_user.id).first()
    if not saving:
        return jsonify({'success': False, 'error': 'No savings goal found.'}), 400

    saving.current_amount += float(amount)
    db.session.commit()

    return jsonify({'success': True, 'new_amount': saving.current_amount})
