from sqlalchemy.orm import relationship
from ..association_tables import actor_movie_table
from ..db import db


class Actor(db.Model):

    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=False)
    gender = db.Column(db.String(30), unique=False, nullable=False)

    movies = relationship(
        "Movie",
        secondary=actor_movie_table,
        back_populates="actors")

    def __repr__(self):
        return f'<Actor {self.id},{self.name},{self.age},{self.gender}>'

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender
        }
