import logging.config

log = logging.getLogger(__name__)

def input_type_checker(board_arg, hand_arg):
    """
    Checks if the input type provided is valid
    :param board_arg: list of string with len > 2
    :param hand_arg: list of string with len = 2
    :return:
    """

    is_valid = False

    if isinstance(board_arg, list) and len(board_arg) > 2:
        if isinstance(hand_arg, list) and len(hand_arg) == 2:
            if card_checker(board_arg) and card_checker(hand_arg):
                return True
            else:
                log.error('Card types must be of "Ad" format.')
        else:
            log.error('Hand {} must be a list of len == 2.'.format(hand_arg))

    else:
        log.error('Board {} must be a list of len > 2.'.format(board_arg))

    return is_valid


def card_checker(list_of_cards):
    """
    Checks if the supplied cards are valid.
    We will split them into two parts, rank and suit.
    Valid ranks are 2,3,4,5,6,7,8,9,T,J,Q,K,A
    Valid suits are s,d,c,h
    :param list_of_cards:
    :return:
    """

    is_valid = False

    valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    valid_suits = ['d', 'h', 's', 'c']

    # transform to upper case rank, lower case suit
    for card in convert_case(list_of_cards):
        if card[0] in valid_ranks and card[1] in valid_suits:
            is_valid = True

    return is_valid


def convert_case(list_of_cards):
    """
    Converts to upper case rank ,lower case suit
    :param list_of_cards:
    :return:
    """

    for idx, card in enumerate(list_of_cards):
        list_of_cards[idx] = card[0].upper() + card[1].lower()

    return list_of_cards