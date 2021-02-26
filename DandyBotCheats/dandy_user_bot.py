import random
import random_bot
import move_player_module as mp

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
    if check("level") == 4:
        return fourth_level(check, x, y)
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
     return mp.take_gold()

    if check("gold", x, y + 1):
        return mp.go_down()
    else:
        return mp.go_right()

def second_level(check, x, y) -> str:
    """
    Called when second level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("gold", x, y):
        return mp.take_gold()
    if check("gold", x, y - 4):
        return mp.go_up()

    #Move player by gold start
    if check("gold", x, y - 1):
        return mp.go_up()
    if check("gold", x, y + 1):
        return mp.go_down()
    if check("gold", x + 1, y):
        return mp.go_right()
    #Move player by gold end

    if not check("wall", x + 2, y):
        return mp.go_right()


def third_level(check, x, y) -> str:
    """
    Called when third level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("gold", x, y):
     return mp.take_gold()

    return mp.attach_player_to_wall(check, x, y)

def fourth_level(check, x, y) -> str:
    """
    Called when fourth level is started
    :param check: Function to check position of the game objects
    :param x: X coordinate
    :param y: Y coordinate
    :return: String to make some events
    """
    if check("gold", x, y):
     return mp.take_gold()

    #Move player to the center block of the map
    if check('gold', x + 12, y - 5) and not check('wall', x, y - 2) and not check('wall', x, y + 2):
        return mp.go_right()

    #Move player in the center block
    if check('gold', x + 2, y + 5) and check('gold', x + 4, y + 6) and not check('gold', x + 4, y - 4):
        return mp.go_down()
    if check('gold', x + 2, y + 4) and check('gold', x + 4, y + 5) and not check('gold', x + 4, y - 5):
        return mp.go_down()
    if check('wall', x, y - 2) and check('wall', x, y - 3) and not check('wall', x, y - 6) and not check('wall', x, y - 7) and not check('wall', x, y - 4):
        return mp.go_up()

    return mp.attach_player_to_wall(check, x, y)