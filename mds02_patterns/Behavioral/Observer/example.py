import datetime


class Publisher:
    _observers = []  # Слухачі

    # {"event1": [], "event2": []}

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify(self, event, data=None):
        for observer in self._observers:
            observer(event, data)


def logger_console(event, data):
    print(datetime.datetime.now(), event, data)


class FileLogger:
    def __init__(self, filename):
        self.filename = filename

    def __call__(self, event, data):
        with open(self.filename, 'a') as f:
            f.write(f"{datetime.datetime.now()}: [{event}] = {data}\n")


if __name__ == "__main__":
    pub = Publisher()
    logger = FileLogger("log.txt")
    pub.register(logger)
    pub.register(logger_console)

    pub.notify("PULS", 65)
    pub.notify("PULS", 95)
    pub.notify("PULS", 115)
    pub.notify("UPS", 'Oh no, it is over!')
    pub.unregister(logger)
    pub.notify("PULS", 0)
    pub.notify('PULS', 0)

