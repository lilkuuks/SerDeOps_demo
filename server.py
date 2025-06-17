import socket
import json
import time


def main():
    # Stream initialisation
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 9999))
    server_socket.listen(5)
    print('Waiting for a connection...')

    conn, addr = server_socket.accept()
    print('Connected by', addr)


    try:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            raise ValueError("No data received")

        #Deserialize Json
        received_obj = json.loads(data)
        print(f"Deserialize data : {received_obj}")
        received_obj_se = json.dumps(data)
        print(f"serialized {received_obj_se}")


        #modify and send back
        received_obj["status"] = "processed"
        print("Encoding Data object")
        time.sleep(1)
        conn.send(json.dumps(received_obj).encode('utf-8'))
        print("Encoding Data object completed")
    except json.JSONDecodeError as e:
        print(f"Deserialize error : {e}")
    finally:
        conn.close()


if __name__ == '__main__':
    main()