# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 19:24:50 2018

@author: Raleigh Littles
"""

import unittest


# Runs in O(N) time

def countholes(num):
    holes_num = 0
    for char in str(num):
        if char in map(str, [0,4,6,9]): 
            holes_num += 1
            
        elif char == '8':
            holes_num += 2
            
    return holes_num



class TestPuzzle(unittest.TestCase):
    def test(self):
        self.assertEqual(countholes(630), 2)
        
if __name__ == '__main__':
    unittest.main()