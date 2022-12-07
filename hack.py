import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('host', type=str, help='The ip address of the sever you want to connect.')
parser.add_argument('port', type=int, help='The port of the sever you want to connect.')
parser.add_argument('message', type=str, help='The message you want to send to sever.')
args = parser.parse_args()

with socket.socket() as client_connection:
    address = (args.host, args.port)
    client_connection.connect(address)
    message = args.message.encode()
    client_connection.send(message)
    response = client_connection.recv(1024)
    response = response.decode()
    print(response)
