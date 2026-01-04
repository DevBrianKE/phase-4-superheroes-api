from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Application factory function
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models
    from models import Superhero

    @app.route("/")
    def index():
        """
        Root route to confirm API is running
        """
        return jsonify({"message": "Welcome to the Superheroes API!"})

    @app.route("/superheroes", methods=["GET"])
    def get_superheroes():
        """
        GET /superheroes
        Returns a list of all superheroes
        """
        superheroes = Superhero.query.all()

        result = []
        for hero in superheroes:
            result.append({
                "id": hero.id,
                "name": hero.name,
                "power": hero.power
            })

        return jsonify(result), 200

    return app


