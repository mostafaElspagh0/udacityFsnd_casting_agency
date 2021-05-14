from operator import ne
import os
from flask.app import Flask
from flask.wrappers import Response
import json
from time import sleep


def test_post_actors_endpoint_return_201_if_castting_director(client: Flask, casting_director_token):
    data = json.dumps(
        {
            "name": "mostafa",
            "age": 21,
            "gender": "male"
        }
    )
    rv: Response = client.post(
        '/actors', headers=casting_director_token, content_type='application/json', data=data)
    assert rv.status_code == 201
    assert rv.json == {
        'actors': [
            {
                'age': 21,
                'gender': 'male',
                'id': 1,
                'name': 'mostafa'
            }
        ],
        'code': 'created',
        'success': True
    }
    assert rv.json["actors"][0]['id'] == 1
    assert rv.content_type == "application/json"


def test_get_actors_endpoint_return_200_if_castting_director(client: Flask, casting_director_token):
    rv: Response = client.get('/actors', headers=casting_director_token)
    assert rv.status_code == 200
    assert rv.content_type == "application/json"


def test_get_actors_by_id_endpoint_return_200_if_castting_assistant_and_exist(client: Flask, casting_director_token):
    data = json.dumps(
        {
            "name": "mostafa",
            "age": 21,
            "gender": "male"
        }
    )
    rv: Response = client.post(
        '/actors', headers=casting_director_token, content_type='application/json', data=data)
    rv: Response = client.get(
        '/actors/1', headers=casting_director_token)
    assert rv.status_code == 200
    assert rv.json["actors"] == [{
        'age': 21,
        'gender': 'male',
        'id': 1,
        'name': 'mostafa'
    }]

    assert rv.json["actors"][0]['id'] == 1
    assert rv.content_type == "application/json"


def test_get_actors_by_id_endpoint_return_404_if_castting_assistant_and_not_exist(client: Flask, casting_director_token):
    rv: Response = client.get(
        '/actors/1', headers=casting_director_token)
    assert rv.status_code == 404
    assert rv.content_type == "application/json"


def test_delete_actors_endpoint_return_202_if_castting_director_and_exist(client: Flask, casting_director_token):
    data = json.dumps(
        {
            "name": "mostafa",
            "age": 21,
            "gender": "male"
        }
    )
    rv: Response = client.post(
        '/actors', headers=casting_director_token, content_type='application/json', data=data)
    rv: Response = client.delete(
        '/actors/1', headers=casting_director_token)
    assert rv.status_code == 202
    assert rv.content_type == "application/json"


def test_delete_actors_endpoint_return_200_if_castting_director_and_not_exist(client: Flask, casting_director_token):
    rv: Response = client.delete(
        '/actors/1', headers=casting_director_token)
    assert rv.status_code == 404
    assert rv.content_type == "application/json"


def test_patch_actors_endpoint_return_202_if_castting_director_and_exist(client: Flask, casting_director_token):
    data = {
        "name": "mostafa",
        "age": 21,
        "gender": "male"
    }

    rv: Response = client.post(
        '/actors', headers=casting_director_token, content_type='application/json', data=json.dumps(data))
    data["name"] = "mohamed"
    rv: Response = client.patch(
        '/actors/1', headers=casting_director_token, content_type='application/json', data=json.dumps(data))
    assert rv.status_code == 202
    assert rv.json["actors"][0]["name"] == "mohamed"
    assert rv.content_type == "application/json"
    rv: Response = client.get(
        '/actors/1', headers=casting_director_token)
    assert rv.json["actors"] == [{
        'age': 21,
        'gender': 'male',
        'id': 1,
        'name': 'mohamed'
    }]
    assert rv.content_type == "application/json"


def test_patch_actors_endpoint_return_404_if_castting_director_and_not_exist(client: Flask, casting_director_token):
    data = {
        "name": "mostafa",
        "age": 21,
        "gender": "male"
    }
    rv: Response = client.patch(
        '/actors/1', headers=casting_director_token, content_type='application/json', data=json.dumps(data))
    assert rv.status_code == 404
    assert rv.content_type == "application/json"
