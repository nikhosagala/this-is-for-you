import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'postgres://userforflask:passwordforflask@localhost:5433/dbforflask')

SQLALCHEMY_TRACK_MODIFICATIONS = True

API_VERSION = os.environ.get('API_VERSION', '0.0.0')

CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'rpc')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'amqp://rabbituser:rabbitpassword@localhost:5672')
