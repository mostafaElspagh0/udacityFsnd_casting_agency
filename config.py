import os

HELLOWORLD = "hello from config"

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL").replace("postgres","postgresql")

SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")

ALGORITHMS = [i.strip() for i in os.getenv("ALGORITHMS").split(",")]

API_AUDIENCE = os.getenv("API_AUDIENCE")

DEBUG = True
