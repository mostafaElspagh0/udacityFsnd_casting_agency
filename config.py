import os

HELLOWORLD = "hello from config"

temp_databaseuri= os.getenv("DATABASE_URL")
if "postgresql" not in temp_databaseuri:
    temp_databaseuri.replace("postgres","postgresql")
SQLALCHEMY_DATABASE_URI = temp_databaseuri

SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")

ALGORITHMS = [i.strip() for i in os.getenv("ALGORITHMS").split(",")]

API_AUDIENCE = os.getenv("API_AUDIENCE")

DEBUG = True
