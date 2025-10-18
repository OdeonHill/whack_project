from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os
from os import path

def create_app():
    app = Flask(__name__)

    return app