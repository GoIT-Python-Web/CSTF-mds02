class Dog:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = 'woof'

    def make_sound(self):
        return self.sound


class Cat:
    def __init__(self, nickname):
        self.nickname = nickname
        self.sound = 'meow'

    def make_sound(self):
        return self.sound


def create_pet(pet_type, nickname):
    if pet_type == 'dog':
        return Dog(nickname)
    elif pet_type == 'cat':
        return Cat(nickname)
    else:
        raise ValueError('Invalid pet type')


if __name__ == '__main__':
    pet = create_pet('dog', 'Rex')
    print(pet.make_sound())
    pet2 = create_pet('cat', 'Garfield')
    print(pet2.make_sound())
