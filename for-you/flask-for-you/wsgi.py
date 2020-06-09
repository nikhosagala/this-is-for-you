#!/usr/bin/env python
import os

from mailer import create_app

os.environ.setdefault("PYTHONPATH", "mailer")

app = create_app()
