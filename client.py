import socket
import json
import time


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 9999))

    #creation and serialise of data
    data = {"name": "Alice", "age": 23}
    print("Serialisation of Data")
    time.sleep(2)
    serialized_data = json.dumps(data).encode()

    try:
        client_socket.send(serialized_data)
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {json.loads(response)}")
    except ConnectionResetError as e:
        print(f"connection reset error: {e}")
    finally:
        client_socket.close()


if __name__ == "__main__":
    main()