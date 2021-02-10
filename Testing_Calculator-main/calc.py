class Calc:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        if b != 0:
            return a // b
        else:
            print('Деление на ноль!')

# result = Calculator()
