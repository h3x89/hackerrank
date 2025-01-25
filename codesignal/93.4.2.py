# https://learn.codesignal.com/course/93/unit/4/practice/2

# You are given two exceedingly large positive decimal numbers, num1 and num2, both represented as strings. The length of these strings can range anywhere from 1 to 500 characters. The challenge here is to subtract num2 from num1 without directly converting the strings into integers.

# Create a Python function that performs this operation and returns the resultant string, referred to as num3.

# Please note that the subtraction will not result in a negative number, as num1 will always be greater than or equal to num2.

def solution(num1, num2):
    # Ensure num1 is greater than or equal to num2
    if len(num1) < len(num2) or (len(num1) == len(num2) and num1 < num2):
        raise ValueError("num1 must be greater than or equal to num2")

    # Pad shorter number with leading zeros
    max_len = max(len(num1), len(num2))
    num1 = num1.zfill(max_len)
    num2 = num2.zfill(max_len)
    
    result = []
    borrow = 0
    
    # Process digits from right to left
    for i in range(max_len-1, -1, -1):
        digit1 = int(num1[i])
        digit2 = int(num2[i])
        
        # Handle borrowing
        digit1 -= borrow
        if digit1 < digit2:
            digit1 += 10
            borrow = 1
        else:
            borrow = 0
            
        # Calculate difference
        diff = digit1 - digit2
        result.insert(0, str(diff))
    
    # Remove leading zeros
    while len(result) > 1 and result[0] == '0':
        result.pop(0)
        
    return ''.join(result)

# Test with valid input
print(solution("456", "123"))  # "456" - "123" = "333"

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution('398746', '199234'), '199512')

    def test2(self):
        self.assertEqual(solution('100', '1'), '99')

    def test3(self):
        self.assertEqual(solution('9', '1'), '8')

    def test4(self):
        self.assertEqual(solution('501', '105'), '396')

    def test5(self):
        self.assertEqual(solution('1000', '999'), '1')

    def test6(self):
        self.assertEqual(solution('10000', '1000'), '9000')

    def test7(self):
        self.assertEqual(solution('111111111111111', '111111111111111'), '0')

    def test8(self):
        self.assertEqual(solution('123456789101112131415', '98765432101012131415'), '24691357000100000000')

    def test9(self):
        self.assertEqual(solution('500', '500'), '0')

if __name__ == '__main__':
    unittest.main()