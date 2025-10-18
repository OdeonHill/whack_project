from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iwukhiq74tvfshjdfcuw37yywuuw78392ucnd83298'

    # Import blueprints
    from .views import bp as views_bp
    from .lessons import bp as lessons_bp
    from .goals import bp as goals_bp
    from .auth import bp as auth_bp

    # Register blueprints
    app.register_blueprint(views_bp, url_prefix='/')
    app.register_blueprint(lessons_bp, url_prefix='/lessons')
    app.register_blueprint(goals_bp, url_prefix='/goals')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
