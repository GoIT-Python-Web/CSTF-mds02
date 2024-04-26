class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self):
        return f"Hello, {self.username}!"


class Decorator:
    def __init__(self, wrapper: Greeting):
        self.wrapper = wrapper

    def greet(self):
        return self.wrapper.greet().upper()


if __name__ == "__main__":
    greeting = Decorator(Greeting("John"))
    print(greeting.greet())
