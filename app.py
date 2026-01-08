from flask import Flask, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/superheroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    # --- Index route ---
    @app.route("/")
    def index():
        return jsonify({"message": "Welcome to the Superheroes API!"})

    # --- HERO ROUTES ---

    # GET all heroes
    @app.route("/heroes", methods=["GET"])
    def get_heroes():
        heroes = Hero.query.all()
        return jsonify([{
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        } for hero in heroes]), 200

    # GET hero by ID
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

    # --- POWER ROUTES ---

    # GET all powers
    @app.route("/powers", methods=["GET"])
    def get_powers():
        powers = Power.query.all()
        return jsonify([{
            "id": power.id,
            "name": power.name,
            "description": power.description
        } for power in powers]), 200

    # GET power by ID
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

    # PATCH power (update description)
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

    # --- HEROPOWER ROUTE ---

    # POST hero_power
    @app.route("/hero_powers", methods=["POST"])
    def create_hero_power():
        data = request.get_json()
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")
        strength = data.get("strength")

        # Validation
        if strength not in ["Strong", "Weak", "Average"]:
            return jsonify({"errors": ["Strength must be Strong, Weak, or Average"]}), 400

        hero = Hero.query.get(hero_id)
        power = Power.query.get(power_id)

        if not hero or not power:
            return jsonify({"errors": ["Hero or Power not found"]}), 404

        hero_power = HeroPower(
            hero_id=hero.id,
            power_id=power.id,
            strength=strength
        )

        db.session.add(hero_power)
        db.session.commit()

        return jsonify({
            "id": hero_power.id,
            "hero_id": hero.id,
            "power_id": power.id,
            "strength": strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
        }), 201

    return app

# --- Run server ---
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
