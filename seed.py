from app import create_app
from models import db, Hero, Power, HeroPower

app = create_app()

with app.app_context():
    print("🌱 Starting database seeding...")

    # --- Clear existing data ---
    HeroPower.query.delete()
    Hero.query.delete()
    Power.query.delete()
    db.session.commit()
    print("🗑️ Cleared existing data.")

    # --- Create heroes ---
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
    ]
    db.session.add_all(heroes)
    db.session.commit()
    print(f"🦸 Created {len(heroes)} heroes.")

    # --- Create powers ---
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
    db.session.add_all(powers)
    db.session.commit()
    print(f"⚡ Created {len(powers)} powers.")

    # --- Assign powers to heroes ---
    hero_powers = [
        HeroPower(hero_id=heroes[0].id, power_id=powers[0].id, strength="Strong"),
        HeroPower(hero_id=heroes[1].id, power_id=powers[2].id, strength="Average"),
        HeroPower(hero_id=heroes[2].id, power_id=powers[1].id, strength="Strong"),
    ]
    db.session.add_all(hero_powers)
    db.session.commit()
    print(f"💥 Assigned powers to {len(hero_powers)} heroes.")

    print("✅ Database seeding complete!")
