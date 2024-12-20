# https://www.hackerrank.com/challenges/30-arrays/problem?isFullScreen=true

# Objective
# Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

# Example


# Print 4 3 2 1. Each integer is separated by one space.

# Input Format

# The first line contains an integer,  (the size of our array).
# The second line contains  space-separated integers that describe array 's elements.

# Constraints

# Constraints

# , where  is the  integer in the array.
# Output Format

# Print the elements of array  in reverse order as a single line of space-separated numbers.

# Sample Input

# 4
# 1 4 3 2
# Sample Output

# 2 3 4 1


#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO

def reverse_array(arr):
    return " ".join(map(str, arr[::-1]))

if __name__ == '__main__':

    # Simulate input data
    # input_data = """4
    # 1 4 3 2"""

    
    input_data = """8
    6676 3216 4063 8373 423 586 8850 6762"""
    # Replace sys.stdin with our simulated input
    # comment out this line to run the code with actual input
    # sys.stdin = StringIO(input_data)

    n = int(input().strip())
    # print(n)

    arr = list(map(int, input().rstrip().split()))
    print(reverse_array(arr))

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(reverse_array([1, 4, 3, 2]), "2 3 4 1")
    def test2(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), "5 4 3 2 1")
    def test3(self):
        self.assertEqual(reverse_array([10, 20, 30, 40, 50]), "50 40 30 20 10")
    def test4(self): # 6676 3216 4063 8373 423 586 8850 6762
        self.assertEqual(reverse_array([6676, 3216, 4063, 8373, 423, 586, 8850, 6762]), "6762 8850 586 423 8373 4063 3216 6676")
    def test5(self): # 9053 4443
        self.assertEqual(reverse_array([9053, 4443]), "4443 9053")
if __name__ == '__main__':
    unittest.main()