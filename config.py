import os

# Base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Configuration settings for the Flask application.
    """
    DEBUG = True  # Enable debug mode
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"

    # Database settings (SQLite)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        f"sqlite:///{os.path.join(basedir, 'instance', 'superheroes.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
