import math


def subtraction(a, b):
    return b - a


def multiplication(a, b):
    return a * b


def addition(a, b):
    return a + b


class Calculator:
    result = 0

    def __init__(self):
        self.result = 1
        pass

    def add(self, a, b):
        self.result = addition(int(a), int(b))
        return self.result

    def sub(self, a, b):
        self.result = subtraction(int(a), int(b))
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(int(a), int(b))
        return self.result

