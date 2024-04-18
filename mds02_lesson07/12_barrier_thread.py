import logging
from random import randint
from threading import Barrier, Thread, current_thread
from time import sleep, ctime


def worker(barrier: Barrier):
    name = current_thread().name
    logging.info(f"Start thread {name}: {ctime()}")
    num = barrier.wait()
    sleep(randint(1, 3))
    logging.info(f"Барьєр подоланий {name}#{num}: {ctime()}")


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")
    br = Barrier(4)

    for i in range(12):
        th = Thread(target=worker, args=(br,))
        th.start()
