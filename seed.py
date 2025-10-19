from website_code import create_app, db
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from website_code.models import User, Savings, Lessons, LessonsCompleted

# Create the Flask app instance
app = create_app()

# Seed the User table
def seed_users():
    user1 = User(id=1,email="rene@gmail.com", password=generate_password_hash("TH1NK"))
    user2 = User(id=2,email="plato@hotmail.com", password=generate_password_hash("greek!"))

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

# Seed the Lessons table
def seed_lessons():
    lesson1 = Lessons(
        id = 1,
        title="Saving Methodologies",
    )
    lesson2 = Lessons(
        id = 2,
        title="Investing 101",
    )
    lesson3 = Lessons(
        id = 3,
        title="Phishing 101",
    )

    db.session.add(lesson1)
    db.session.add(lesson2)
    db.session.add(lesson3)
    db.session.commit()

# Seed the Savings table
def seed_savings():
    savings1 = Savings(
        user_id = 1,
        goal="Phone",
        total_amount=5000.0,
        current_amount=1500.0,
        after_interest=2000.0,
        interest_rate=0.03,  # 3% interest rate
        start_date=date(2023, 1, 1),
        end_date=date(2023, 12, 31)
    )

    db.session.add(savings1)
    db.session.commit()

# Seed the LessonsUser table (example of user progress in lessons)
def seed_lessons_completed():
    lesson_user1 = LessonsCompleted(id =1,user_id=1, lesson_id=1)
    lesson_user2 = LessonsCompleted(id =2,user_id=2, lesson_id=2)
    
    db.session.add(lesson_user1)
    db.session.add(lesson_user2)

    db.session.commit()

# Main function to seed the database
def seed_db():
     with app.app_context():
        db.create_all()  # Ensure tables are created if they don't exist
        seed_users()
        seed_lessons()

        seed_savings()
        seed_lessons_completed()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_db()
