# ------------------ Socket module -------------- #
import socket

with socket.socket() as client_socket:
    hostname = '127.0.0.1'
    port = 5000
    address = (hostname, port)

    client_socket.connect(address)

    data = 'Wake up, Jane'
    data = data.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)