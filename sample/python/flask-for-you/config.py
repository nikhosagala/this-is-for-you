import os

SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI',
                                         'postgres://flask_userforyou:passwordforyou@localhost:5432/flask_foryou')

SQLALCHEMY_TRACK_MODIFICATIONS = True

API_VERSION = os.environ.get('API_VERSION', '0.0.0')
