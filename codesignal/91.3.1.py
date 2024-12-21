# https://learn.codesignal.com/course/91/unit/3/practice/1

# In this task, you are given a string composed of lowercase English alphabet letters ('a' to 'z'). The length of the string will range from 1 to 100 characters. Your challenge is to create a new string resulting from a unique order of character selection from the original string.

# You need to develop a Python function, special_order(inputString), which takes inputString as an argument. The resulting string begins with the last character of the inputString, then selects the second-to-last character, continuing in reverse order until you reach the middle character of the string. Then, start with the first character of the inputString, proceed to the second character, and continue in this manner until you reach the middle character.

# For example, if the inputString is "abcdefg", the function should return "gfedabc".

# Keep in mind the following constraints while creating your function:

# The input string contains only lowercase English letters ('a' to 'z').
# The length of the input string is between 1 and 100, inclusive.

def special_order(inputString):
    n = len(inputString)
    if n <= 1:
        return inputString
        
    mid = n // 2
    # First part: characters from end to middle
    result = inputString[n-1:mid-1:-1]
    # Second part: characters from start to middle
    result += inputString[:mid]
    return result


# Example usage:
print(special_order("abcdefg"))  # Output: "gfedabc"

import unittest

class TestSpecialOrder(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(special_order("abcde"), "edcab")

    def test_case_2(self):
        self.assertEqual(special_order("abcdef"), "fedabc")

    def test_case_3(self):
        self.assertEqual(special_order("a"), "a")

    def test_case_4(self):
        self.assertEqual(special_order("zyxwvutsrqpon"), "nopqrstzyxwvu")

    def test_case_5(self):
        self.assertEqual(special_order("abcddcba"), "abcdabcd")
    
    def test_case_6(self):
        self.assertEqual(
            special_order("abcdefghijklmnopqrstuvwxyz"*4 +"abcd"), 
            "dcbazyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzab"
        )

if __name__ == "__main__":
    unittest.main()