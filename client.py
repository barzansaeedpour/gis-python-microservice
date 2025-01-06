import grpc
import dwg_pb2
import dwg_pb2_grpc
import os

def generate_file_chunks(file_path):
    with open(file_path, 'rb') as file:
        index = 0
        while True:
            chunk = file.read(1024)  # Read in 1024-byte chunks
            if not chunk:
                break
            yield dwg_pb2.FileChunk(index=index, data=chunk)
            index += 1

def save_converted_files(response):
    output_folder = "received_files"
    os.makedirs(output_folder, exist_ok=True)
    for file in response.files:
        file_path = os.path.join(output_folder, file.filename)
        with open(file_path, 'wb') as f:
            f.write(file.data)
    print("Converted files have been saved.")

def send_file():
    channel = grpc.insecure_channel(
        'localhost:50051',
        options=[
            ('grpc.max_send_message_length', 50 * 1024 * 1024),  # 50 MB
            ('grpc.max_receive_message_length', 50 * 1024 * 1024),  # 50 MB
        ]
    )
    stub = dwg_pb2_grpc.FileServiceStub(channel)
    response = stub.Upload(generate_file_chunks('./input/Khoroseh Var-Plan & Profile.dwg'))
    print(f'Upload response: {response.status}')
    save_converted_files(response)

if __name__ == '__main__':
    send_file()


