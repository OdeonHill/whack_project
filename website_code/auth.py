from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from . import db
from .models import User
from .views import no_cache

auth = Blueprint('auth', __name__)
@auth.route('/login', methods=['GET', 'POST'])  # Login route
@no_cache  # Prevent caching
def login():
    if request.method == 'POST':  # If the request method is POST, the user is trying to log in
        email2 = request.form.get('username')  # Get the email from the form
        password = request.form.get('password')  # Get the password from the form
        print(email2)
        user = User.query.filter_by(email=email2).first()  # Query the database for the user with the given email
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
