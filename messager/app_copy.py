import threading

import pika
from flask import Flask

app = Flask(__name__)

@app.route('/messages',  methods=['GET'])
def messages():
    print(ALL_TIME_MESSAGES__)
    return str(ALL_TIME_MESSAGES__)


def threaded(fn):
    def run(*args, **kwargs):
        t = threading.Thread(target=fn, args=args, kwargs=kwargs)
        t.start()
        return t
    return run

@threaded
def consuming(messages_list):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='127.0.0.1')
    )
    channel = connection.channel()
    channel.queue_declare(queue='mq_for_messages_service')
    for method_frame, properties, body in channel.consume('mq_for_messages_service'):
        print("RECEIVED %r" % body)
        print('old data: ', messages_list)
        messages_list.append(str(body))
        print('new data in memory', messages_list)


if __name__ == '__main__':
    ALL_TIME_MESSAGES__ = []
    consuming(ALL_TIME_MESSAGES__)
    print('started consumer2')
    app.run(host='0.0.0.0', port=1235, debug=False)

