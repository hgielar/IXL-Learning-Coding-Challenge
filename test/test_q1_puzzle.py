import unittest
import src.q1_puzzle

class TestQuestion1Puzzle(unittest.TestCase):
    def test_when_zero_or_one_holes(self):
        # Add the holes count for each digit: 6, 3, and 0. Return 1 + 0 + 1 =2
        self.assertEqual(src.q1_puzzle.countholes(630), 2)

    def test_when_zero_or_two_holes(self):
        # Add the holes count for each digit: 1, 2, 8, 8. Return 0 + 0 + 2 + 2 = 4
        self.assertEqual(src.q1_puzzle.countholes(1288), 4)

