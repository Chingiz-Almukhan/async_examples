import socket
import selectors
from selectors import SelectorKey
from typing import List, Tuple

selector = selectors.DefaultSelector()


def server() -> None:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    selector.register(fileobj=server_socket, events=selectors.EVENT_READ, data=accept_connection)


def accept_connection(_server_socket: socket) -> None:
    client_socket, addr = _server_socket.accept()
    print("Connection from: ", addr)

    selector.register(fileobj=client_socket, events=selectors.EVENT_READ, data=send_message)


def send_message(_client_socket: socket) -> None:
    request = _client_socket.recv(4096)

    if request:
        response = "Hello world\n".encode()
        _client_socket.send(response)
    else:
        selector.unregister(_client_socket)
        _client_socket.close()


def event_loop() -> None:
    while True:

        events: List[Tuple[SelectorKey, int]] = selector.select()  # return tuple (key, events)

        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == "__main__":
    server()
    event_loop()
