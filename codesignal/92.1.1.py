# https://learn.codesignal.com/course/92/unit/1/practice/1

# You are given a string of n characters, with n varying from 1 to 1000, inclusive. Your task is to write a Python function that takes this string as input, applies the following operations, and finally returns the resulting string.

# Split the given string into individual words, using a space as the separator.
# Convert each word into a list of its constituent characters, and shift each list once to the right (with the last element moving to the first position).
# After the rotations, reassemble each word from its list of characters.
# Join all the words into a single string, separating adjacent words with a single space.
# Return this final string as the function's output.
# The constraints for the problem are as follows:

# The input string will neither start nor end with a space, nor will it have multiple consecutive spaces.
# Each word will contain only alphabets and digits, and its length will range from 1 to 10.
# The words are case-sensitive; for example, 'word' and 'Word' are considered distinct.
# Your program should output a single string with the words rotated by their lengths while preserving their original order.

# As an illustration, consider the input string "abc 123 def". Applying the stated operations results in the output "cab 312 fde".

def solution(s):
    words = s.split(" ")
    result = []
    for word in words:
        last_char = word[-1]
        word_without_last_char = word[:-1]
        result.append(last_char + word_without_last_char)
    return " ".join(result)

print(solution("abc 123 def"))

import unittest

class TestSolution(unittest.TestCase):
    def test_input_0(self):
        self.assertEqual(solution("abc 123 def"), "cab 312 fde")
   
    def test_input_1(self):
        self.assertEqual(solution("abc 123 def ghi"), "cab 312 fde igh")

    def test_input_2(self):
        self.assertEqual(solution("bat"), "tba")

    def test_input_3(self):
        self.assertEqual(solution("raceCar"), "rraceCa")

    def test_input_4(self):
        self.assertEqual(solution("mAnGo666 TaCo123i"), "6mAnGo66 iTaCo123")

    def test_input_5(self):
        self.assertEqual(solution("_ab 77Y UwF88"), "b_a Y77 8UwF8")

    def test_input_6(self):
        self.assertEqual(solution("SingleWord"), "dSingleWor")

    def test_input_7(self):
        self.assertEqual(solution("abcdefghij"), "jabcdefghi")
        
    def test_input_8(self):
        self.assertEqual(solution("ZzZzZzZ 1234567890 zYxWvUtS"), "ZZzZzZz 0123456789 SzYxWvUt")

if __name__ == "__main__":
    unittest.main()