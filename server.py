import grpc
from concurrent import futures
import dwg_pb2
import dwg_pb2_grpc

class FileService(dwg_pb2_grpc.FileServiceServicer):
    def Upload(self, request_iterator, context):
        file_path = 'uploaded_file.dwg'
        with open(file_path, 'wb') as file:
            for request in request_iterator:
                file.write(request.data)
        return dwg_pb2.UploadResponse(status=dwg_pb2.UploadResponse.SUCCESS)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dwg_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
