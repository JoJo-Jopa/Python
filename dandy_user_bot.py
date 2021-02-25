import random
import random_bot

def go_down() -> str:
    """
    Returns string to move player down
    :return: String to move player down
    """
    return "down"

def go_up() -> str:
    """
    Returns string to move player up
    :return: String to move player up
    """
    return "up"

def go_right() -> str:
    """
    Returns string to move player to the right
    :return: String to move player to the right
    """
    return "right"

def go_left() -> str:
    """
    Returns string to move player to the left
    :return: String to move player to the left
    """
    return "left"

def take_gold() -> str:
    """
    Returns string to take gold
    :return: String to take gold
    """
    return "take"

def script(check, x, y) -> str:
    """
    Executes in loop
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("level") == 1:
        return first_level(check, x, y)
    if check("level") == 2:
        return second_level(check, x, y)
    if check("level") == 3:
        return third_level(check, x, y)
    return "pass"

def first_level(check, x, y) -> str:
    """
    Called when first level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("gold", x, y):
     return take_gold()
    if check("gold", x, y + 1):
        return go_down()
    else:
        return go_right()

def second_level(check, x, y) -> str:
    """
    Called when second level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("gold", x, y):
        return take_gold()
    if check("gold", x, y - 4):
        return go_up()

    #Moving player by gold start
    if check("gold", x, y - 1):
        return go_up()
    if check("gold", x, y + 1):
        return go_down()
    if check("gold", x + 1, y):
        return go_right()
    #Moving player by gold end

    if not check("wall", x + 2, y):
        return go_right()

def third_level(check, x, y) -> str:
    """
    Called when third level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    #TODO
    return "Something LOL"