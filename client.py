import grpc
import dwg_pb2
import dwg_pb2_grpc

def generate_file_chunks(file_path):
    with open(file_path, 'rb') as file:
        index = 0
        while True:
            chunk = file.read(1024)  # Read in 1024-byte chunks
            if not chunk:
                break
            yield dwg_pb2.FileChunk(index=index, data=chunk)
            index += 1

def send_file():
    channel = grpc.insecure_channel('localhost:50051')
    stub = dwg_pb2_grpc.FileServiceStub(channel)
    response = stub.Upload(generate_file_chunks('./input/Khoroseh Var-Plan & Profile.dwg'))
    print(f'Upload response: {response.status}')

if __name__ == '__main__':
    send_file()
