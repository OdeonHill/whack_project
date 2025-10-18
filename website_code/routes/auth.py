from flask import Blueprint, render_template, request, flash, redirect, url_for, make_response, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash
from . import db
from .models import User
from .views import no_cache

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) # Login route
@no_cache #no_cache decorator to prevent caching
def login():
    if request.method == 'POST': # If the request method is POST, it means the user is trying to log in
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()# Query the database for the user with the given usernam
        if user and check_password_hash(user.password, password): # Check if the user exists and if the password is correct
            login_user(user) # Log the user in
            session.modified = True # Mark the session as modified to ensure it is saved
            flash('Logged in successfully.', category='success')
            return redirect(url_for('views.manager_dashboard' if user.role == 'project_manager' else 'views.member_dashboard'))
        else:
            flash('Incorrect username or password. If you do not have an account, inform a project manager.', category='error')

    return render_template('login.html')

@auth.route('/logout')
@login_required
@no_cache #no_cache decorator to prevent caching
def logout():
    logout_user() # Log the user out
    session.clear() # Clear the session
    # Clear cookies
    response = make_response(redirect(url_for('auth.login')))
    response.set_cookie('session', '', expires=0)
    response.set_cookie('remember_token', '', expires=0)
    flash('Logged out successfully.', category='success')
    return response
