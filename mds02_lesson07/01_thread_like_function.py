from threading import Thread
from time import sleep
from random import randint


def worker(name):
    print('Starting')
    print(f"{name} is running")
    sleep(randint(0, 5))
    print(f'Exiting {name}')


if __name__ == '__main__':
    for i in range(3):
        t = Thread(target=worker, args=(f'Thread-{i}',))
        t.start()

