import time
from socket import *
from threading import Thread
import KtoaHeader
from echo_util import calcDate


def echo_handler(conn, addr, terminator='bye'):
    BUF_SIZE = 2048
    while True:
        data = conn.recv(BUF_SIZE)
        recvdata = data.decode()

        if recvdata == '':
            pass
        else:
            # print(f"RECEIVED:{data}:{recvdata}:{addr}")
            recvreport = KtoaHeader()
            sendreport = KtoaHeader()

            recvreport.setParam(recvdata)
            # print(f"recvreport:[{recvreport.toString}]")
            print(f"bizGubun:{recvreport.bizGubun}")

            if recvreport.bizGubun == '0300':
                recvreport.bizGubun = '0301'
                recvreport.respCode = 'BS0000'

                sendreport.setParam(recvdata)
                sendreport.bizGubun = '0310'
                sendreport.respCode = 'BS0000'
                sendreport.procDate = calcDate('d')
                sendreport.procTime = calcDate('t')
                sendreport.setBody(recvdata)

            if recvreport.bizGubun == '0810':
                recvreport.bizGubun = '0811'
                recvreport.respCode = 'BS0000'

                sendreport.setParam(recvdata)
                sendreport.bizGubun = '0820'
                sendreport.respCode = 'BS0000'
                sendreport.procDate = calcDate('d')
                sendreport.procTime = calcDate('t')
                sendreport.setBody(recvdata)

            if sendreport.toString == '':
                pass
            else:
                print(f"ack:[{recvreport.toString}]")
                conn.send(recvreport.toString.encode())
                time.sleep(1)
                print(f"sendreport:[{sendreport.toString}]")
                conn.send(sendreport.toString.encode())



def run_server(host='', port=4000):
    with socket() as s:
        s.bind((host,port))
        while True:
            s.listen(3)
            conn, addr = s.accept()
            t = Thread(target=echo_handler, args=(conn, addr))
            t.start()
        s.close()


if __name__ == '__main__':
    run_server()
