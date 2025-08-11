import socket


class ConnConfig:
    host = socket.gethostbyname(socket.gethostname())

    port = 502
