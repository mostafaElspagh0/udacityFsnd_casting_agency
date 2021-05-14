from flask.app import Flask
from flask.wrappers import Response


def test_get_actors_endpoint_return_401_if_unauthorized(client: Flask,):
    rv: Response = client.get('/actors')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_delete_actors_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.delete('/actors/1')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_patch_actors_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.patch('/actors/1')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_post_actors_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.post('/actors')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"
