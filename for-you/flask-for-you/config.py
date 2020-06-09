import os


class Config:
    _basedir = os.path.abspath(os.path.dirname(__file__))

    DB_USER = "userforflask"
    DB_PASS = "passwordforflask"
    DB_HOST = "localhost"
    DB_PORT = "5433"
    DB_NAME = "dbforflask"

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "SQLALCHEMY_DATABASE_URI",
        f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    API_VERSION = os.environ.get("API_VERSION", "0.0.1")

    CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "rpc")

    CELERY_BROKER_URL = os.environ.get(
        "CELERY_BROKER_URL", "amqp://rabbituser:rabbitpassword@localhost:5672"
    )
