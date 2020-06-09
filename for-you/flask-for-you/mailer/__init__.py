import os

from celery import Celery
from flask import Flask
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()


def create_app(test=False):
    app = Flask(__name__, instance_relative_config=False)

    if test:
        app.config.from_object("config.TestConfig")
    else:
        app.config.from_object("config.Config")

    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from mailer.routes import mailer_blueprint

        app.register_blueprint(mailer_blueprint)

    return app


def make_celery(app=None):
    app = app or create_app()
    os.environ.setdefault("FORKED_BY_MULTIPROCESSING", "1")
    celery_instance = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )

    class ContextTask(celery_instance.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_instance.Task = ContextTask
    return celery_instance
