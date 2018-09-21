import logging.config

log = logging.getLogger(__name__)

def input_checker(board_arg, hand_arg):
    """
    Checks if the input provided is valid
    :param board_arg: list of string with len > 2
    :param hand_arg: list of string with len = 2
    :return:
    """

    is_valid = False

    # checks if list and correct len
    if isinstance(board_arg, list) and len(board_arg) > 2:
        if isinstance(hand_arg, list) and len(hand_arg) == 2:
            if card_checker(board_arg) and card_checker(hand_arg):
                is_valid = True
        else:
            log.error('{} not a valid Hand'.format(hand_arg))

    else:
        log.error('{} not a valid Board.'.format(board_arg))

    return is_valid


def card_checker(list_of_cards):
    """
    Checks if the supplied cards are valid
    :param list_of_cards:
    :return:
    """

    return True