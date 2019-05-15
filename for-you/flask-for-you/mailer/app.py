import os

from celery import Celery
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

from mailer.models import db
from mailer.views import Status, SendEmail, ProcessEmail, Faker


def make_celery(application):
    os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
    celery_instance = Celery(
        application.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )

    class ContextTask(celery_instance.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_instance.Task = ContextTask
    return celery_instance


app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
ma = Marshmallow(app)

db.init_app(app)

api.add_resource(Status, '/status')
api.add_resource(SendEmail, '/send_email')
api.add_resource(ProcessEmail, '/process_email')
api.add_resource(Faker, '/faker')
