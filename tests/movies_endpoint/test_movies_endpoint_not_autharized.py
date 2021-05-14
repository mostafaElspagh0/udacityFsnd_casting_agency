from flask.app import Flask
from flask.wrappers import Response


def test_get_movies_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.get('/movies')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_delete_movies_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.delete('/movies/1')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_patch_movies_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.patch('/movies/1')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_post_movies_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.post('/movies')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"
