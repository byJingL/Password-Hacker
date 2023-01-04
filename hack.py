import socket
from argparse import ArgumentParser
import itertools

CHAR = '0123456789abcdefghijklmnopqrstuvwxyz'


# Custom generator
def find_password():
    for i in range(1, len(CHAR)+1):
        pool = itertools.product(CHAR, repeat=i)
        for item in pool:
            yield ''.join(item)


parser = ArgumentParser()
parser.add_argument('host', type=str, help='The ip address of the sever you want to connect.')
parser.add_argument('port', type=int, help='The port of the sever you want to connect.')
args = parser.parse_args()

with socket.socket() as client_connection:
    address = (args.host, args.port)
    client_connection.connect(address)

    password_generator = find_password()

    for password in password_generator:
        message = password.encode()
        client_connection.send(message)
        response = client_connection.recv(1024)
        response = response.decode()

        if response == 'Connection success!':
            print(password)
            break