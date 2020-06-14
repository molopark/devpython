import threading
class Messager(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())

x = Messager(name="메시지를 보냅니다.")
y = Messager(name="메시지를 수신합니다.")

x.start()
y.start()

mul = lambda x: x*7
print(mul(5))
