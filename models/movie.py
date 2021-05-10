from db import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False, nullable=False)
    release_date = db.Column(db.DateTime, unique=False, nullable=False)

    def __repr__(self):
        return f'<Movie {self.id},{self.title},{self.release_date}>'

    def toDict(self):
        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
        }
