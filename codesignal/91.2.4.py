# https://learn.codesignal.com/course/91/unit/2/practice/4

# You are tasked with writing a function that takes a positive integer, n, as an input and returns the number of consecutive equal digits in the number. Specifically, your function should identify pairs of digits in n that are equal and consecutive and return the count of these pairs.

# For instance, if n = 113224, it contains two groups of consecutive equal digits: 11 and 22. Therefore, the output should be 2. For n = 444, the output should also be 2, as there are two groups of 44 in this number.

# Keep in mind that n will be a positive integer ranging from 
# 1 to 10^8, inclusive.

# Note: You are not permitted to convert the number into a string or any other iterable structure for this task. You should work directly with the number.

def solution(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == (n // 10) % 10:
            count += 1
        n //= 10  # Divide n by 10 to "remove" the last digit.
                  # For example, if n is 1234, after this operation n will be 123
    return count

print(solution(113224))

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(113224), 2)
 
    def test2(self):
        self.assertEqual(solution(33333888), 6)
 
    def test3(self):
        self.assertEqual(solution(13579), 0)
 
    def test4(self):
        self.assertEqual(solution(345672), 0)
 
    def test5(self):
        self.assertEqual(solution(22333555), 5)
        
    def test6(self):
        self.assertEqual(solution(100000), 4)

    def test7(self):
        self.assertEqual(solution(10), 0)

    def test8(self):
        self.assertEqual(solution(98876), 1)

    def test9(self):
        self.assertEqual(solution(4444), 3)

    def test10(self):
        self.assertEqual(solution(1), 0)

if __name__ == '__main__':
    unittest.main()