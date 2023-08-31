import socket
from select import select

to_monitor = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


def accept_connection(_server_socket: socket) -> None:
    client_socket, addr = server_socket.accept()
    print("Connection from: ", addr)
    to_monitor.append(client_socket)


def send_message(_client_socket: socket) -> None:
    request = _client_socket.recv(4096)

    if request:
        response = "Hello world\n".encode()
        _client_socket.send(response)
    else:
        _client_socket.close()


def event_loop() -> None:
    while True:

        ready_to_read, _, _ = select(to_monitor, [], [])  # for read, for write, for errors

        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == "__main__":
    to_monitor.append(server_socket)
    event_loop()
