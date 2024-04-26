from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class PrinterCommand(Command):
    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)


class HelloCommand(PrinterCommand):
    def __init__(self):
        super().__init__("Hello")


class GoodbyeCommand(PrinterCommand):
    def __init__(self):
        super().__init__("Goodbye")


if __name__ == "__main__":
    commands = [HelloCommand(), GoodbyeCommand()]
    for command in commands:
        command.execute()
