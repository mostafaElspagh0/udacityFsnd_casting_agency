# Casting Agency API
an api to make managing casting agency easier
## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://casting123.herokuapp.com/

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

To run the server, execute:

```bash
export ALGORITHMS="RS256"
export AUTH0_DOMAIN="happy2000.us.auth0.com"
export API_AUDIENCE="http://localhost/:5000"
export DATABASE_URL=<database-connection-url>
export FLASK_APP=app.py
flask db migrate
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://casting123.herokuapp.com/`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root (or health) endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- Casting Assistant
  - Can view actors and movies
- Casting Director
  - All permissions a `Casting Assistant` has and…
  - Add or delete an actor from the database
  - Modify actors or movies
- Executive Producer
  - All permissions a `Casting Director has and…
  - Add or delete a movie from the database



## Testing
For testing the backend, run the following commands (in the exact order):
```
python -m pytest
```