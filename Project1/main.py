import math


def task11(x, y):
    """
    Calculates and prints result of mathematical operations with two arguments
    :param x: First argument
    :param y: Second argument
    """
    a = math.e - math.cos(x) + 69
    b = math.cos(x) + math.pow(x, 7)
    c = math.tan(y) - (math.pow(y, 6) / 37)
    d = 87 * math.pow(x, 7) + math.pow(math.e, y)
    e = math.pow(x, 7) - (math.pow(y, 5) / 11)
    result = math.sqrt(a / b) + c + (d / e)
    print(f"{result:.2e}")


def task12(x):
    """
    Calculates result of mathematical operations with one argument depending on the specific conditions
    :param x: Argument with which to operate
    """
    if x < 38:
        print(f"{condition_function1(x):.2e}")
    if (x >= 38) and (x < 103):
        print(f"{condition_function2(x):.2e}")
    if (x >= 103) and (x < 164):
        print(f"{condition_function3(x):.2e}")
    if x >= 164:
        print(f"{condition_function4(x):.2e}")


def condition_function1(x):
    """
    Returns result of mathematical operations with one argument
    :param x: Argument with which to operate
    :return: Result of mathematical operations with one argument
    """
    return math.pow(math.e, math.cos(x)) - math.pow(x, 8) + 67


def condition_function2(x):
    """
    Returns result of mathematical operations with one argument
    :param x: Argument with which to operate
    :return: Result of mathematical operations with one argument
    """
    return math.pow(x, 7) + math.pow(x, 5)


def condition_function3(x):
    """
    Returns result of mathematical operations with one argument
    :param x: Argument with which to operate
    :return: Result of mathematical operations with one argument
    """
    return math.pow(x, 6) + (math.pow(x, 5) / 19) + 3


def condition_function4(x):
    """
    Returns result of mathematical operations with one argument
    :param x: Argument with which to operate
    :return: Result of mathematical operations with one argument
    """
    return math.pow(x, 5) + math.cos(x) - 4
