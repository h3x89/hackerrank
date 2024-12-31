# https://learn.codesignal.com/course/92/unit/1/practice/2

# Given a string consisting of words separated by whitespace, your task is to write a Python function that accepts this string. It then replaces each character in the words with the corresponding character opposite in the English alphabet and stitches them all together to form a new string.

# Here's what you need to consider:

# The input string will include between 1 and 100 words.
# Each word consists of characters separated by white space.
# A word is composed of characters ranging from a to z or A to Z. So, if a word contains a lowercase 'a', for instance, it should be replaced with 'z', 'b' with 'y', 'c' with 'x', and so on, maintaining the same case. For words with an uppercase 'A', it should be replaced with 'Z', 'B' with 'Y', 'C' with 'X', and so forth, while preserving the uppercase.
# The given string will not start or end with a space, and there will be no occurrence of double spaces.
# After transforming the characters of the words, form a new string by taking the last word first and appending the remaining words in their original order, each separated by spaces.
# Note: The opposite letter mappings are as follows: a ↔ z, b ↔ y, c ↔ x, ..., m ↔ n, n ↔ m, ..., x ↔ c, y ↔ b, z ↔ a. The mapping is case-sensitive.

# Example

# For the input string "CapitaL letters", the output should be "ovggvih XzkrgzO".

def solution(s):
    def opposite_char(c):
        if 'a' <= c <= 'z':
            return chr(219 - ord(c))  # 219 = 'a' + 'z'
        elif 'A' <= c <= 'Z':
            return chr(155 - ord(c))  # 155 = 'A' + 'Z'
        return c

    words = s.split()
    transformed_words = [''.join(opposite_char(c) for c in word) for word in words]
    # Rearrange words: last word first, then the rest
    rearranged_words = [transformed_words[-1]] + transformed_words[:-1]
    return ' '.join(rearranged_words)

# Test the function
print(solution("CapitaL letters"))  # Should output: "ovggvih XzkrgzO"

import os
import sys
import unittest

# These lines are important!
currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)



class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("Hello"), "Svool")

    def test2(self):
        self.assertEqual(solution("ABC"), "ZYX")

    def test3(self):
        self.assertEqual(solution("abc"), "zyx")

    def test4(self):
        self.assertEqual(solution("A quick brown FOX jumps over the lazy DOG"), "WLT Z jfrxp yildm ULC qfnkh levi gsv ozab")

    def test5(self):
        self.assertEqual(solution("Zebra"), "Avyiz")

    def test6(self):
        self.assertEqual(solution("CapitaL letters"), "ovggvih XzkrgzO")

    def test7(self):
        self.assertEqual(solution("loWer letters"), "ovggvih olDvi")

    def test8(self):
        self.assertEqual(solution("OPPOSITE letters"), "ovggvih LKKLHRGV")

    def test9(self):
        self.assertEqual(solution("An apple a day keeps the doctor away"), "zdzb Zm zkkov z wzb pvvkh gsv wlxgli")

    def test10(self):
        self.assertEqual(solution("m n"), "m n")


if __name__ == '__main__':
    unittest.main()