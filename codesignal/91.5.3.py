# https://learn.codesignal.com/course/91/unit/5/practice/3

# In this task, you need to write a Python function that finds repeating two-character patterns in a string. The function should identify when the same pair of characters appear next to each other in the string and count how many times each pair repeats consecutively.

# The function should return a new string that lists each pair followed by the number of times it repeats consecutively. For example, let's break down the input string "aaabbabbababacab":

# Divide the string into pairs:

# "aa"
# "ab"
# "ba"
# "bb"
# "ab"
# "ab"
# "ac"
# "ab"
# Note the consecutive pairs:

# "ab" appears twice consecutively in the middle.
# Therefore, the output string will be: "aa1ab1ba1bb1ab2ac1ab1".

# Similarly, for the input string "aaababbababaca", the output should be "aa1ab2ba3ca1".

# Key points to remember:

# The input string always has an even number of characters.
# The string contains only lowercase letters.
# The string length can be up to 500 characters.
# Focus on finding consecutive repetitions of the same two-character patterns.

def solution(s):
    result = ""
    i = 0
    # iterate over the string in steps of 2
    while i < len(s)-1:
        current_pair = s[i:i+2] # get the current pair
        count = 1 # initialize the count
        j = i+2 # start counting from the next pair
        # count the number of times the current pair appears consecutively
        while j < len(s)-1 and s[j:j+2] == current_pair:
            count += 1
            j += 2
        # add the current pair and its count to the result
        result += current_pair + str(count)
        i = i+2 if j == i+2 else j # move to the next pair
    return result

print(solution("aaababbababaca"))

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution("aaababbababaca"), "aa1ab2ba3ca1")

    def test2(self):
        self.assertEqual(solution("abcabcabcabcab"), "ab1ca1bc1ab1ca1bc1ab1")

    def test3(self):
        self.assertEqual(solution("ab"), "ab1")

    def test4(self):
        self.assertEqual(solution("ccddaaeeff"), "cc1dd1aa1ee1ff1")

    def test5(self):
        self.assertEqual(solution("eeffgg"), "ee1ff1gg1")

if __name__ == '__main__':
    unittest.main()