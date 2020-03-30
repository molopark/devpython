from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('',8080))
serverSock.listen(1)

connectSock, addr = serverSock.accept()

print(str(addr),'에서 연결이 확인되었습니다.')

data = connectSock.recv(1024)
print('받은 데이터:', data.decode('utf-8'))

connectSock.send('I am Server.'.encode('utf-8'))
print('메시지를 보냈습니다.')
