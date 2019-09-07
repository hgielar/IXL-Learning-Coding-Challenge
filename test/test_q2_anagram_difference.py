import unittest
import src.q2_anagram_difference

class TestAnagramQuestion2(unittest.TestCase):
    def test_question_2_anagram(self):
        # Explanation: Given a and b, we perform the following 5 calculations (since there are 5 elements in each array):
        # Index 0: 'a' and 'bb' cannot be anagrams because they contain different numbers of characters
        # Index 1: 'jk' and 'kf' are already anagrams because they both contain the same characters at the same frequencies
        # Index 2: 'abb' and 'bbc' differ bt one character
        # Index 3: 'mn' and 'op' differ by two characters
        # Index 4: 'abc' and 'def' differ by three characters
        # After checking each pair of strings, we return the array [-1, 0, 1, 2, 3] as our answer.
        a = ['a', 'jk', 'abb', 'mn', 'abc']
        b = ['bb', 'kj', 'bbc', 'op', 'def']
        self.assertEqual(src.q2_anagram_difference.getMinimumDifference(a,b), [-1, 0, 1, 2, 3])
