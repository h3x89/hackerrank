# https://learn.codesignal.com/course/93/unit/1/practice/3

# You are given two lists of integers (listA and listB), each containing n elements, with n ranging from 1 to 50. Each element in both lists can range from -1000 to 1000, inclusive.

# Your task is to write a Python function that identifies pairs of integers {a, b} wherein a belongs to listA and b belongs to listB, and a is greater than b. The function should return all such pairs in the order in which a appears in listA.

# For instance, if listA consists of [5, 1, 8, -2, 0] and listB comprises [3, 2, 7, 10, -1], the output should be [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)].

# Importantly, the order of elements in the output tuples should reflect the sequence in which a appears in listA. A pair cannot be included more than once. If no pair meets the condition, the function should return an empty list.

# Hint: Solving this task requires the use of nested loops. The outer loop should iterate through listA and the inner loop through listB, checking the condition a > b during each iteration.

def solution(listA, listB):
    # Create a set of unique values from listB to avoid duplicates
    seen_pairs = set()
    result = []
    for a in listA:
        for b in listB:
            if a > b and (a, b) not in seen_pairs:
                result.append((a, b))
                seen_pairs.add((a, b))
    return result

print(solution([5, 1, 8, -2, 0], [3, 2, 7, 10, -1])) # [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)]

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([5, 1, 8, -2, 0], [3, 2, 7, 10, -1]), [(5, 3), (5, 2), (5, -1), (1, -1), (8, 3), (8, 2), (8, 7), (8, -1), (0, -1)])

    def test2(self):
        self.assertEqual(solution([3, 2, 1], [1, 2, 3]), [(3, 1), (3, 2), (2, 1)])

    def test3(self):
        self.assertEqual(solution([0], [0]), [])

    def test4(self):
        self.assertEqual(solution([-5, -10, -15], [-20, -25, -30]), [(-5, -20), (-5, -25), (-5, -30), (-10, -20), (-10, -25), (-10, -30), (-15, -20), (-15, -25), (-15, -30)])
        
    def test5(self):
        self.assertEqual(solution([1000], [999]), [(1000, 999)])

    def test6(self):
        self.assertEqual(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 
                         [(1, -1), (1, -2), (1, -3), (1, -4), (1, -5), (1, -6), (1, -7), (1, -8), (1, -9), (1, -10), 
                          (2, -1), (2, -2), (2, -3), (2, -4), (2, -5), (2, -6), (2, -7), (2, -8), (2, -9), (2, -10), 
                          (3, -1), (3, -2), (3, -3), (3, -4), (3, -5), (3, -6), (3, -7), (3, -8), (3, -9), (3, -10), 
                          (4, -1), (4, -2), (4, -3), (4, -4), (4, -5), (4, -6), (4, -7), (4, -8), (4, -9), (4, -10), 
                          (5, -1), (5, -2), (5, -3), (5, -4), (5, -5), (5, -6), (5, -7), (5, -8), (5, -9), (5, -10), 
                          (6, -1), (6, -2), (6, -3), (6, -4), (6, -5), (6, -6), (6, -7), (6, -8), (6, -9), (6, -10),
                          (7, -1), (7, -2), (7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (7, -8), (7, -9), (7, -10), 
                          (8, -1), (8, -2), (8, -3), (8, -4), (8, -5), (8, -6), (8, -7), (8, -8), (8, -9), (8, -10), 
                          (9, -1), (9, -2), (9, -3), (9, -4), (9, -5), (9, -6), (9, -7), (9, -8), (9, -9), (9, -10),
                          (10, -1), (10, -2), (10, -3), (10, -4), (10, -5), (10, -6), (10, -7), (10, -8), (10, -9), (10, -10)])

    def test7(self):
        self.assertEqual(solution([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [])

    def test8(self):
        self.assertEqual(solution([500, 200, -400, -700], [200, -300, 400, -500, 700]), [(500, 200), (500, -300), (500, 400), (500, -500), (200, -300), (200, -500), (-400, -500)])

    def test9(self):
        self.assertEqual(solution([-1000] * 50, [1000] * 50), [])

    def test10(self):
        self.assertEqual(solution([1000] * 50, [-1000] * 50), [(1000, -1000)])


if __name__ == '__main__':
    unittest.main()
