import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname(socket.gethostname())
        print(host)
        s.bind((host, 8000))
        s.listen()
        print('Listening on port 8000...')
        while True:
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024).decode()
                if not data:
                    continue
                print('Received', repr(data))
                conn.send(data.encode())


if __name__ == '__main__':
    main()
