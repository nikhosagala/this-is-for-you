from http import HTTPStatus

from flask import request, current_app
from flask_restful import Resource

from mailer.marsmallow import schema_load
from mailer.models import EmailToSend
from mailer.schemas import SendEmailSchema


class SendEmail(Resource):
    def post(self):
        from mailer.app import db
        json_data = request.get_json()
        data = schema_load(SendEmailSchema(), json_data)
        send_email = EmailToSend(**data)
        db.session.add(send_email)
        db.session.commit()
        return dict(message='ok'), HTTPStatus.CREATED


class ProcessEmail(Resource):
    def get(self):
        from mailer.scripts import check_email_to_send
        check_email_to_send()


class Status(Resource):
    def get(self):
        return {'version': current_app.config.get('API_VERSION')}


class Faker(Resource):
    def post(self):
        from mailer.faker import create_fake_user
        request_data = request.get_json()
        faker_type = request_data.get('type', 'person')
        total = request_data.get('total', 10)
        if faker_type == 'user':
            create_fake_user(total=total)
            return {'message': 'Ok'}, HTTPStatus.OK
        else:
            return HTTPStatus.NOT_IMPLEMENTED
