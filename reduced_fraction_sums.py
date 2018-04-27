# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 01:37:03 2018

@author: raleigh-littles
"""

import fractions, unittest

def reducedFractionSums(expressions):
    """
    Fairly self-explanatory, just use the built-in fractions package to perform
    the fraction addition -- they'll be automatically reduced in the end.
    """
    sum_array = []
    for expr in expressions:
        first_frac_string, second_frac_string = expr.split('+')
        first_frac = fractions.Fraction(first_frac_string)
        second_frac = fractions.Fraction(second_frac_string)
        sum_frac = first_frac + second_frac
        sum_array.append(str(sum_frac.numerator) + '/' + str(sum_frac.denominator))
        
    return sum_array
        

fraction_expressions = ['722/148+360/176',
                        '978/1212+183/183',
                        '358/472+301/417',
                        '780/309+684/988',
                        '258/840+854/686']


class TestReducedFractionSums(unittest.TestCase):
    def test(self):
        self.assertEqual( reducedFractionSums(fraction_expressions), ['2818/407', '365/202', '145679/98412', '4307/1339', '1521/980'])
        
if __name__ == '__main__':
    unittest.main()