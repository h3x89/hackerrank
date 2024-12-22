# https://learn.codesignal.com/course/91/unit/4/practice/1

# You are provided with an array of n integers, where n can range from 1 to 200, inclusive. Your task is to create a new array that takes two pairs of 'opposite' elements from the original array at each iteration, starting from the center and moving towards both ends, to calculate the resulting multiplication of each pair.

# By 'opposite' elements, we mean pairs of elements symmetrically located relative to the array's center. If the array's length is odd, the center element doesn't have an opposite and should be included in the result array as is.

# Each element in the array can range from -100 to 100, inclusive.

# For example, if the input array is [1, 2, 3, 4, 5], the returned array should be [3, 8, 5]. This is because the center element 3 remains as it is, the multiplication of 2 and 4 is 8, and the multiplication of 1 and 5 is 5.

def solution(numbers):
    result = []
    n = len(numbers)
    
    # Handle single element case
    if n == 1:
        return numbers
    
    # Add middle element for odd length arrays
    if n % 2 == 1:
        result.append(numbers[n // 2])
    
    # Process pairs starting from middle towards outside
    for i in range((n - 1) // 2, -1, -1):
        if i != n // 2:  # Skip middle element if already added
            result.append(numbers[i] * numbers[n-1-i])
    
    return result

import unittest

class TestSolution(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solution([1, 2, 3, 4, 5]), [3, 8, 5])

    def test_case2(self):
        self.assertEqual(solution([1, -1, 1, -1, 1, -1]), [-1, -1, -1])

    def test_case3(self):
        self.assertEqual(solution([-100] * 200), [10000] * 100)

    def test_case4(self):
        self.assertEqual(solution([5, -7, 2, -9, 1, -3, 8]), [-9, 2, 21, 40])

    def test_case5(self):
        self.assertEqual(solution([3, 6, 2, 9, -4, -1, 0, 5, 7]), [-4, -9, 0, 30, 21])

    def test_case6(self):
        self.assertEqual(solution([9]*200), [81]*100)

    def test_case7(self):
        self.assertEqual(solution([5]), [5])

    def test_case8(self):
        self.assertEqual(solution([0, 0]), [0])


if __name__ == '__main__':
    unittest.main()