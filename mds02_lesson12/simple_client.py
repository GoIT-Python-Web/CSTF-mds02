import socket


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = socket.gethostbyname(socket.gethostname())
        print(host)
        s.connect((host, 8000))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
        print('Received', repr(data))


if __name__ == '__main__':
    main()
