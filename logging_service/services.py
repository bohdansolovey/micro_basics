from concurrent import futures

import grpc
import hazelcast

from protos import logging_pb2_grpc
from protos.logging_pb2 import PostLoggingResponse, GetLoggingResponse


class LoggingService(
    logging_pb2_grpc.LoggingServicer
):
    def __init__(self, hazelcast_instance_addr, map_name='some_d'):
        self.map_name = map_name
        self.client = hazelcast.HazelcastClient(
            cluster_name="dev",
            cluster_members=hazelcast_instance_addr
        )
        print('client created')

    def postLogging(self, request, context):
        print(f'RECEIVED request: {request}')
        if not request.msg or not request.uuid:
            context.abort(grpc.StatusCode.ABORTED, "msg not in the request")
        self.save_to_distributed_map(uuid=request.uuid, msg=request.msg)
        # self.messages_dict.update({request.uuid: request.msg})
        print(f'SAVED to distr map')
        return PostLoggingResponse(status=200)

    def getLogging(self, request, context):
        # print(f'Return messages:', self.messages_dict.values())
        distributed_map = self.client.get_map(self.map_name)
        messages = distributed_map.values().result()
        print('messages:', messages)
        return GetLoggingResponse(
            messages=messages
        )

    def save_to_distributed_map(self, uuid, msg):
        distributed_map = self.client.get_map(self.map_name)
        distributed_map.set(str(uuid), str(msg))


def serve(hz_addr, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    logging_pb2_grpc.add_LoggingServicer_to_server(
        LoggingService([hz_addr]),
        server
    )
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()