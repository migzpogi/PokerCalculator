import unittest
from PokerCalcMain import calculate_deuces

class TestPokerMain(unittest.TestCase):
    """
    Unit tests for PokerCalcMain
    """

    def test_calculate_deuces(self):
        """
        Method for getting the deuces score
        :return:
        """

        board = ['4h', '5h', '8h', '7h', '9c']
        hand = ['2s', '3s']

        deuces = calculate_deuces(board, hand)

        self.assertEqual(deuces[0], 7414)
        self.assertEqual(deuces[1], 'High Card')

if __name__ == '_main__':
    unittest.main()