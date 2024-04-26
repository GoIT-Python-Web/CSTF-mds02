class LegacySystem:
    def execute(self, left, right, operation):
        if operation == 'add':
            return left + right
        elif operation == 'sub':
            return left - right
        else:
            return None


if __name__ == '__main__':
    legacy = LegacySystem()
    print(legacy.execute(1, 2, 'add'))
    print(legacy.execute(1, 2, 'sub'))
