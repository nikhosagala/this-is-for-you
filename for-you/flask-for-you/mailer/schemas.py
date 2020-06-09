from mailer import ma
from mailer.models import EmailToSend
from marshmallow.fields import DateTime


class SendEmailSchema(ma.SQLAlchemyAutoSchema):
    send_date = DateTime(required=True, format='%d-%m-%YT%H:%M')

    class Meta:
        model = EmailToSend
