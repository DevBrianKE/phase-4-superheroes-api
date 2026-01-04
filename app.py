from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """
    Flask application factory
    """
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Import models so migrations detect them
    from models import Superhero

    # --- Routes ---
    
    @app.route('/')
    def home():
        """
        Home route to check if app is running
        """
        return jsonify({"message": "Welcome to the Superheroes API!"})

    @app.route('/superheroes', methods=['GET'])
    def get_superheroes():
        """
        Returns a list of all superheroes in the database
        """
        superheroes = Superhero.query.all()
        result = [{"id": hero.id, "name": hero.name, "power": hero.power} for hero in superheroes]
        return jsonify(result)

    return app

# Optional: for direct use (not needed if using manage.py)
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
