from mailer import db


class BaseModelMixin(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated = db.Column(
        db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False
    )
    is_active = db.Column(db.Boolean, default=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)


class EmailToSend(BaseModelMixin):
    __tablename__ = 'email_to_send'

    event_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    send_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, default=False)


class User(BaseModelMixin):
    __tablename__ = 'user'

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
