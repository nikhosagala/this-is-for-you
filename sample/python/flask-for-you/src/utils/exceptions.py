import json

from werkzeug.exceptions import HTTPException


class ApiException(HTTPException):
    def __init__(self, code=None, error_code=None, user_message=None, developer_message=None):
        self.code = code or 500
        self.error_code = error_code or 500
        self.user_message = user_message or "An unknown error occurred."
        self.developer_message = developer_message or "An unknown error occurred."
        self.response = None
        self.description = developer_message

    def get_body(self, environ=None):
        return json.dumps({
            "status": self.code,
            "error_code": self.error_code,
            "user_message": self.user_message,
            "developer_message": self.developer_message
        })

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]

    def __str__(self):
        return '%d: %s' % (self.code, self.__class__.__name__)

    def __repr__(self):
        return '<%s \'%s\'>' % (self.__class__.__name__, self)
