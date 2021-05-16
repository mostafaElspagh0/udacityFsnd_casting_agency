from .db import db


actor_movie_table = db.Table('actor_movie',
                           db.Column(
                               'actor_id',
                               db.Integer,
                               db.ForeignKey('actor.id')),
                           db.Column(
                               'movie_id',
                               db.Integer,
                               db.ForeignKey('movie.id'))
                           )
