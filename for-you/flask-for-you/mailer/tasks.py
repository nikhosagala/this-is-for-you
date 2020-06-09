from mailer.app import make_celery
from mailer.models import User, EmailToSend

celery = make_celery()


@celery.task()
def send_email(user_id: int, email_to_send_id: str):
    user = User.query.get(user_id)
    email = EmailToSend.query.get(email_to_send_id)
    print(f"sending email {email.subject} to {user.email}")
