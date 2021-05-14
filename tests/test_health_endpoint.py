from flask import Flask, Response


def test_root_endpoint_return_healthy(client: Flask):
    rv: Response = client.get('/')
    assert rv.status_code == 200


def test_get_actors_endpoint_return_401_if_unauthorized(client: Flask):
    rv: Response = client.get('/actors')
    assert rv.status_code == 401
    assert rv.content_type == "application/json"
