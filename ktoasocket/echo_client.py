from datetime import datetime
from socket import *
from echo_util import calcDate, calcAccptNum

now = datetime.now()


def run(host='127.0.0.1', port=4000):
    with socket.socket() as s:
        s.connect((host, port))
        line = input('>')
        print("line:{}".format(line))
        s.send(line.encode())
        res = s.recv(2048)
        print(f'={res.decode()}')


def run_client(host='127.0.0.1', port=4000):
    print(f"{now.year}년 {now.month:02}월 {now.day:02}일({'월화수목금토일'[now.weekday()]}) - {now.hour:02}시 {now.minute:02}분")
    with socket() as s:
        s.connect((host, port))
        for _ in range(10):
            senddata = ''
            body = ''

            data = input('> ')
            if data == 'bye':
                s.close()
                break
            elif data == '0300':
                body = f"01KTSSKB01197002{'':6}{'':13}{'':10}21004{'홍길동':100}0020201112340100123456781{'':6}{'서울 용산구':100}{'1동':100}1{'홍길동부인':100}19770101087654321"
                senddata = f"{'0056KTSSKB'}{calcDate('d')}{calcDate('t')}{data}{calcAccptNum('KTS')}{'':14}{body}"
            elif data == '0810':
                senddata = f"{'0056KTSOSS'}{calcDate('d')}{calcDate('t')}{data}{calcAccptNum('KTS')}{'':14}{body}"
            else:
                pass

            if senddata == '':
                pass
            else:
                print(f"senddata:[{senddata}]")
                s.send(senddata.encode())
                res = s.recv(2048)
                print(f"recvdata1 ack:[{res.decode()}]")
                res = s.recv(2048)
                print(f"recvdata2:[{res.decode()}]")


if __name__ == '__main__':
    # run()
    run_client()
