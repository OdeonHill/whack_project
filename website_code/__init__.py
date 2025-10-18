from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'iwukhiq74tvfshjdfcuw37yywuuw78392ucnd83298'

    # Import blueprints
    from .views import views
    
    # Register blueprints
    app.register_blueprint(views, url_prefix='/')

    return app
