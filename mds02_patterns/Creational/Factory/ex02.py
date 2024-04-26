class Car:
    def __init__(self):
        self.type = None

    def get_type(self):
        return self.type


class SportCar(Car):
    def __init__(self):
        super().__init__()
        self.type = 'Sport'

    def make_sound(self):
        return 'Vroom, vroom!'


class Truck(Car):
    def __init__(self):
        super().__init__()
        self.type = 'Truck'

    def make_sound(self):
        return 'Honk, honk!'


class CarFactory:
    def __init__(self):
        self.cars = {}

    def register_car(self, car_type, car_class):
        self.cars[car_type] = car_class

    def create_car(self, car_type):
        if car_type not in self.cars:
            raise ValueError(f'Invalid car type: {car_type}')
        return self.cars[car_type]()


if __name__ == '__main__':
    factory = CarFactory()
    factory.register_car('Sport', SportCar)
    factory.register_car('Truck', Truck)
    car = factory.create_car('Sport')
    print(car.get_type())
    
