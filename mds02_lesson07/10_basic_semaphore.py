from threading import Semaphore, Thread
from time import sleep
import logging


def worker(semaphore: Semaphore):
    logging.info("waiting...")
    with semaphore:
        logging.info("Got semaphore")
        sleep(1)
        logging.info("Finished operation")


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")
    pool = Semaphore(3)

    for i in range(10):
        w = Thread(target=worker, args=(pool,))
        w.start()
