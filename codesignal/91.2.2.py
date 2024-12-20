# https://learn.codesignal.com/course/91/unit/2/practice/2

# Your task is to construct a function that accepts an integer n and returns the integer with the same digits as n, but in reverse order. You should implement your solution using a while loop.

# For instance, if the input is 12345, the output should be 54321.

# Keep in mind that n will always be a positive integer between 
# 1 and 10^8

# Do not use built-in functions that convert the integer to another data type, such as a string, to reverse it. Solve the problem purely using mathematical operations and loop constructs.

# Note that when the result has leading zeros, you should consider only the integer value (e.g., 1230 becomes 321 after the operation).

def solution(n):
    reversed_number = 0
    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10
    return reversed_number

print(solution(12345))

import unittest

class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(12345), 54321)

    def test2(self):
        self.assertEqual(solution(1), 1)

    def test3(self):
        self.assertEqual(solution(87654321), 12345678)
        
    def test4(self):
        self.assertEqual(solution(54321), 12345)
        
    def test5(self):
        self.assertEqual(solution(9876543210), 123456789)

    def test6(self):
        self.assertEqual(solution(56), 65)
        
    def test7(self):
        self.assertEqual(solution(4567890), 987654)
        
    def test8(self):
        self.assertEqual(solution(98765), 56789)

    def test9(self):
        self.assertEqual(solution(876), 678)
        
    def test10(self):
        self.assertEqual(solution(23456789), 98765432)
       
if __name__ == '__main__':
    unittest.main()