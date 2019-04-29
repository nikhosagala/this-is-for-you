from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin(object):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    modified = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class EmailToSend(BaseModelMixin, db.Model):
    __tablename__ = 'email_to_send'

    event_id = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
    send_date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Boolean, default=False)


class User(BaseModelMixin, db.Model):
    __tablename__ = 'user'

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
