import math


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
