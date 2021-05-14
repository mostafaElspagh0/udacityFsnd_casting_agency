import os
import flask_migrate
from tests.utils import login_util
import pytest
from src.app import create_app

os.environ["ALLOW_EXPIRED_TOKENS"] = "1"


@pytest.fixture
def client():
    os.system("rm /tmp/foo.db")
    app = create_app()
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/foo.db"
    with app.app_context() as k:
        flask_migrate.upgrade()
    return app.test_client()


@pytest.fixture
def new_casting_assistant_token():
    username = os.getenv("CASTING_ASSISTANT_USER")
    password = os.getenv("CASTING_ASSISTANT_PWD")
    return login_util(username, password)


@pytest.fixture
def new_casting_director_token():
    username = os.getenv("CASTING_DIRECTOR_USER")
    password = os.getenv("CASTING_DIRECTOR_PWD")
    return login_util(username, password)


@pytest.fixture
def new_executive_producer_token():
    username = os.getenv("EXECUTIVE_PRODUCER_USER")
    password = os.getenv("EXECUTIVE_PRODUCER_PWD")
    return login_util(username, password)


@pytest.fixture
def casting_assistant_headers():
    expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilk1S3MwNE5KTGhfcWl4eC1Mc3AzVSJ9.eyJpc3MiOiJodHRwczovL2hhcHB5MjAwMC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5OGEyODQ5MjAxMzkwMDY4ZWQxYWVmIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC86NTAwMCIsImlhdCI6MTYyMDk2NDA0NywiZXhwIjoxNjIwOTcxMjQ3LCJhenAiOiJrN1pFcU95Qm9QVXMyenF3NXhCSGgxeXRNcnpwbWE2NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.Ae1Xxby-c4dnItyOzC3v9VG_dH9kf3cYwe1TH9uyKeSAgJLKGqfx_-CiuB70Ed8Eb7I2_vzR8uitRAwWjDHGUVNFE1UnYXd03tIVrtH9ycSQ7QTAREUiORE3csajGa2htDLWGGDFRTF9FnbADxPcozW3z8j-hjYC7xb4qntj1O4rQMxovfAjEtuc6D9hHlnxc3aM-Ib2RftxAsnwJTK5f5fwgjPyd_iSjWMWZMnV1IKHWOcEZu5IrcPrA1NlDu77y2cRQwa8NNalYNX-SYaL9qrvqR4DtvunDG5dzCwuVy_tK5hLdLx9QyF3taI2vDep8KRDTPMhQ_q_vN68WLIX5w'
    headers = {
        "Authorization": f"Bearer {expired_token}"
    }
    return headers


@pytest.fixture
def casting_director_headers():
    expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilk1S3MwNE5KTGhfcWl4eC1Mc3AzVSJ9.eyJpc3MiOiJodHRwczovL2hhcHB5MjAwMC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5OGEyZDRiNzQzYTkwMDZhMGEzMWQyIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC86NTAwMCIsImlhdCI6MTYyMDk2NzU0NywiZXhwIjoxNjIwOTc0NzQ3LCJhenAiOiJrN1pFcU95Qm9QVXMyenF3NXhCSGgxeXRNcnpwbWE2NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyJdfQ.fFsPZcQ24Sqd3Z4Il0XgHA3MnbUwMfoKy1lituTNRLmEuLE_FHjAF68VNkIYjnSv9WF-EP04NJdB17HyVbh3rXNF-Pfc7c0XK-g62cDnSlVp3fDu28BLKVQ7pp9KKYB6CI3IFo107barYMlJw-Ah-FmkTvlRAvNO_JNw15D1gcF5wTGOm9ms4C7viby1q6-lROMV96g6iuex96kjYbEFeP7MLTJhOZ8Aoel37wx2lBOM9NDCzFT5cXnKfDhZPtMrjvDrkWeE2IvbxfANp4PZe3cW6EuPe9XePK4iFw0KaIjvZrL5nzjF8bIwAiuQJuDWzvQcv07-ln91rtdxjwMY4w'
    headers = {
        "Authorization": f"Bearer {expired_token}"
    }
    return headers


@pytest.fixture
def executive_producer_headers():
    expired_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ilk1S3MwNE5KTGhfcWl4eC1Mc3AzVSJ9.eyJpc3MiOiJodHRwczovL2hhcHB5MjAwMC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjA5OGEzMzViMWNjNTgwMDcxZDBlYzkwIiwiYXVkIjoiaHR0cDovL2xvY2FsaG9zdC86NTAwMCIsImlhdCI6MTYyMTAyMzY0MiwiZXhwIjoxNjIxMDMwODQyLCJhenAiOiJrN1pFcU95Qm9QVXMyenF3NXhCSGgxeXRNcnpwbWE2NyIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiYWRkOmFjdG9ycyIsImFkZDptb3ZpZXMiLCJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIl19.h-V1pxh6U9emSfzZkEkiJ2ZJ6qaLmUhfIvqS4iTKZ-1umHZNwc10Y6RUkrULgWf0VWwvrXxkawonrYQ557w6CgDO5--ik9b9-YIA0axLcJSeAGt2E_8_8fX4mQfwqoipCIO9Pwza_RyO6NmBMc8_Ldo7YmhH17SB2A4rkeQBygAxKl8zATpCSMyE0z9Xv07qRfykavRM5lBXqeO9BMmqsEBpgyO5-H2TKoBF1BRd-HRm5Ov1yt9chlWZRREoZS0lFLLRuETO3fz2CF28y_UGcJFr0OkKpR6lcEm0YsMJtYU2b6oNqe0C03-QJJJ1xhnZSOxEnGghs-0mLDwmqWvecw'
    headers = {
        "Authorization": f"Bearer {expired_token}"
    }
    return headers

