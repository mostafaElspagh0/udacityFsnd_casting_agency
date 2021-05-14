from flask import Flask, Response


def test_root_endpoint_return_healthy(client: Flask):
    rv: Response = client.get('/')
    assert rv.status_code == 200
