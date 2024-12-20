# https://learn.codesignal.com/course/91/unit/2/practice/1

# You are given an integer n where n ranges from 
# 1 to 10^8, inclusive. Your task is to write a function that calculates and returns the product of the odd digits of n, without converting n into a string.

# For example, if n equals 43172, the output should be 21, because the product of the odd digits 3, 1, and 7 is 21.

# Please note that if n has no odd digits, your function should return 0.

# You are expected to solve this task by using a while loop. Good luck!

def solution(n):
    product = 1
    found_odd = False  # flaga sprawdzająca czy znaleziono nieparzystą cyfrę
    
    while n > 0:
        digit = n % 10
        if digit % 2 != 0:
            product *= digit
            found_odd = True  # znaleziono nieparzystą cyfrę
        n //= 10
    
    return product if found_odd else 0  # zwróć 0 jeśli nie znaleziono nieparzystych cyfr

print(solution(43172))

import unittest

class SolutionTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(43172), 21)

    def test2(self):
        self.assertEqual(solution(2468), 0)

    def test3(self):
        self.assertEqual(solution(11111), 1)

    def test4(self):
        self.assertEqual(solution(10), 1)

    def test5(self):
        self.assertEqual(solution(39991), 2187)
    
    def test6(self):
        self.assertEqual(solution(73004), 21)

    def test7(self):
        self.assertEqual(solution(123456), 15)
        
    def test8(self):
        self.assertEqual(solution(77777), 16807)
        
    def test9(self):
        self.assertEqual(solution(33333333), 6561)
        
    def test10(self):
        self.assertEqual(solution(100000000), 1)

if __name__ == '__main__':
    unittest.main()