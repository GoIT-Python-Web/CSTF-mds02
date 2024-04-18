from random import randint
from threading import Thread, RLock, current_thread
import logging
from time import sleep

counter = 0
lock = RLock()


def worker():
    global counter
    while True:
        # lock.acquire()
        with lock:
            counter += 1
            sleep(randint(1, 2))
            with open("result.txt", "a") as fd:
                fd.write(f"{current_thread().name}:{counter}\n")
        # lock.release()


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Starting")
    for i in range(5):
        th = Thread(target=worker, name=f"Thread#{i}")
        th.start()
    logging.info("End program")
