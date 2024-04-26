from legacy_code import LegacySystem


class NewSystem:
    def execute(self, left, right, operation):
        if operation == '+':
            return left + right
        elif operation == '-':
            return left - right
        elif operation == '*':
            return left * right
        elif operation == '/':
            return left / right
        else:
            return None


class AdapterSystem:
    def __init__(self, system: LegacySystem):
        self.system = system

    def execute(self, left, right, operation):
        if operation == '+':
            return self.system.execute(left, right, 'add')
        elif operation == '-':
            return self.system.execute(left, right, 'sub')
        else:
            return None


if __name__ == '__main__':
    system = AdapterSystem(LegacySystem())  # system = NewSystem()
    print(system.execute(1, 2, '+'))
    print(system.execute(1, 2, '-'))
