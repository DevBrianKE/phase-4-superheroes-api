
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base configuration class.
    Add any settings you need here.
    """
    # Enable Flask debug mode
    DEBUG = True

    # Secret key for session management
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"

    # Database configuration (SQLite for simplicity)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "instance", "superheroes.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
