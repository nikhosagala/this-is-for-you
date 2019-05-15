from mimesis import Person

from mailer.models import User


def create_fake_user(total: int = 100):
    from mailer.app import db
    person = Person('en')
    exist = User.query.first()
    if exist is None:
        for _ in range(total):
            user = User(name=person.name(), email=person.email())
            db.session.add(user)
            db.session.commit()
