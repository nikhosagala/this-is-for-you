from flask import Flask, jsonify
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
ma = Marshmallow()
mail = Mail()


def create_app(test=False):
    app = Flask(__name__, instance_relative_config=False)

    if test:
        app.config.from_object("config.TestConfig")
    else:
        app.config.from_object("config.Config")

    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)

    with app.app_context():
        from mailer.routes import mailer_blueprint
        app.register_blueprint(mailer_blueprint)

    return app
