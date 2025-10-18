from website_code import db
from flask_login import UserMixin,login_manager
from sqlalchemy import func

class User(UserMixin, db.Model):
    __tablename__ = 'User' 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

    def __repr__(self):
        return f"User('{self.id}')"
    
    def get_id(self):
        return self.id


class Savings(db.Model):
    __tablename__ = 'Savings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    goal = db.Column(db.String(100), nullable=True)
    total_amount = db.Column(db.Float, nullable=False)
    current_amount = db.Column(db.Float, nullable=False, default=0.0)
    after_interest = db.Column(db.Float, nullable=True)
    interest_rate = db.Column(db.Float, nullable=True)
    start_date = db.Column(db.Date, nullable=False, default=func.current_date())
    end_date = db.Column(db.Date, nullable=True)

class Lessons(db.Model):
    __tablename__ = 'Lessons'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

class LessonsCompleted(db.Model):
    __tablename__ = 'LessonsCompleted'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('Lessons.id'), nullable=False)