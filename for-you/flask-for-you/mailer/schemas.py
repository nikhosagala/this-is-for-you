from datetime import datetime

from marshmallow import validates, ValidationError

from mailer import ma
from mailer.models import EmailToSend
from marshmallow.fields import DateTime


class SendEmailSchema(ma.SQLAlchemyAutoSchema):
    send_date = DateTime(required=True, format="%d-%m-%YT%H:%M")

    @validates("send_date")
    def validate_send_date(self, value):
        now = datetime.now()
        if value < now:
            raise ValidationError("date must be in the future")

    class Meta:
        model = EmailToSend
