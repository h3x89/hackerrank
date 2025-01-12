# https://learn.codesignal.com/course/93/unit/1/practice/1

# You are provided with two arrays of unique integers, with the lengths of arrays ranging from 1 to 100, inclusive. The task requires you to identify elements that appear in both arrays and return them in an array, maintaining the order from the first provided array.

# Each array's element ranges from -100 to 100, inclusive.

# In your function common_elements(listA, listB), listA and listB represent the two input arrays. The function should return an array that includes the common elements found in both listA and listB, while preserving the order of elements as they appear in listA.

# For example, if listA = [7, 2, 3, 9, 1] and listB = [2, 3, 7, 6], the output should be [7, 2, 3].

def common_elements(listA, listB):
    return [x for x in listA if x in listB] # List comprehension to check if x is in listB

# Expected output: [7, 2, 3]
print(common_elements([7, 2, 3, 9, 1], [2, 3, 7, 6]))

import unittest

class CommonElementsTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(common_elements([7, 2, 3, 9, 1], [2, 3, 7, 6]), [7, 2, 3])

    def test2(self):
        self.assertEqual(common_elements([1, 2, 3, 4, 5], [-1, -2, -3, -4, -5]), [])

    def test3(self):
        self.assertEqual(common_elements([1, 2, 3], [2, 3, 4, 1]), [1, 2, 3])

    def test4(self):
        self.assertEqual(common_elements([1, 2, 3], [3, 2, 1, 4, 5, 6]), [1, 2, 3])

    def test5(self):
        self.assertEqual(common_elements([1, 2, 3], []), [])

    def test6(self):
        self.assertEqual(common_elements([-1, -2, -3, -4, -5], [-2, -4]), [-2, -4])

    def test7(self):
        self.assertEqual(common_elements([1, 2, 3], [1, 3]), [1, 3])


if __name__ == "__main__":
    unittest.main()