from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    @app.route("/heroes", methods=["GET"])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes]), 200

    @app.route("/heroes", methods=["POST"])
    def create_hero():
        data = request.get_json()

        name = data.get("name")
        super_name = data.get("super_name")

        if not name or not super_name:
            return jsonify({"error": "Name and super_name are required"}), 400

        hero = Hero(name=name, super_name=super_name)
        db.session.add(hero)
        db.session.commit()

        return jsonify(hero.to_dict()), 201

    @app.route("/heroes/<int:id>", methods=["GET"])
    def get_hero(id):
        hero = Hero.query.get(id)

        if not hero:
            return jsonify({"error": "Hero not found"}), 404

        return jsonify({
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name,
            "hero_powers": [
                {
                    "id": hp.id,
                    "hero_id": hp.hero_id,
                    "power_id": hp.power_id,
                    "strength": hp.strength,
                    "power": {
                        "id": hp.power.id,
                        "name": hp.power.name,
                        "description": hp.power.description
                    }
                } for hp in hero.hero_powers
            ]
        }), 200

    @app.route("/powers", methods=["GET"])
    def get_powers():
        powers = Power.query.all()
        return jsonify([
            {
                "id": power.id,
                "name": power.name,
                "description": power.description
            } for power in powers
        ]), 200

    @app.route("/powers/<int:id>", methods=["GET"])
    def get_power(id):
        power = Power.query.get(id)

        if not power:
            return jsonify({"error": "Power not found"}), 404

        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    @app.route("/powers/<int:id>", methods=["PATCH"])
    def update_power(id):
        power = Power.query.get(id)

        if not power:
            return jsonify({"error": "Power not found"}), 404

        data = request.get_json()
        description = data.get("description")

        if not description or len(description) < 20:
            return jsonify({"errors": ["Description must be at least 20 characters"]}), 400

        power.description = description
        db.session.commit()

        return jsonify({
            "id": power.id,
            "name": power.name,
            "description": power.description
        }), 200

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
