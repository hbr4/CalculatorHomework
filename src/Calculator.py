from CsvReader import CsvReader


def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a*b
    return c

def division(a, b):
    a = int(a)
    b = int(b)
    c = b/a
    return c

def square(a):
    a = int(a)
    b = a**2
    return b

def sqrt(a):
    a = int(a)
    b = a**0.5
    return b

def mean(data):
    mean = data
    return mean


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = (a, b)
        return self.result

    def square(self, a, b):
        self.result = (a, b)
        return self.result

    def sqrt(self, a, b):
        self.result = (a, b)
        return self.result

class CSVStats(Calculator):
    data = []

    def __init__(self, data_file):
        self.data = CsvReader(data_file)
        pass

    def mean(self):
        mean(self.data)