from marshmallow import Schema
from marshmallow.fields import Integer, String, DateTime


class SendEmailSchema(Schema):
    event_id = Integer(required=True)
    subject = String(required=True)
    content = String(required=True)
    send_date = DateTime(required=True)
