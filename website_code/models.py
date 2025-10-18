from website_code import db
from flask_login import UserMixin
from sqlalchemy import func Enum

class User(db.Model, UserMixin):
    email = db.Column(db.String(150), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(150), nullable=False)

class Savings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(150), db.ForeignKey('User.email'), nullable=False)
    goal = db.Column(db.String(100), nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, nullable=False, default=0.0)
    after_interest = db.Column(db.Float, nullable=True)
    interest_rate = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.Date, nullable=False, default=func.current_date())
    end_date = db.Column(db.Date, nullable=True)

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.Enum('Budgeting', 'Investing', 'Saving', 'Debt Management', name='lesson_category'), nullable=False)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('Lessons.id'), nullable=False)
    question = db.Column(db.Text, nullable=False)
    option_a = db.Column(db.String(200), nullable=False)
    option_b = db.Column(db.String(200), nullable=False)
    option_c = db.Column(db.String(200), nullable=False)
    option_d = db.Column(db.String(200), nullable=False)
    correct_option = db.Column(db.Enum('A', 'B', 'C', 'D', name='quiz_option'), nullable=False)

class LessonsUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(150), db.ForeignKey('User.email'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('Lessons.id'), nullable=False)
    completed = db.Column(db.Boolean, default=False)