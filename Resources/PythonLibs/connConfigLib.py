import socket


class ConnConfigLib:
    host = socket.gethostbyname(socket.gethostname())

    port = 502
