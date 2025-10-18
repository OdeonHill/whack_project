from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize the SQLAlchemy object
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iwukhiq74tvfshjdfcuw37yywuuw78392ucnd83298'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    login_manager = LoginManager(app)   
    # Import blueprints
    from .views import views
    from .auth import auth
    
    # Initialize the db with the app
    db.init_app(app)
    login_manager.init_app(app)

     # Create tables if they don't exist
    with app.app_context():
        db.create_all()  # This creates all tables for your models

    from .models import User  # Ensure this import happens after login_manager initialization
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app
