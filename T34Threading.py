import threading

class TunaMessager(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())

x = TunaMessager(name='Send out messages')
y = TunaMessager(name='Receive message')

x.start()
y.start()