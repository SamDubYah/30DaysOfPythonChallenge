# mypackages/arithmetics.py
# arithmetics.py


def add_numbers(*args):
    """Adds a non defined set of numbers"""
    total = 0
    for num in args:
        total += num
    return total


def mean(*args):
    """Returns the mean of set of numbers"""
    arg_sum = add_numbers(*args)
    arg_mean = arg_sum / len(args)

    return arg_mean


def subtract(a, b):
    """Subtracts two numbers"""
    return a - b


def multiply(a, b):
    """Multiply 2 numbers"""
    return a * b


def divide(a, b):
    """Divide 2 numbers"""
    return a / b


def remainder(a, b):
    """Returns the remainder divide of 2 numbers"""
    return a % b


def power(a, b):
    """Returns the power of 2 numbers"""
    return a ** b
