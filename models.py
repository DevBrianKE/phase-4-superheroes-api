
from app import db

class Superhero(db.Model):
    """
    Superhero model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    power = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Superhero {self.name}>"
