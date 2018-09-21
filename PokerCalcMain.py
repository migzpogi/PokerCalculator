from configparser import ConfigParser
from deuces.Card import Card
from deuces.Evaluator import Evaluator
import logging.config

log = logging.getLogger(__name__)

if __name__ == '__main__':
    # load config and initialize logging
    config = ConfigParser()
    config.read('./conf/settings.ini')

    logging.config.fileConfig(disable_existing_loggers=False,
                              fname='./logs/logging_config.ini',
                              defaults={'logfilename': config.get('logs', 'path')})

    board = [
        Card.new('4h'),
        Card.new('5h'),
        Card.new('8h'),
        Card.new('7h'),
        Card.new('9d')
    ]

    hand = [
        Card.new('2s'),
        Card.new('3s')
    ]

    print(board)
    print(hand)
    evaluator = Evaluator()
    print(evaluator.evaluate(board, hand))

