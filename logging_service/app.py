from concurrent import futures
import grpc

import protos.logging_pb2_grpc as logging_pb2_grpc
from protos.logging_pb2 import PostLoggingResponse, GetLoggingResponse


class LoggingService(
    logging_pb2_grpc.LoggingServicer
):
    messages_dict = {}

    def postLogging(self, request, context):
        print(f'RECEIVED request: {request}')
        if not request.msg or not request.uuid:
            context.abort(grpc.StatusCode.ABORTED, "msg not in the request")
        self.messages_dict.update({request.uuid: request.msg})
        print(f'SAVED to self.messages_dict')
        return PostLoggingResponse(status=200)

    def getLogging(self, request, context):
        print(f'Return messages:', self.messages_dict.values())
        return GetLoggingResponse(
            messages=','.join([msg for msg in self.messages_dict.values()])
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    logging_pb2_grpc.add_LoggingServicer_to_server(
        LoggingService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

