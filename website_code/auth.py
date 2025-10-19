from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash,generate_password_hash
from . import db
from .models import User
from .views import no_cache
import re

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])  # Login route
@no_cache  # Prevent caching
def login():
    if request.method == 'POST':  # If the request method is POST, the user is trying to log in
        email = request.form.get('username')  # Get the email from the form
        password = request.form.get('password')  # Get the password from the form
        user = User.query.filter_by(email=email).first()  # Query the database for the user with the given email
        if user and check_password_hash(user.password,password):  # Check if user exists and password matches
            login_user(user)  # Log the user in using Flask-Login
            return redirect(url_for('views.dashboard'))  # Redirect to the dashboard page
    return render_template('login.html')  # Render the login template when the method is GET

@auth.route('/logout')
@login_required
@no_cache #no_cache decorator to prevent caching
def logout():
    logout_user() # Log the user out
    return redirect(url_for('views.home'))

@auth.route('/signup', methods=['GET', 'POST'])
@no_cache
def signup():
    if request.method == 'POST':  # If the request method is POST, the user is trying to sign up
        try:
            email = sanitise_email(request.form.get('username'))  # Get the email from the form
            password = request.form.get('password') 
            user = User(email=email, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return render_template('login.html')
        except ValueError as e:
                error_message = str(e)  # Catch the error and send it to the template
                return render_template('signup.html', error_message=error_message)
    return render_template('signup.html')





def sanitise_email(email):
    # Remove leading/trailing whitespace
    email = email.strip()
    
    # Validate email format using regex (simple validation)
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")
    
    # Normalize the email (e.g., lowercase it)
    email = email.lower()
    
    # Optionally, you could further sanitize by escaping characters depending on the context (e.g., for SQL or HTML)
    
    return email

