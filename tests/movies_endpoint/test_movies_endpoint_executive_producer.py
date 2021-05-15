from operator import ne
import os
from flask.app import Flask
from flask.wrappers import Response
import json
from time import sleep


def test_post_movies_endpoint_return_201_if_executive_producer(client: Flask, executive_producer_headers):
    data = json.dumps(
        {
            "title": "avengere",
            "release_date": "2021-05-15 01:42:52.624318"
        }
    )
    rv: Response = client.post(
        '/movies', headers=executive_producer_headers, content_type='application/json', data=data)
    assert rv.status_code == 201
    assert rv.json["movies"][0]['id'] == 1
    assert rv.content_type == "application/json"


def test_get_movies_endpoint_return_200_if_executive_producer(client: Flask, executive_producer_headers):
    rv: Response = client.get('/movies', headers=executive_producer_headers)
    assert rv.status_code == 200
    assert rv.content_type == "application/json"


def test_get_movies_by_id_endpoint_return_200_if_executive_producer_and_exist(client: Flask, executive_producer_headers):
    data = json.dumps(
        {
            "title": "avengere",
            "release_date": "2021-05-15 01:42:52.624318"
        }
    )
    rv: Response = client.post(
        '/movies', headers=executive_producer_headers, content_type='application/json', data=data)
    rv: Response = client.get(
        '/movies/1', headers=executive_producer_headers)
    assert rv.status_code == 200
    assert rv.json["movies"] == [{
        'id': 1,
        "title": "avengere",
        "release_date": "Sat, 15 May 2021 01:42:52 GMT"
    }]

    assert rv.json["movies"][0]['id'] == 1
    assert rv.content_type == "application/json"


def test_get_movies_by_id_endpoint_return_404_if_executive_producer_and_not_exist(client: Flask, executive_producer_headers):
    rv: Response = client.get(
        '/movies/1', headers=executive_producer_headers)
    assert rv.status_code == 404
    assert rv.content_type == "application/json"


def test_delete_movies_endpoint_return_202_if_executive_producer_and_exist(client: Flask, executive_producer_headers):
    data = json.dumps(
        {
            "title": "avengere",
            "release_date": "2021-05-15 01:42:52.624318"
        }
    )
    rv: Response = client.post(
        '/movies', headers=executive_producer_headers, content_type='application/json', data=data)
    rv: Response = client.delete(
        '/movies/1', headers=executive_producer_headers)
    assert rv.status_code == 202
    assert rv.content_type == "application/json"


def test_delete_movies_endpoint_return_200_if_executive_producer_and_not_exist(client: Flask, executive_producer_headers):
    rv: Response = client.delete(
        '/movies/1', headers=executive_producer_headers)
    assert rv.status_code == 404
    assert rv.content_type == "application/json"


def test_patch_movies_endpoint_return_202_if_executive_producer_and_exist(client: Flask, executive_producer_headers):
    data = {
        "title": "avengere",
        "release_date": "2021-05-15 01:42:52.624318"
    }
    rv: Response = client.post(
        '/movies', headers=executive_producer_headers, content_type='application/json', data=json.dumps(data))
    data["title"] = "sucks"
    rv: Response = client.patch(
        '/movies/1', headers=executive_producer_headers, content_type='application/json', data=json.dumps(data))
    assert rv.status_code == 202
    assert rv.json["movies"][0]["title"] == "sucks"
    assert rv.content_type == "application/json"
    rv: Response = client.get(
        '/movies/1', headers=executive_producer_headers)
    assert rv.json["movies"] == [
        {
            'id': 1,
            'release_date': 'Sat, 15 May 2021 01:42:52 GMT', 'title': 'sucks',
        }
    ]
    assert rv.content_type == "application/json"


def test_patch_movies_endpoint_return_404_if_executive_producer_and_not_exist(client: Flask, executive_producer_headers):
    data = {
        "title": "avengere",
        "release_date": "2021-05-15 01:42:52.624318"
    }
    rv: Response = client.patch(
        '/movies/1', headers=executive_producer_headers, content_type='application/json', data=json.dumps(data))
    assert rv.status_code == 404
    assert rv.content_type == "application/json"
