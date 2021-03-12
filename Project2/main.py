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

#################################################################################


def task22(number) -> int:
    """
    Returns transcoded decimal number, this function uses bitwise operators to transcode given value
    :param number: hexadecimal number to transcode
    :return: Transcoded decimal number
    """
    a = number & 0b00000000000000000111111111111111
    b = number & 0b00111111111111111000000000000000
    c = number & 0b11000000000000000000000000000000
    a = a << 17
    b = b >> 13
    c = c >> 30

    return a | b | c

#################################################################################


def remove_duplicate(input_list=[]) -> list:
    """
    Returns list of lists with removed duplicates
    :param input_list: input list
    :return: List of lists with removed duplicates
    """
    temp_list = []
    for element in input_list:
        if element not in temp_list:
            temp_list.append(element)
    input_list = temp_list
    return input_list


def sep_first_column(sep_symbol, input_list=[]) -> list:
    """
    Return list with first separated column by specified symbol
    :param sep_symbol: specified symbol to use in separating
    :param input_list: list in that function will separate first column
    :return: List with first separated column
    """
    counter_of_sublist = 0
    temp_list = []
    second_column_cell = []
    for element in input_list:
        temp_list = element[0].split(sep_symbol, 1)
        input_list[counter_of_sublist][0] = temp_list[1]
        second_column_cell.append(temp_list[0])
        counter_of_sublist = counter_of_sublist + 1

    # Adds new column to the list and converts it to the tuple
    new_list = [(x, None, y, z) for (x, y, z) in input_list]

    # Converts tuple to the list
    t_list = [list(x) for x in new_list]

    for x in range(len(t_list)):
        t_list[x][1] = second_column_cell[x]

    return t_list


def transform_cells(input_list=[]) -> list:
    """
    Returns list with transformed cells
    :param input_list: list that will be transformed
    :return: List with transformed cells
    """
    for x in range(len(input_list)):
        input_list[x][1] = str(round(float(input_list[x][1]), 1))

        if input_list[x][2] == 'да':
            input_list[x][2] = 'true'
        elif input_list[x][2] == 'нет':
            input_list[x][2] = 'false'

        input_list[x][0] = input_list[x][0].replace(' ', '-')
        input_list[x][3] = input_list[x][3].replace('[at]', '@')
    return input_list


def task23(input_list=[]) -> list:
    """
    Returns transformed list of lists, removes duplicate lines, separates first column by ';'
    and transforms content of cells
    :param input_list: input list to transform
    :return: Transformed list of lists
    """
    return transform_cells(sep_first_column(';', remove_duplicate(input_list)))

# Testing task23 function
#initial_list = [['0.46;498 927‐2483', 'нет', 'zusulov68[at]mail.ru'],
                #['0.71;741 699‐2740', 'нет', 'secobin34[at]rambler.ru'],
                #['0.36;363 760‐3794', 'да', 'binan97[at]yahoo.com'],
                #['0.36;363 760‐3794', 'да', 'binan97[at]yahoo.com'],
                #['0.16;100 776‐2316', 'да', 'gozman24[at]mail.ru'],
                #['0.36;363 760‐3794', 'да', 'binan97[at]yahoo.com']]


#for i in task23(initial_list):
    #print(i)
