import os
from tests.utils import login_util
from flask import Flask, Response
from flask.wrappers import Request
import pytest
from app import create_app


@pytest.fixture
def client():
    return create_app().test_client()


@pytest.fixture
def casting_assistant_token():
    username = os.getenv("CASTING_ASSISTANT_USER")
    password = os.getenv("CASTING_ASSISTANT_PWD")
    return login_util(username, password)


@pytest.fixture
def casting_director_token():
    username = os.getenv("CASTING_DIRECTOR_USER")
    password = os.getenv("CASTING_DIRECTOR_PWD")
    return login_util(username, password)


@pytest.fixture
def executive_producer_token():
    username = os.getenv("EXECUTIVE_PRODUCER_USER")
    password = os.getenv("EXECUTIVE_PRODUCER_PWD")
    return login_util(username, password)
