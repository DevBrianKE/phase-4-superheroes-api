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

        new_hero = Superhero(name=name, power=data.get("power"))
        db.session.add(new_hero)
        db.session.commit()

        return jsonify({
            "id": new_hero.id,
            "name": new_hero.name,
            "power": new_hero.power
        }), 201

    @app.route("/superheroes/<int:id>", methods=["GET"])
    def get_superhero_by_id(id):
        """
        Fetch a single superhero by ID.
        Returns 404 if superhero does not exist.
        """
        superhero = Superhero.query.get(id)

        if not superhero:
            return {"error": "Superhero not found"}, 404

        return {
            "id": superhero.id,
            "name": superhero.name,
            "power": superhero.power
        }, 200

    @app.route("/superheroes/<int:id>", methods=["DELETE"])
    def delete_superhero(id):
        """
        Delete a superhero by ID.
        Returns 404 if superhero does not exist.
        """
        superhero = Superhero.query.get(id)

        if not superhero:
            return {"error": "Superhero not found"}, 404

        db.session.delete(superhero)
        db.session.commit()

        return {"message": "Superhero deleted successfully"}, 200

    return app
