import os


class DatabaseUri:
    type = 'sqlite'
    name = "trivia_dev"
    host = 'localhost'
    port = 5432
    username = os.getenv('DATABASE_USERNAME')
    password = os.getenv('DATABASE_PASSWORD')
    sqlite_path = "/tmp/test.db"

    def __str__(self):

        if self.type == 'sqlite':
            return f"sqlite:///{self.sqlite_path}"

        return f"{self.type}: // {self.username}: {self.password}@"
        f"{self.host}: {self.port}/{self.name}"


HELLOWORLD = "hello from config"

SQLALCHEMY_DATABASE_URI = str(DatabaseUri())

SQLALCHEMY_TRACK_MODIFICATIONS = False

AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")

ALGORITHMS = [i.strip() for i in os.getenv("ALGORITHMS"), split(",")]

API_AUDIENCE = os.getenv("API_AUDIENCE")
