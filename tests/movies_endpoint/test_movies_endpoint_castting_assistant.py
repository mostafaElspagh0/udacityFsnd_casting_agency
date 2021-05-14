import os
from flask.app import Flask
from flask.wrappers import Response


def test_get_movies_endpoint_return_200_if_castting_assistant(client: Flask, casting_assistant_headers):
    rv: Response = client.get('/movies', headers=casting_assistant_headers)
    assert rv.status_code == 200
    assert rv.content_type == "application/json"


def test_delete_movies_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.delete('/movies/1',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_patch_movies_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.patch('/movies/1',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_post_movies_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.post('/movies',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"
