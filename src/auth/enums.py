from enum import Enum


class Permissions(Enum):
    get_actors = "get:actors"
    delete_actors = "delete:actors"
    add_actors = 'add:actors'
    patch_actors = 'patch:actors'
    get_movies = 'get:movies'
    delete_movies = 'delete:movies'
    add_movies = 'add:movies'
    patch_movies = 'patch:movies'
