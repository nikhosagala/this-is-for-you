import json

from flask import request
from werkzeug.exceptions import BadRequest

from src.utils.exceptions import ApiException


def schema_load(schema, json_data):
    json_data = json_data or json.loads(request.data)
    if not json_data:
        raise BadRequest()

    data, errors = schema.load(json_data)

    if errors:
        raise ApiException(user_message='Data tidak valid.', developer_message=json.dumps(dict(**errors)))

    return data
