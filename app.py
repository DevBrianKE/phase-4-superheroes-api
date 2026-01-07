from flask import Flask, jsonify
from flask_migrate import Migrate
import models              # import the module (registers model classes and exposes models.db)

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize the db and migrations using the db instance from models.py
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    # Basic health route
    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    # (Optional) quick test route to verify models are importable
    @app.route("/_models")
    def list_models():
        # simple check to ensure models import ok
        return jsonify({
            "has_hero": hasattr(models, "Hero"),
            "has_power": hasattr(models, "Power"),
            "has_hero_power": hasattr(models, "HeroPower")
        })

    return app
