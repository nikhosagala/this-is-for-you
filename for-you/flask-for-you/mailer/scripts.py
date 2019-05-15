from mailer.models import EmailToSend, User
from mailer.tasks import send_email


def check_email_to_send():
    emails = EmailToSend.query.filter_by(status=False)
    if emails:
        for email in emails:
            search_user(email)


def search_user(email):
    users = User.query.all()
    for user in users:
        send_email.delay(user.id, email.id)
