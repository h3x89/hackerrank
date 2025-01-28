# https://learn.codesignal.com/course/94/unit/1/practice/1

# You're assisting in the creation of an algorithm for a novel game where a character hops between two arrays following certain rules. The game starts at the first index (1-based) of an array, arrayA.

# The value at the character's current position in arrayA determines the index it jumps to on the second array, arrayB. Upon landing on arrayB, it does the same thing: the value at the current position specifies the index it jumps to in arrayA. This iteration continues until the character lands on an index in arrayA that it has already visited, at which point the game concludes.

# Your task is to develop a Python function simulating this gameplay. The function receives two equal-length arrays of integers, arrayA and arrayB, each containing n elements (1 ≤ n ≤ 100). It should return an array consisting of the 1-based indices on arrayB that the character visited before a position on arrayA was repeated.

# Each element in the input arrays ranges from 1 to n, indicating the next 1-based index that the character will jump to in the other array. The function guarantees that each jump always results in a valid position within the same-length arrays, and a position in arrayA will inevitably be revisited.

# Can you devise a function that proficiently simulates this gameplay?

# Example

# For arrayA = [1, 3, 2, 5, 4] and arrayB = [5, 4, 3, 2, 1] the output should be [1, 4, 3, 2, 5] since it first lands at the first position in arrayB (the resulting array is [1]), then goes to the fifth position in arrayA, then returns to the fourth position in arrayB (the resulting array becomes [1, 4]), etc.

def solution(arrayA, arrayB):
    visited_indices = set()
    result = []
    
    # Start from index 0 (first position)
    current_index_a = 0
    
    # Continue until we hit a position in arrayA that we've seen before
    while current_index_a not in visited_indices:
        # Mark current position in arrayA as visited
        visited_indices.add(current_index_a)
        
        # Get the next index in arrayB (1-based)
        next_index_b = arrayA[current_index_a]
        
        # Add the 1-based index we're jumping to in arrayB
        result.append(next_index_b)
        
        # Jump to arrayA using 0-based index
        current_index_a = arrayB[next_index_b - 1] - 1
    
    return result

print(solution([1, 3, 2, 5, 4], [5, 4, 3, 2, 1])) # [1, 4, 3, 2, 5]

import unittest

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        arrayA = [1, 3, 2, 5, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [1, 4, 3, 2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_2(self):
        arrayA = [1, 1, 1, 1, 1]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_3(self):
        arrayA = [2, 3, 4, 5, 1]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_4(self):
        arrayA = [1, 5, 2, 4, 3]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_5(self):
        arrayA = [4, 3, 2, 1, 5]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [4, 3, 2, 1, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_6(self):
        arrayA = [5, 4, 3, 2, 1]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [5, 1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_7(self):
        arrayA = [5, 1, 2, 3, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_8(self):
        arrayA = [1, 2, 3, 4, 5]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_9(self):
        arrayA = [3, 2, 1, 5, 4]
        arrayB = [5, 4, 3, 2, 1]
        expected_output = [3, 1, 4, 2, 5]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

    def test_case_10(self):
        arrayA = [2, 3, 4, 1, 5]
        arrayB = [1, 2, 3, 4, 5]
        expected_output = [2, 3, 4, 1]
        self.assertEqual(solution(arrayA, arrayB), expected_output)

if __name__ == '__main__':
    unittest.main()