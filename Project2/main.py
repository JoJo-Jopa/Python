from builtins import print


def upper_branch(input_list=[]) -> int:
    """
    Returns result of upper branch of conditions
    :param input_list: input list that contains values to pass in conditions
    :return: Result of upper branch of conditions
    """
    # The first branch
    if input_list[0] == 'zimpl':
        if input_list[3] == 'max':
            return 5
        elif input_list[3] == 'r':
            return 4
        elif input_list[3] == 'jsx':
            return 3
    # The other branch
    if input_list[0] == 'mupad':
        if input_list[1] == 'uno':
            return 2
        elif input_list[1] == 'tcl':
            return 1
        elif input_list[1] == 'nsis':
            return 0


def lower_branch(input_list=[]) -> int:
    """
    Returns result of lower branch of conditions
    :param input_list: input list that contains values to pass in conditions
    :return: Result of lower branch of conditions
    """
    # The first branch
    if input_list[3] == 'r':
        return 10
    elif input_list[3] == 'max':
        return 11
    elif input_list[3] == 'jsx':
        if input_list[1] == 'nsis':
            return 7
        elif input_list[1] == 'tcl':
            return 8
        elif input_list[1] == 'uno':
            return 9


def task21(input_list=[]) -> int:
    """
    Returns integer as result of condition tree execution
    :param input_list: input list that contains values to pass in conditions
    :return: Integer as result of condition tree execution
    """
    if input_list[2] == 'cool':
        return 6
    elif input_list[2] == 'forth':
        return upper_branch(input_list)
    elif input_list[2] == 'xml':
        return lower_branch(input_list)


def task22(number) -> str:
    """
    Returns transcoded hexadecimal string, this function uses bitwise operators to transcode given value
    :param number: hexadecimal number to transcode
    :return: Transcoded hexadecimal string
    """
    a = number & 0b00000000000000000111111111111111
    b = number & 0b00111111111111111000000000000000
    c = number & 0b11000000000000000000000000000000
    a = a << 17
    b = b >> 13
    c = c >> 30

    return hex(a | b | c)
