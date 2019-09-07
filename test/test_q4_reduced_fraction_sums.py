import unittest
import src.q4_reduced_fraction_sums

class TestReducedFractionSums(unittest.TestCase):
    def test_reduced_fraction_sums(self):
        sample_input = ['722/148+360/176',
                        '978/1212+183/183',
                        '358/472+301/417',
                        '780/309+684/988',
                        '258/840+854/686']

        expected_output = ['2818/407', '365/202', '145679/98412', '4307/1339', '1521/980']

        self.assertEqual(src.q4_reduced_fraction_sums.reducedFractionSums(sample_input), expected_output)
