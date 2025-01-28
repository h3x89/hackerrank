# https://learn.codesignal.com/course/93/unit/4/practice/3

# You are tasked with writing a Python function to multiply two extremely large positive integers. These are not your regular-sized large numbers; they are represented as strings potentially up to 500 digits long.

# Your function should take two string parameters, representing the two large integers to be multiplied, and return the product as a string. The challenging part is that you should perform the multiplication without converting the entire strings into integers.

# Keep in mind that the elements of the string are digits in the range from 0 to 9, inclusive.

# Furthermore, bear in mind that when multiplying numbers manually, we align the numbers vertically and multiply each digit of the first number with each digit of the second number, starting from the rightmost digits, and add the results after shifting appropriately.

# Please solve this problem using similar, decision-based string manipulations instead of merely converting strings into integers, multiplying them, and converting the result back to a string. This approach is imperative as direct multiplication would not be feasible for very large numbers.

# Challenge yourself, and Happy Coding!

def solution(num1, num2):
    # Initialize result array with zeros
    result = [0] * (len(num1) + len(num2))
    
    # Process each digit of num2 from right to left
    for i in range(len(num2)-1, -1, -1):
        carry = 0
        # Process each digit of num1 from right to left
        for j in range(len(num1)-1, -1, -1):
            # Get current digit from result considering position shift
            pos = i + j + 1
            curr = result[pos] + carry + (ord(num1[j]) - ord('0')) * (ord(num2[i]) - ord('0'))
            # Update result and carry
            result[pos] = curr % 10
            carry = curr // 10
        # Handle remaining carry
        result[i] += carry
    
    # Convert result to string and remove leading zeros
    result_str = ''.join(map(str, result))
    result_str = result_str.lstrip('0')
    
    return result_str if result_str else '0'

print(solution("123", "456"))

import os
import sys
import unittest

# These line are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


class SolutionTests(unittest.TestCase):
    def test01(self):
        self.assertEqual(solution("123456789", "987654321"), "121932631112635269")

    def test02(self):
        self.assertEqual(solution("123", "456"), "56088")

    def test03(self):
        self.assertEqual(solution("100", "200"), "20000")

    def test04(self):
        self.assertEqual(solution("500", "500"), "250000")

    def test05(self):
        self.assertEqual(solution("1000000000", "1000000000"), "1000000000000000000")

    def test06(self):
        self.assertEqual(solution("999999999", "1"), "999999999")

    def test07(self):
        self.assertEqual(solution("0", "500"), "0")

    def test08(self):
        self.assertEqual(solution("1", "1"), "1")

    def test09(self):
        self.assertEqual(solution("9", "9"), "81")    

    def test10(self):
        self.assertEqual(solution("111111111", "111111111"), "12345678987654321")

if __name__ == '__main__':
    unittest.main()