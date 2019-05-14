from http import HTTPStatus

from flask import current_app as app, request
from flask_restful import Resource

from src.utils.faker import create_fake_user


class Status(Resource):
    def get(self):
        return {'version': app.config.get('API_VERSION')}


class Faker(Resource):
    def post(self):
        request_data = request.get_json()
        faker_type = request_data.get('type', 'person')
        total = request_data.get('total', 10)
        if faker_type == 'user':
            create_fake_user(total=total)
            return {'message': 'Ok'}, HTTPStatus.OK
        else:
            return HTTPStatus.NOT_IMPLEMENTED
