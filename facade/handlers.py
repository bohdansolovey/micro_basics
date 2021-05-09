import uuid

import pika
import requests
from flask import request, abort
from grpc._channel import _InactiveRpcError

from facade.app import app
from facade.config import get_rand_logging_client, \
    get_rand_messages_service_url
from protos.logging_pb2 import PostLoggingRequest, GetLoggingRequest


def get_processed_post_request():
    print('send POST-like request to logging service')
    try:
        post_msg_to_mq(request.json.get('msg'))
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


def post_msg_to_mq(msg: str):
    mq_connection = pika.BlockingConnection(
        pika.ConnectionParameters('127.0.0.1')
    )
    channel = mq_connection.channel()
    channel.queue_declare(queue='mq_for_messages_service')
    channel.basic_publish(
        exchange='', routing_key="mq_for_messages_service",
        body=msg,
    )
    print(f"[x] Sent: {msg}")
    mq_connection.close()


def get_processed_get_request():
    print('send GET-like request to logging service')
    client_logging = get_rand_logging_client()
    msg_service_url = get_rand_messages_service_url()
    try:
        get_logging_response = client_logging.getLogging(
            GetLoggingRequest()
        )
        print('received from logging:', get_logging_response)
        response_from_messages_service = requests.get(
            f'{msg_service_url}/messages'
        )
        print(
            'received from messages:', response_from_messages_service.content
        )
        return f'from logging: {str(get_logging_response.messages)}, \n' \
               f'from messages: {str(response_from_messages_service.text)}'

    except _InactiveRpcError:
        print('ERROR with getLogging(): _InactiveRpcError')
        abort(500)
