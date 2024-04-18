import logging
from threading import Thread, current_thread, Event
from time import sleep
from random import randint


def worker(e: Event):
    while True:
        if e.is_set():
            break
        logging.info(f"{current_thread().name} working")
        sleep(1)
    logging.info(f"{current_thread().name} done")


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")

    event = Event()

    th = Thread(target=worker, args=(event,))
    th.start()

    sleep(5)
    event.set()

