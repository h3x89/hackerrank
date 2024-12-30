# https://learn.codesignal.com/course/91/unit/5/practice/2

# Your task is to write a Python function that takes in a string and identifies all the consecutive groups of identical characters within it, with the analysis starting from the end of the string rather than from its beginning. A group is defined as a segment of the text where the same character is repeated consecutively.

# Your function should return a list of tuples. Each tuple will consist of the repeating character and the number of its repetitions. For instance, if the input string is "aaabbcccdde", the function should output: [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)].

# Note that the input string cannot be empty; in other words, it must contain at least one character, and its length must not exceed 500 characters. The return should also be in reverse order, starting from the group of repeated characters at the end of the string and moving backward.

# Put your knowledge and skills into action to solve this reverse pattern identification puzzle!

def solution(s):
    result = []
    count = 1
    # iterate over the string in reverse order
    for i in range(len(s) - 1, 0, -1):
        # if the current character is the same as the previous character, increment the count
        if s[i] == s[i - 1]:
            count += 1
        else:
            # if the current character is different from the previous character, add the previous character and its count to the result
            result.append((s[i], count))
            count = 1

    # add the last character and its count to the result
    result.append((s[0], count))
    return result

print(solution("aaabbcccdde"))

import unittest

class TestSolution(unittest.TestCase):

    def test1(self):
        self.assertEqual(solution("aaabbcccdde"), [('e', 1), ('d', 2), ('c', 3), ('b', 2), ('a', 3)])

    def test2(self):
        self.assertEqual(solution("aaaaaaaZ"), [('Z', 1), ('a', 7)])

    def test3(self):
        self.assertEqual(solution("a"), [('a', 1)])

    def test4(self):
        self.assertEqual(solution("abc12321cba"), [('a', 1), ('b', 1), ('c', 1), ('1', 1), ('2', 1), ('3', 1), ('2', 1), ('1', 1), ('c', 1), ('b', 1), ('a', 1)])

    def test5(self):
        self.assertEqual(solution("123454321"), [('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('4', 1), ('3', 1), ('2', 1), ('1', 1)])

    def test6(self):
        self.assertEqual(solution("ABBA"), [('A', 1), ('B', 2), ('A', 1)])

    def test7(self):
        self.assertEqual(solution("Radar"), [('r', 1), ('a', 1), ('d', 1), ('a', 1), ('R', 1)])

    def test8(self):
        self.assertEqual(solution("$$$$$"), [('$', 5)])

    def test9(self):
        self.assertEqual(solution("Rotor"), [('r', 1), ('o', 1), ('t', 1), ('o', 1), ('R', 1)])

    def test10(self):
        self.assertEqual(solution("Red roses run no risk, sir, on Nurse's order"), [('r', 1), ('e', 1), ('d', 1), ('r', 1), ('o', 1), (' ', 1), ('s', 1), ('\'', 1), ('e', 1), ('s', 1), ('r', 1), ('u', 1), ('N', 1), (' ', 1), ('n', 1), ('o', 1), (' ', 1), (',', 1), ('r', 1), ('i', 1), ('s', 1), (' ', 1), (',', 1), ('k', 1), ('s', 1), ('i', 1), ('r', 1), (' ', 1), ('o', 1), ('n', 1), (' ', 1), ('n', 1), ('u', 1), ('r', 1), (' ', 1), ('s', 1), ('e', 1), ('s', 1), ('o', 1), ('r', 1), (' ', 1), ('d', 1), ('e', 1), ('R', 1)])

if __name__ == '__main__':
    unittest.main()