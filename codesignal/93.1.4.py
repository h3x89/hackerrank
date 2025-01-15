# https://learn.codesignal.com/course/93/unit/1/practice/4

# You will be given two arrays of integers. The first array has n elements, and the second array has k elements. Sizes n and k both range from 1 to 100, inclusive. The elements of both arrays can fall within a range of -100 to 100, inclusive.

# Your task is to write a Python function that will locate and return an array of all pairs of integers with the property that the first element of each pair comes from the first array and the second element of each pair comes from the second array, such that the sum of the two elements of the pair is a perfect square. A perfect square, as you know, is an integer that is the square of another integer.

# The order of pairs in your output should correspond to the order of the elements in the input arrays. For example, if the two arrays are [2, 3, 16] and [1, 9, 10], the function should return [(3, 1), (16, 9)] because 3+1=4 (which is the square of 2) and 16+9=25 (which is the square of 5).

# If no such pairs exist, or if either input array is empty, your function should return an empty list.

def solution(arr1, arr2):
    result = []
    for a in arr1:
        for b in arr2:
            sum_ab = a + b
            # Check if sum is non-negative and is a perfect square
            if sum_ab >= 0:
                sqrt = int(sum_ab ** 0.5)
                if sqrt * sqrt == sum_ab:
                    result.append((a, b))
    return result

print(solution([2, 3, 16], [1, 9, 10])) # [(3, 1), (16, 9)] 

import unittest

class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        arr1 = [2, 3, 16]
        arr2 = [1, 9, 10]
        expected_output = [(3, 1), (16, 9)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_2(self):
        arr1 = [0]
        arr2 = [0]
        expected_output = [(0, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_3(self):
        arr1 = [4, 13, 23]
        arr2 = [-4, -3, -24]
        expected_output = [(4, -4), (4, -3), (13, -4)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_4(self):
        arr1 = [0, 1, 2, -100, 100]
        arr2 = [-100, 100, 30, 0, -1, -2, -3]
        expected_output = [(0, 100), (0, 0), (1, 0), (1, -1), (2, -1), (2, -2), (-100, 100), (100, -100), (100, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_5(self):
        arr1 = [100, 75, 36, 9, -25, -64, -100]
        arr2 = [-1, 1, 24, 0, -1, -24]
        expected_output = [(100, 0), (36, 0), (9, 0)]
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_6(self):
        arr1 = []
        arr2 = [1, 2, 3, 4]
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_7(self):
        arr1 = [1, 2, 3, 4]
        arr2 = []
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)

    def test_case_8(self):
        arr1 = []
        arr2 = []
        expected_output = []
        self.assertEqual(solution(arr1, arr2), expected_output)


if __name__ == "__main__":
    unittest.main()