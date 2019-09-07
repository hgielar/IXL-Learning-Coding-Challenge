import unittest
import src.q3_grid_game

class TestGridGameQuestion3(unittest.TestCase):
    def test_question_3_grid_game(self):
        self.assertEqual(src.q3_grid_game.function(['2 3', '3 7', '4 1'], 3), 2)
