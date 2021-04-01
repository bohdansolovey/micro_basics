import os
import random

import grpc

from protos.logging_pb2_grpc import LoggingStub

LOGGING_SERVICE_HOST = os.getenv("LOGGING_HOST", "localhost")

LOGGING_SERVICE_CHANNELS = [
    grpc.insecure_channel(f"{LOGGING_SERVICE_HOST}:50051"),
    grpc.insecure_channel(f"{LOGGING_SERVICE_HOST}:50052"),
    grpc.insecure_channel(f"{LOGGING_SERVICE_HOST}:50053")
]
LOGGING_SERVICE_CLIENTS = [
    LoggingStub(channel) for channel in LOGGING_SERVICE_CHANNELS
]

MESSAGES_SERVICE_URL = "http://localhost:1234"


def get_rand_logging_client() -> LoggingStub:
    return random.choice(LOGGING_SERVICE_CLIENTS)
