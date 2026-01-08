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
        super_name = data.get("name")  # client sends "name"

        if not super_name:
            return jsonify({"error": "Hero name is required"}), 400

        hero = Hero(super_name=super_name)
        db.session.add(hero)
        db.session.commit()
        return jsonify(hero.to_dict()), 201

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
