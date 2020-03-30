import socket
import numpy as np
import cv2


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf:
            return None
        buf += newbuf
        count -= len(newbuf)
    return buf


HOST = '127.0.0.1'
PORT = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = '1'
    client_socket.send(message.encode())
    length = recvall(client_socket, 16)
    stringData = recvall(client_socket, int(length))
    data = np.frombuffer(stringData, dtype='unit8')
    decimg = cv2.imdecode(data, 1)
    cv2.imshow('image', decimg)
    key = cv2.waitKey(1)
    if key == 27:
        break

client_socket.close()
