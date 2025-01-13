# https://learn.codesignal.com/course/93/unit/1/practice/2

# You are given two lists: sourceArray and searchArray, consisting of n and m tuples respectively, where n is an integer such that 1 ≤ n ≤ 100 and m is an integer such that 1 ≤ m ≤ 500. Each tuple in both arrays contains two elements: an integer identifier and a string. The identifiers in both arrays range from 1 to 100, inclusive. The strings in sourceArray consist of alphanumeric characters with lengths ranging from 1 to 100, inclusive. The strings in searchArray have lengths ranging from 1 to 500, inclusive.

# Your task is to implement a function stringSearch(sourceArray, searchArray) that takes these two arrays as input and returns an array that includes all tuples from sourceArray for which its string is a substring of at least one string in any tuple from searchArray and the identifier of the source tuple is less than or equal to the identifier of the search tuple.

# The order in which the tuples appear in the result should reflect their original order in the sourceArray. If no matches are found, the function should return an empty array.

# For example, if sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')] and searchArray = [(1, 'abcdef'), (5, 'uvwxy')], the function should return [(1, 'abc')] since 'abc' and 'def' are substrings found in 'abcdef', but 'def' is associated with 2 in sourceArray which is not less than or equal to 1 in searchArray. The string 'xyz' is not found in either 'abcdef' or 'uvwxy', so it is not included in the result.

# This task requires mastery of skills in nested looping and array manipulation, especially in the context of searching for a string within other strings.

def stringSearch(sourceArray, searchArray):
    result = []
    for s in sourceArray:
        for s2 in searchArray:
            if s[1] in s2[1] and s[0] <= s2[0]:
                result.append(s)
                break
    return result

# Expected: [(1, 'abc')]
print(stringSearch([(1, 'abc'), (2, 'def'), (3, 'xyz')], [(1, 'abcdef'), (5, 'uvwxy')]))

import unittest
class TestStringSearch(unittest.TestCase):
    def test_case_1(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'xyz')]
        searchArray = [(1, 'abcdef'), (5, 'uvwxy')]
        expected_output = [(1, 'abc')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_2(self):
        sourceArray = [(1, 'abc')]
        searchArray = [(2, 'def')]
        expected_output = []
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_3(self):
        sourceArray = [(1, 'abc'), (2, 'def')]
        searchArray = [(3, 'abc'), (4, 'def')]
        expected_output = [(1, 'abc'), (2, 'def')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_4(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi'), (4, 'jkl')]
        searchArray = [(5, 'mnopqr')]
        expected_output = []
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_5(self):
        sourceArray = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        searchArray = [(4, 'abcdefghi'), (5, 'defghiabc')]
        expected_output = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_6(self):
        sourceArray = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        searchArray = [(4, 'variant'), (5, 'answertest'), (6, 'tesla')]
        expected_output = [(1, 'var'), (2, 'ans'), (3, 'tes')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)

    def test_case_7(self):
        sourceArray = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        searchArray = [(4, 'abcd'), (5, 'bcda')]
        expected_output = [(1, 'ab'), (2, 'bc'), (3, 'cd')]
        self.assertEqual(stringSearch(sourceArray, searchArray), expected_output)


if __name__ == '__main__':
    unittest.main()