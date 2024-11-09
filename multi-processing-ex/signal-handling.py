from multiprocessing import Process
import signal
def keyboardInterruptHandler(*args):
    print("interrupt")
    exit()
signal.signal(signal.SIGINT,keyboardInterruptHandler)
while True:
    pass