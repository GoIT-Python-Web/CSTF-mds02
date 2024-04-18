from threading import Event, Thread, current_thread
from time import sleep
import logging


def master(event: Event):
    logging.info("Master is working")
    sleep(1)  # Simulate work
    logging.info("Master finished and set event")
    event.set()


def worker(event: Event):
    logging.info(f"{current_thread().name} waiting...")
    event.wait()
    logging.info(f"{current_thread().name} working")
    sleep(1)  # Simulate work
    logging.info(f"{current_thread().name} finished")


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")
    event = Event()

    m = Thread(target=master, args=(event,))
    w1 = Thread(target=worker, args=(event,))
    w2 = Thread(target=worker, args=(event,))
    w3 = Thread(target=worker, args=(event,))

    w1.start()
    w2.start()
    w3.start()
    sleep(0.5)
    m.start()
