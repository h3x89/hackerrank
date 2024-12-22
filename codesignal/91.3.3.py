# https://learn.codesignal.com/course/91/unit/3/practice/3

# In this task, you are given a string s, and your goal is to produce a new string following a specific pattern. You are to take characters in sets of three, reverse the characters in each set, and then place them back into the string in their original positions, preserving the reverse order within each set. If 1 or 2 characters remain at the end (because the length of the string is not divisible by 3), they should be left as they are.

# The string s contains only lowercase English letters, with its length ranging from 1 to 300, inclusive.

# For example, if you are given the input 'abcdef', the output should be 'cbafed'. For the input 'abcdefg', your function should provide 'cbafedg'.

def reversed_triple_chars(s: str) -> str:
    result = ""
    # Process string in groups of 3 characters, reversing each complete group
    # If the last group has fewer than 3 chars, leave it unchanged
    for i in range(0, len(s), 3):
        # Take chunk to reverse (max 3 chars)
        chunk = s[i:i+3]
        # If we have a full group of 3 chars, reverse it
        if len(chunk) == 3:
            result += chunk[::-1]
        # If less than 3 chars remain, leave unchanged
        else:
            result += chunk
    return result

import unittest

class TestReversedTripleChars(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reversed_triple_chars("abcdef"), "cbafed")

    def test_2(self):
        self.assertEqual(reversed_triple_chars("s"), "s")
        
    def test_3(self):
        self.assertEqual(reversed_triple_chars("reversedtriplechars"), "versretdepircelrahs")

    def test_4(self):
        self.assertEqual(reversed_triple_chars("abc"), "cba")

    def test_5(self):
        self.assertEqual(reversed_triple_chars("hello"), "lehlo")

    def test_6(self):
        self.assertEqual(reversed_triple_chars("abcdefg"), "cbafedg")

    def test_7(self):
        self.assertEqual(reversed_triple_chars("hellopython"), "lehpolhtyon")

    def test_8(self):
        self.assertEqual(reversed_triple_chars("ab"), "ab")

if __name__ == "__main__":
    unittest.main()