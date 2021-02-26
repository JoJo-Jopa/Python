"""
This module contains ready-made functions to move player to the left, right, up and down
and also function to attach player to the wall.....
"""

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

def attach_player_to_wall(check, x, y) -> str:
    """
    Attaches player and returns string to move it along the wall
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to move player
    """
    if check('wall', x - 1, y) and not check('wall', x + 1, y) and not check('wall', x, y - 1) or (not check('wall', x + 1, y) and not check('wall', x - 1, y) and not check('wall', x, y - 1) and not check('wall', x, y + 1) and check('wall', x - 1, y - 1)):
        return go_up()
    if not check('wall', x - 1, y) and check('wall', x + 1, y) and not check('wall', x, y + 1) or (not check('wall', x + 1, y) and not check('wall', x - 1, y) and not check('wall', x, y - 1) and not check('wall', x, y + 1) and check('wall', x + 1, y + 1)):
        return go_down()
    if check('wall', x, y - 1) or (not check('wall', x + 1, y) and not check('wall', x - 1, y) and not check('wall', x, y - 1) and not check('wall', x, y + 1) and check('wall', x + 1, y - 1)):
        return go_right()
    if check('wall', x, y + 1) or (not check('wall', x + 1, y) and not check('wall', x - 1, y) and not check('wall', x, y - 1) and not check('wall', x, y + 1) and check('wall', x - 1, y + 1)):
        return go_left()