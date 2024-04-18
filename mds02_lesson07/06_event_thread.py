import logging
from threading import Thread, current_thread, Event
from time import sleep
from random import randint


def worker_smart(e: Event, t: float):
    while not e.is_set():
        logging.info(f"Waiting for event set to complete")
        is_event = e.wait(t)
        if is_event:
            logging.info(f"Event set to complete")
            logging.info(f"Виконуємо роботу")
        else:
            logging.info(f"Робимо додатково щось корисне. Дивимось Тік-ток")


def worker(e: Event):
    logging.info(f"{current_thread().name} waiting")
    e.wait()
    logging.info(f"{current_thread().name} is working")
    sleep(randint(1, 2))
    logging.info(f"{current_thread().name} finished")


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")

    event = Event()

    ws = Thread(target=worker_smart, args=(event, 1))
    ws.start()

    w = Thread(target=worker, args=(event,))
    w.start()

    logging.info("Виконуємо важливу роботу...")
    sleep(3)
    logging.info("Робота виконана")
    event.set()
