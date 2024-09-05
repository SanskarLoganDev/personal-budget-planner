import os
from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)

    # Define the path to the SQLite database
    db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'instance', 'budget.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)

    with app.app_context():
        db.create_all()  # Create tables if they do not exist

    return app
