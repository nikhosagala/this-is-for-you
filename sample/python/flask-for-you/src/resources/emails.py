import json
from http import HTTPStatus

from flask import request
from flask_restful import Resource

from src.utils.schemas import SendEmailSchema
from src.utils.marsmallow import schema_load


class SendEmail(Resource):
    def post(self):
        json_data = request.get_json()
        data = schema_load(SendEmailSchema(), json_data)
        return json.dumps(dict(message='ok')), HTTPStatus.OK
