from abc import ABC, abstractmethod


class Car:
    def __init__(self) -> None:
        self.parts = {}

    def add(self, key, value):
        self.parts[key] = value

    def show(self) -> str:
        print(f"Car Parts")
        for key, value in self.parts.items():
            print(f"{key}: {value}")


class CarBuilder(ABC):
    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_engine(self):
        pass

    @abstractmethod
    def build_wheel(self):
        pass

    @abstractmethod
    def build_doors(self):
        pass

    @abstractmethod
    def get_result(self):
        pass


class ElectricCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self.car = Car()

    def build_body(self):
        self.car.add("body", "metal")

    def build_engine(self):
        self.car.add("engine", "electric")

    def build_wheel(self):
        self.car.add("wheel", "4")

    def build_doors(self):
        self.car.add("doors", "2")

    def get_result(self):
        return self.car


class GasCarBuilder(CarBuilder):
    def __init__(self) -> None:
        self.car = Car()

    def build_body(self):
        self.car.add("body", "metal")

    def build_engine(self):
        self.car.add("engine", "gas")

    def build_wheel(self):
        self.car.add("wheel", "4")

    def build_doors(self):
        self.car.add("doors", "4")

    def get_result(self):
        return self.car


class Director:
    def __init__(self, builder: CarBuilder) -> None:
        self.builder = builder

    def construct_car(self):
        self.builder.build_body()
        self.builder.build_engine()
        self.builder.build_wheel()
        self.builder.build_doors()


if __name__ == "__main__":
    electric_builder = ElectricCarBuilder()
    director = Director(electric_builder)
    director.construct_car()
    electric_car = electric_builder.get_result()
    electric_car.show()

    gas_builder = GasCarBuilder()
    director = Director(gas_builder)
    director.construct_car()
    gas_car = gas_builder.get_result()
    gas_car.show()