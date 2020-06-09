from mailer import make_celery
from mailer.models import EmailToSend

celery = make_celery()


@celery.task
def send_pending_email(email_to_send_id: int):
    # TODO: figure out how to send flask app context so we can query
    # user = User.query.get(1)
    # email = EmailToSend.query.get(email_to_send_id)
    # print(f"sending email {email.subject}")
    print("sending email")
