import os
import uuid
import requests
import grpc
from flask import Flask, request, abort

from protos.logging_pb2 import PostLoggingRequest, GetLoggingRequest
from protos.logging_pb2_grpc import LoggingStub

app = Flask(__name__)
logging_service_host = os.getenv("LOGGING_HOST", "localhost")
logging_service_channel = grpc.insecure_channel(
    f"{logging_service_host}:50051"
)
logging_service_client = LoggingStub(logging_service_channel)

messager_service_url = "http://localhost:1234"


@app.route('/facade-service', methods=['GET', 'POST'])
def facade_s():
    if request.method == 'POST':
        return get_processed_post_request()
    else:
        return get_processed_get_request()


def get_processed_post_request():
    print('send POST-like request to logging service')
    try:
        post_logging_request = PostLoggingRequest(
            uuid=str(uuid.uuid4()),
            msg=request.json.get('msg')
        )
        post_logging_response = logging_service_client.postLogging(
            post_logging_request
        )
        status = post_logging_response.status
        print('received status from logging:', status)
        return app.response_class(status=status)
    except Exception as ex:
        abort(400)


def get_processed_get_request():
    print('send GET-like request to logging service')
    get_logging_response = logging_service_client.getLogging(
        GetLoggingRequest()
    )
    print('received from logging:', get_logging_response)
    response_from_messages_service = requests.get(
        f'{messager_service_url}/messages'
    )
    print('received from messages:', response_from_messages_service.content)
    return f'from logging: {str(get_logging_response.messages)}, ' \
           f'from messager: {str(response_from_messages_service.text)}'


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1233, debug=True)
