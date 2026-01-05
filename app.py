from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from models import Superhero

    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    @app.route("/superheroes", methods=["GET"])
    def get_superheroes():
        heroes = Superhero.query.all()
        return jsonify([
            {"id": h.id, "name": h.name, "power": h.power}
            for h in heroes
        ])

    @app.route("/superheroes", methods=["POST"])
    def create_superhero():
        if not request.is_json:
            return jsonify({"error": "Request must be JSON"}), 400

        data = request.get_json()

        name = data.get("name")
        power = data.get("power")

        if not name or not power:
            return jsonify({"error": "Name and power are required"}), 400

        new_hero = Superhero(name=name, power=power)
        db.session.add(new_hero)
        db.session.commit()

        return jsonify({
            "id": new_hero.id,
            "name": new_hero.name,
            "power": new_hero.power
        }), 201

    return app
