import unittest
from lib.checkers import input_checker, card_checker

class TestCheckers(unittest.TestCase):
    """
    Unit tests for checker methods
    """

    def test_valid_input_true(self):
        """
        Checks if the input is a list of len > 2 for board and len > 1 for hand
        :return:
        """

        board = ['As', 'Ac', 'Ad']
        hand = ['Ah', 'Kd']

        self.assertTrue(input_checker(board, hand))

    def test_valid_input_false_board_wrong(self):
        """
        Checks if the method can detect wrong input
        :return:
        """

        board = ['As', 'Ac']
        hand = ['Ah', 'Kd']

        self.assertFalse(input_checker(board, hand))

    def test_valid_input_false_hand_wrong(self):
        """
        Checks if the method can detect wrong input
        :return:
        """

        board = ['As', 'Ac', 'Ad']
        hand = ['Ah']

        self.assertFalse(input_checker(board, hand))


if __name__ == '__main__':
    unittest.main()