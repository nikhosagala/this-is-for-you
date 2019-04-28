from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restful import Api

from src.resources.emails import SendEmail
from src.resources.hello import HelloWorld
from src.utils.models import db

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
ma = Marshmallow(app)

db.init_app(app)

api.add_resource(HelloWorld, '/')
api.add_resource(SendEmail, '/send_email')
