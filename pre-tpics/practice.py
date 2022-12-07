# ------------------ bytes in String -------------- #
print(ord('a'))  # 97
print(chr(97))  # a
print(ord('7'))  # 55

characters = bytes([55, 255])
print(characters)

array = bytes([31, 32, 126, 127])
print(array)
print(bytes([126]))

# ------------------ Creating bytes -------------- #
transed_number = (2024).to_bytes(2, byteorder='little')
print(transed_number[0]) 

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

