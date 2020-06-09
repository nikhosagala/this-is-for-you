from mailer import make_celery, create_app
from mailer.models import EmailToSend, User

app = create_app()
celery = make_celery(app)


@celery.task
def send_pending_email(email_to_send_id: int):
    app.app_context().push()
    users = User.query.filter_by(is_active=True)
    print("sending email to: ")
    print(users.all())
    email = EmailToSend.query.get(email_to_send_id)
    print(f"sending email with subject {email.subject}")
