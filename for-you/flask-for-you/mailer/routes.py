import http

from flask import Blueprint, request, jsonify, current_app

from mailer.models import EmailToSend
from mailer.schemas import SendEmailSchema

mailer_blueprint = Blueprint("mailer", __name__, url_prefix="/")


@mailer_blueprint.route("send_email", methods=("POST",))
def send_email():
    if request.data.decode("utf-8"):
        schema = SendEmailSchema()
        request_data = schema.load(request.json)
        email = EmailToSend(**request_data)
        email.save()
        return jsonify({"message": "ok"}), http.HTTPStatus.CREATED
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
