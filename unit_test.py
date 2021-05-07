from flask import Flask,Response
import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


def test_root_endpoint_return_404(client: Flask):
    rv: Response = client.get('/')
    assert rv.status_code == 404
