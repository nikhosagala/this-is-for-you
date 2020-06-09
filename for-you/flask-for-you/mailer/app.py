import os

from celery import Celery
from flask import Flask


def create_app(test=False):
    flask_app = Flask(__name__)

    if test:
        flask_app.config.from_object("mailer.config.ConfigTest")
    else:
        flask_app.config.from_object("mailer.config.Config")

    register_extension(flask_app)
    register_blueprints(flask_app)

    return flask_app


def make_celery(app=None):
    app = app or create_app()
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
    celery_instance = Celery(
        app.import_name,
        backend=app.config["CELERY_RESULT_BACKEND"],
        broker=app.config["CELERY_BROKER_URL"],
    )
    celery_instance.conf.update(app.config)

    class ContextTask(celery_instance.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_instance.Task = ContextTask
    return celery_instance


def register_extension(app: Flask):
    """Register Flask extensions."""
    ma.init_app(app)


def register_blueprints(app: Flask):
    """Register Flask extensions."""
    app.register_blueprint(helper_blueprint)
    app.register_blueprint(rdl_blueprint)
    app.register_blueprint(payment_blueprint)
