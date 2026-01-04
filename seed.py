from app import create_app, db
from models import Superhero

app = create_app()

# Run seeding within the app context
with app.app_context():
    # Clear existing data
    Superhero.query.delete()

    # List of superheroes to seed
    superheroes = [
        {"name": "Superman", "power": "Super Strength"},
        {"name": "Batman", "power": "Genius Intellect"},
        {"name": "Wonder Woman", "power": "Super Strength & Agility"},
        {"name": "Flash", "power": "Super Speed"},
        {"name": "Green Lantern", "power": "Power Ring"},
    ]

    # Add superheroes to the session
    for hero in superheroes:
        new_hero = Superhero(name=hero["name"], power=hero["power"])
        db.session.add(new_hero)

    # Commit to database
    db.session.commit()
    print(f"Seeded {len(superheroes)} superheroes!")
