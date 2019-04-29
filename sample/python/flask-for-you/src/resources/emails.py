from http import HTTPStatus

from flask import request
from flask_restful import Resource

from src.utils.databases import commit_to_db
from src.utils.marsmallow import schema_load
from src.utils.models import EmailToSend
from src.utils.schemas import SendEmailSchema


class SendEmail(Resource):
    def post(self):
        json_data = request.get_json()
        data = schema_load(SendEmailSchema(), json_data)
        send_email = EmailToSend(**data)
        commit_to_db(send_email)
        return dict(message='ok'), HTTPStatus.CREATED
