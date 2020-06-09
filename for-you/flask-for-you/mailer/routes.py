import http

from flask import Blueprint, request, jsonify, current_app
from marshmallow import ValidationError

from mailer.models import EmailToSend
from mailer.schemas import SendEmailSchema

mailer_blueprint = Blueprint("mailer", __name__, url_prefix="/")


@mailer_blueprint.route("send_email", methods=("POST",))
def send_email():
    if request.data.decode("utf-8"):
        from mailer.tasks import send_pending_email

        schema = SendEmailSchema()
        try:
            request_data = schema.load(request.json)
            email = EmailToSend(**request_data)
            email.save()
            send_pending_email.apply_async((email.id,), countdown=3)
            return jsonify({"message": "ok"}), http.HTTPStatus.CREATED
        except ValidationError as e:
            return jsonify({"message": e.messages}), http.HTTPStatus.BAD_REQUEST
    return jsonify({"message": "No data given"}), http.HTTPStatus.BAD_REQUEST


@mailer_blueprint.route("faker", methods=("POST",))
def faker():
    if request.data.decode("utf-8"):
        from mailer.faker import create_fake_user

        request_data = request.get_json()
        faker_type = request_data.get("type", "user")
        total = request_data.get("total", 10)
        if faker_type == "user":
            create_fake_user(total=total)
            return {"message": "Ok"}, http.HTTPStatus.OK
        else:
            return http.HTTPStatus.NOT_IMPLEMENTED
    return jsonify({"message": "No data given"}), http.HTTPStatus.BAD_REQUEST


@mailer_blueprint.route("version", methods=("GET",))
def version():
    return {"version": current_app.config.get("API_VERSION")}
