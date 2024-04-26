from enum import Enum
from abc import ABC, abstractmethod


class OperationType(Enum):
    SUM = "sum"
    MUL = "mul"
    SQR = "squares"


class Operation(ABC):
    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Adder(Operation):
    def __init__(self, data):
        self.data = data

    def operation(self):
        return sum(self.data)

    def info(self):
        return OperationType.SUM.value


class Multiplier(Operation):
    def __init__(self, data):
        self.data = data

    def operation(self):
        r = 1
        for i in self.data:
            r *= i
        return r

    def info(self):
        return OperationType.MUL.value


class Squares(Operation):
    def __init__(self, data):
        self.data = data

    def operation(self):
        r = []
        for i in self.data:
            r.append(i ** 2)
        return r

    def info(self):
        return OperationType.SQR.value


class OperationFactory:
    @abstractmethod
    def create_operation(self) -> Operation:
        pass

    def make_operation(self) -> Operation:
        return self.create_operation()


class AdderFactory(OperationFactory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Adder(self.data)


class MultiplierFactory(OperationFactory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Multiplier(self.data)


class SquaresFactory(OperationFactory):
    def __init__(self, data):
        self.data = data

    def create_operation(self) -> Operation:
        return Squares(self.data)


def calculation(factory: OperationFactory) -> tuple:
    op = factory.make_operation()
    return op.operation(), op.info()


if __name__ == "__main__":
    print(calculation(AdderFactory([1, 2, 3, 4, 5])))
    print(calculation(MultiplierFactory([1, 2, 3, 4, 5])))
    print(calculation(SquaresFactory([1, 2, 3, 4, 5])))
