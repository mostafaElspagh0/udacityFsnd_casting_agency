import os
from flask.app import Flask
from flask.wrappers import Response


def test_get_actors_endpoint_return_401_if_castting_assistant(client: Flask, casting_assistant_headers):
    rv: Response = client.get('/actors', headers=casting_assistant_headers)
    assert rv.status_code == 200
    assert rv.content_type == "application/json"


def test_delete_actors_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.delete('/actors/1',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_patch_actors_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.patch('/actors/1',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_post_actors_endpoint_return_401_if_castting_assistant(client: Flask,casting_assistant_headers):
    rv: Response = client.post('/actors',headers=casting_assistant_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"
