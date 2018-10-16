import argparse
from configparser import ConfigParser
import logging.config
import sys

from deuces.Card import Card
from deuces.Evaluator import Evaluator
from lib.checkers import input_type_checker
from lib.mydeck import MyDeck

log = logging.getLogger(__name__)

def handle_args(args):
    """
    Handles the arguments passed by the user. Used mainly for card input.
    :return: argParse.ArgumentParser()
    """

    parser = argparse.ArgumentParser(
        description='Poker Calculater. Please input your cards:')

    parser.add_argument('-b', '--board', action='store', nargs='*', default=None,
                        dest='board', help='The board cards.')

    parser.add_argument('-c', '--hand', action='store', nargs=2, default=None,
                        dest='hand', help='The hand cards.')

    if len(args) < 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args(args)


def calculate_deuces(board_arg, hand_arg):
    """
    Calculates the Deuces score as well as its class (high card, pair, etc)
    :param board: list of string with len > 2
    :param hand: list of string with len = 2
    :return: Tuple of (deuces score, deuces class)
    """

    log.debug('Calculating Deuces of {} and {}'.format(board_arg, hand_arg))

    if input_type_checker(board_arg, hand_arg):
        # convert string to Card object
        board = list(map(lambda c: Card.new(c), board_arg))
        hand = list(map(lambda c: Card.new(c), hand_arg))

        evaluator = Evaluator()
        deuces_score = evaluator.evaluate(board, hand)
        deuces_class = evaluator.class_to_string(evaluator.get_rank_class(deuces_score))

        return (deuces_score, deuces_class)

    else:
        log.error('Please see documentation for list of valid input.')
        sys.exit(1)


def draw_from_deck(number, exclude):
    """
    Draws card from a deck
    :param number:
    :param exclude:
    :return:
    """
    deck = MyDeck()
    i = 0
    drawn_cards = []

    while i != number:
        sample_draw = deck.draw()
        if sample_draw in exclude:
            pass
        else:
            drawn_cards.append(sample_draw)
            i += 1

    return drawn_cards


def compute_win_percentage(board_arg, hand_arg):
    """
    Computes your winning percentage using a Monte Carlo Simulation
    :param board_arg: list of string with len > 2
    :param hand_arg: list of string with len = 2
    :return:
    """

    log.debug('Computing win percentage of {} and {}'.format(board_arg, hand_arg))
    board = []
    hand = []

    if input_type_checker(board_arg, hand_arg):
        # convert string to Card object
        board = list(map(lambda c: Card.new(c), board_arg))
        hand = list(map(lambda c: Card.new(c), hand_arg))

    simulation_count = 3000
    win_count = 0
    runs = 0

    evaluator = Evaluator()

    for sim in range(simulation_count):
        board_fill = 5 - len(board)

        simulate_board = board + draw_from_deck(board_fill, board + hand)
        simulate_hand = draw_from_deck(2, simulate_board + hand)

        my_score = evaluator.evaluate(simulate_board, hand)
        enemy_score = evaluator.evaluate(simulate_board, simulate_hand)

        if my_score < enemy_score:
            win_count += 1

        runs += 1

        log.debug('Your score: {} {} vs {} {}'.format(
            evaluator.class_to_string(evaluator.get_rank_class(my_score)),
            my_score,
            evaluator.class_to_string(evaluator.get_rank_class(enemy_score)),
            enemy_score))

    win_chance = win_count/float(runs)

    return win_chance

if __name__ == '__main__':
    # load config and initialize logging
    config = ConfigParser()
    config.read('./conf/settings.ini')

    logging.config.fileConfig(disable_existing_loggers=False,
                              fname='./logs/logging_config.ini',
                              defaults={'logfilename': config.get('logs', 'path')})


    # arg handling
    user_input_cards = handle_args(sys.argv[1:])
    if user_input_cards.board == None or user_input_cards.hand == None:
        log.error('Please supply board cards and hand cards.')

    else:

        board = user_input_cards.board
        hand = user_input_cards.hand

        print(calculate_deuces(board, hand))
        print(compute_win_percentage(board, hand))

