#!/usr/bin/env python3
# coding: utf-8

from flask.ext.runner import Manager
from flask_migrate import MigrateCommand, Migrate

from src import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
