from src.utils.models import EmailToSend, User


def check_email_to_send():
    emails = EmailToSend.query.filter_by(status=False)
    if emails:
        for email in emails:
            search_user(email)


def search_user(email):
    from src.utils.tasks import send_email
    users = User.query.all()
    for user in users:
        send_email.delay(user.id, email.id)
