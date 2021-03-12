import math


def print_eps(result):
    """
    Prints value of parameter using epsilon format
    :param result: Value to print
    """
    print(f"{result:.2e}")


def task11(x, y) -> float:
    """
    Calculates and returns result of mathematical operations with two parameters
    :param x: First parameter
    :param y: Second parameter
    :return Result of mathematical operations with two parameters
    """
    a = math.pow(math.e, y) - math.cos(x) + 69
    b = math.cos(x) + math.pow(x, 7)
    c = math.tan(y) - (math.pow(y, 6) / 37)
    d = (87 * math.pow(x, 8)) + math.pow(math.e, y)
    e = math.pow(x, 7) - (math.pow(y, 5) / 11)
    result = math.sqrt(a / b) + c + (d / e)
    return result

#####################################################################


def task12(x) -> float:
    """
    Calculates and returns result of mathematical operations with one parameter depending on the specific conditions
    :param x: Parameter with which to operate
    :return Result of mathematical operations with one parameter
    """
    if x < 38:
        return condition_function1(x)
    if (x >= 38) and (x < 103):
        return condition_function2(x)
    if (x >= 103) and (x < 164):
        return condition_function3(x)
    if x >= 164:
        return condition_function4(x)


def condition_function1(x) -> float:
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
    return math.pow(math.e, math.cos(x)) - math.pow(x, 8) + 67


def condition_function2(x) -> float:
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
    return math.pow(x, 7) + math.pow(x, 5)


def condition_function3(x) -> float:
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
    return math.pow(x, 6) + (math.pow(x, 5) / 19) + 3


def condition_function4(x) -> float:
    """
    Returns result of mathematical operations with one parameter
    :param x: Parameter with which to operate
    :return: Result of mathematical operations with one parameter
    """
    return math.pow(x, 5) + math.cos(x) - 4

####################################################################


def task13(n, m) -> float:
    """
    Implements iteration function with two parameters and returns result
    :param n: First parameter
    :param m: Second parameter
    :return Result of mathematical operations with two mathematical sums
    """
    return 53 * math_sum1(1, 1, n, m) + math_sum2(1, 1, n, m)


def math_sum1(i, j, n, m) -> float:
    """
    Returns result of double mathematical sum
    :param i: lower bound of first mathematical sum
    :param j: lower bound of second mathematical sum
    :param n: upper bound of first mathematical sum
    :param m: upper bound of second mathematical sum
    :return: Result of double mathematical sum
    """
    result = 0.0
    for x in range(i, n + 1):
        for y in range(j, m + 1):
            result = result + (math.pow(math.e, y) - math.cos(x) + 69)
    return result


def math_sum2(i, j, n, m) -> float:
    """
    Returns result of double mathematical sum
    :param i: lower bound of first mathematical sum
    :param j: lower bound of second mathematical sum
    :param n: upper bound of first mathematical sum
    :param m: upper bound of second mathematical sum
    :return: Result of double mathematical sum
    """
    result = 0.0
    for x in range(i, n + 1):
        for y in range(j, m + 1):
            result = result + (math.pow(x, 5) + math.pow(y, 8))
    return result

#######################################################################


def task14(n) -> float:
    """
    Implements recurrent function with one parameter and returns result
    :param n: Recurrent function parameter
    :return: Result of recurrent function with one parameter
    """
    a = 0.0
    b = 0.0
    result = 4.0
    if n > 0:
        a = a + math.tan(task14(n - 1))
        b = b + (1 / 58) * task14(n - 1)
        result = a - b - 30
    return result
