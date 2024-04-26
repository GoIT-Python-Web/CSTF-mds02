class Ops:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.commands = {
            'add': AddCommand(self),
            'mul': MulCommand(self)
        }

    def add(self):
        return self.first + self.second

    def mul(self):
        return self.first * self.second

    def execute(self, command_name):
        return self.commands[command_name].execute()


class AddCommand:
    def __init__(self, ops: Ops):
        self.ops = ops

    def execute(self):
        return self.ops.add()


class MulCommand:
    def __init__(self, ops: Ops):
        self.ops = ops

    def execute(self):
        return self.ops.mul()


if __name__ == "__main__":
    ops = Ops(10, 20)
    print(ops.execute('add'))
    print(ops.execute('mul'))
