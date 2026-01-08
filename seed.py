from app import create_app
from models import db, Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("🌱 Seeding database...")

    # Clear existing data
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()

    # Create heroes
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
    ]

    # Create powers
    powers = [
        Power(
            name="super strength",
            description="gives the wielder super-human strength beyond normal limits"
        ),
        Power(
            name="flight",
            description="gives the wielder the ability to fly through the skies at supersonic speed"
        ),
        Power(
            name="elasticity",
            description="can stretch the human body to extreme lengths with ease"
        ),
    ]

    db.session.add_all(heroes)
    db.session.add_all(powers)
    db.session.commit()

    # Create hero powers
    hero_powers = [
        HeroPower(hero_id=heroes[0].id, power_id=powers[0].id, strength="Strong"),
        HeroPower(hero_id=heroes[1].id, power_id=powers[2].id, strength="Average"),
        HeroPower(hero_id=heroes[2].id, power_id=powers[1].id, strength="Strong"),
    ]

    db.session.add_all(hero_powers)
    db.session.commit()

    print("✅ Done seeding!")
