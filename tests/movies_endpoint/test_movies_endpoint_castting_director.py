from operator import ne
from flask.app import Flask
from flask.wrappers import Response
import json
from datetime import datetime


def test_get_movies_endpoint_return_200_if_castting_director(client: Flask, casting_director_headers):
    rv: Response = client.get('/movies', headers=casting_director_headers)
    assert rv.status_code == 200
    assert rv.content_type == "application/json"


def test_post_movies_endpoint_return_401_if_castting_director(client: Flask, casting_director_headers):
    data = json.dumps(
        {
            "title": "avengers",
            "release_date": str(datetime.now())
        }
    )
    rv: Response = client.post(
        '/movies', headers=casting_director_headers, content_type='application/json', data=data)
    assert rv.status_code == 401
    assert rv.json == {
        "code": "AuthError",
        "error": {
            "code": "invalid_permissions",
            "description": "User does not have enough privileges"
        },
        "success": False
    }


def test_delete_movies_endpoint_return_401_if_castting_director(client: Flask, casting_director_headers):
    rv: Response = client.delete(
        '/movies/1', headers=casting_director_headers)
    assert rv.status_code == 401
    assert rv.content_type == "application/json"


def test_patch_movies_endpoint_return_202_if_castting_director_and_exist(client: Flask, casting_director_headers):
    pass
    #TODO:// implement this test
