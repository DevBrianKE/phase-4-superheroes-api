from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Application factory pattern for Flask.
    Returns a configured Flask app.
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")  # Load configuration

    # Initialize database and migration objects
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so migrations can detect them
    from models import Superhero

    # Simple route to test API
    @app.route("/superheroes", methods=["GET"])
    def get_superheroes():
        """
        Returns a list of all superheroes in JSON format.
        """
        heroes = Superhero.query.all()
        return jsonify([
            {"id": hero.id, "name": hero.name, "power": hero.power} 
            for hero in heroes
        ])

    return app
