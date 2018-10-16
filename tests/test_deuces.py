import unittest
from deuces.Card import Card
from deuces.Evaluator import Evaluator

class TestDeuces(unittest.TestCase):
    """
    Test the classes in deuces
    """

    def test_cards_numerical_value(self):
        """
        Each card has a unique numerical value
        :return:
        """

        card1 = Card.new('4h')
        card2 = Card.new('2s')

        self.assertEqual(card1, 270853)
        self.assertEqual(card2, 69634)

    def test_evaluator(self):
        """
        Checks if the deuces score produced is correct
        :return:
        """

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

        evaluator = Evaluator()
        deuces_score = evaluator.evaluate(board, hand)

        self.assertEqual(deuces_score, 7414)


if __name__ == '__main__':
    unittest.main()