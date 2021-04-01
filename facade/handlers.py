import uuid

import requests
from flask import request, abort
from grpc._channel import _InactiveRpcError

from facade.app import app
from facade.config import MESSAGES_SERVICE_URL, get_rand_logging_client
from protos.logging_pb2 import PostLoggingRequest, GetLoggingRequest


def get_processed_post_request():
    print('send POST-like request to logging service')
    try:
        post_logging_request = PostLoggingRequest(
            uuid=str(uuid.uuid4()),
            msg=request.json.get('msg')
        )
        client = get_rand_logging_client()
        post_logging_response = client.postLogging(
            post_logging_request
        )
        status = post_logging_response.status
        print('received status from logging:', status)
        return app.response_class(status=status)
    except Exception as ex:
        print(ex)
        abort(400)


def get_processed_get_request():
    print('send GET-like request to logging service')
    client = get_rand_logging_client()
    try:
        get_logging_response = client.getLogging(
            GetLoggingRequest()
        )
        print('received from logging:', get_logging_response)
        response_from_messages_service = requests.get(
            f'{MESSAGES_SERVICE_URL}/messages'
        )
        print('received from messages:',
              response_from_messages_service.content)
        return f'from logging: {str(get_logging_response.messages)}, ' \
               f'from messager: {str(response_from_messages_service.text)}'

    except _InactiveRpcError:
        print('ERROR with getLogging(): _InactiveRpcError')
        abort(500)
