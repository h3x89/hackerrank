# https://learn.codesignal.com/course/93/unit/4/practice/1

# For this task, you are given two non-negative integers, num1 and num2. However, these are not just ordinary numbers; they are so large that they should be represented as strings instead of normal integers. Each can be up to 100 digits long.

# Your mission is to write a Python function that compares these two "string-numbers" without converting the entire strings into integers. Your function should determine whether num1 is greater than, less than, or equal to num2.

# Your function can only use comparison operators (such as >, <, or ==) on strings. So "1" < "2" is allowed, but 1 < 2 is not. The task requires that you manually compare the two strings from the most significant digit to the least significant. You should implement your own logic to compare two string numbers.

# The function should return the following results:

# If num1 is greater than num2, your function should return 1.
# If num2 is greater than num1, your function should return -1.
# If num1 and num2 are equal, your function should return 0.

# For `num1` = '12345' and `num2` = '1234', your function should return `1`.
# For `num1` = '1234' and `num2` = '12345', your function should return `-1`.
# For `num1` = '12345' and `num2` = '12345', your function should return `0`.

# This exercise is a great test of your understanding of how numbers and strings work and interact in a programming language. We hope you find it challenging and enjoyable!

def solution(a, b):
    # If lengths are different, longer number is greater
    if len(a) != len(b):
        return -1 if len(a) < len(b) else 1
    
    # If lengths are same, compare lexicographically
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

print(solution('12345', '1234'))  # Output: 1
print(solution('1234', '12345'))  # Output: -1
print(solution('12345', '12345'))  # Output: 0

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('12345', '1234'),  1)

    def test2(self):
        self.assertEqual(solution('1234', '12345'), -1)

    def test3(self):
        self.assertEqual(solution('12345', '12345'),  0)

    def test4(self):
        self.assertEqual(solution('100', '101'), -1)

    def test5(self):
        self.assertEqual(solution('500', '500'), 0)

    def test6(self):
        self.assertEqual(solution('105382', '105383'), -1)

    def test7(self):
        self.assertEqual(solution('99999999999999999999', '100000000000000000000'), -1)

    def test8(self):
        self.assertEqual(solution('100000000000000000000', '99999999999999999999'), 1)

    def test9(self):
        self.assertEqual(solution('1', '1'), 0)


if __name__ == "__main__":
    unittest.main()
