# https://learn.codesignal.com/course/94/unit/1/practice/2

# Gloria the bunny finds herself once again amidst an array game. This time, however, the game has slightly intensified with a third array coming into play. Your task is to develop a Python function to maneuver Gloria through her quest, yielding the summation of the maximum values she encounters from arrayB and arrayC together.

# Gloria's movement pattern oscillates between the arrays in the following order: arrayA -> arrayB -> arrayA -> arrayC -> arrayA -> arrayB -> arrayA -> arrayC, and so on.

# The rule to decide Gloria's move is: She uses the current element's value in the array as an index for her next array. For example, if Gloria is at arrayA[1]=2, she would move to arrayB[2].

# The pattern repeats itself until one of the following occurs:

# Gloria's path repeats, indicating that she is stuck in a loop and cannot progress further, OR
# Gloria tries to access an index that exceeds the length of an array (for example, attempting to access arrayA[4] when arrayA only contains 4 items indexed from 0 to 3), in which case Gloria's journey should also stop.
# Your task is to calculate the sum of the maximum values that Gloria encounters in arrayB and arrayC during her journey.
# Each input array consists of n items, where n ranges from 1 to 100, inclusive.
# Every item in the arrays is a non-negative integer and falls within the range of 0 to 99, inclusive.

# EXAMPLE

# Consider arrayA = [2, 1, 3, 0], arrayB = [1, 3, 2, 4], and arrayC = [4, 2, 5, 1]. Gloria's journey would look like:

# She begins at arrayA[0] = 2 which leads her to arrayB[2] = 2.
# She then goes back to arrayA[2] = 3, and then to arrayC[3] = 1.
# She returns to arrayA[1] = 1, then makes a hop to arrayB[1] = 3.
# She goes back to arrayA[3] = 0 and then proceeds to arrayC[0] = 4.
# Now Gloria would go to arrayA[4], however, since arrayA[4] doesn't exist because arrayA only contains 4 elements indexed from 0 to 3, Gloria's journey stops here.
# During her journey, Gloria encounters the maximum value 3 in arrayB and 4 in arrayC. The function should return 7, the sum of these two maximum values.

def solution(arrayA, arrayB, arrayC):
    max_B = float('-inf')
    max_C = float('-inf')

    # Start in A, at position 0
    current_array = 'A'
    current_pos = 0

    # We'll track visited states to detect loops
    # State is (current_array, index, flag_B_or_C)
    visited = set()

    # Flag determines if we go from A to B (True) or C (False)
    next_is_B = True

    while True:
        # Check if index is out of bounds for current array
        if current_array == 'A' and current_pos >= len(arrayA):
            break
        if current_array == 'B' and current_pos >= len(arrayB):
            break
        if current_array == 'C' and current_pos >= len(arrayC):
            break

        # Save current state (including B/C flag)
        state = (current_array, current_pos, next_is_B)
        # If we've been in this state before, it's a loop - break
        if state in visited:
            break
        visited.add(state)

        # If we're in B or C, update maximum value for B or C
        if current_array == 'B':
            max_B = max(max_B, arrayB[current_pos])
        elif current_array == 'C':
            max_C = max(max_C, arrayC[current_pos])

        # Determine where to go next
        if current_array == 'A':
            # From A we go to B or C, depending on next_is_B flag
            if next_is_B:
                next_array = 'B'
            else:
                next_array = 'C'
            # Index in new array is value from arrayA[current_pos]
            next_pos = arrayA[current_pos]
            # Flip flag (next time from A we'll go to other array)
            next_is_B = not next_is_B
        elif current_array == 'B':
            # From B always return to A, index taken from arrayB[current_pos]
            next_array = 'A'
            next_pos = arrayB[current_pos]
        else:  # current_array == 'C'
            # From C always return to A, index taken from arrayC[current_pos]
            next_array = 'A'
            next_pos = arrayC[current_pos]

        # Move to determined position
        current_array = next_array
        current_pos = next_pos

    # If we never visited B or C, maxes could be -inf
    if max_B == float('-inf'):
        max_B = 0
    if max_C == float('-inf'):
        max_C = 0

    return max_B + max_C


# ------- TESTS -------

if __name__ == '__main__':
    import unittest

    class TestSolution(unittest.TestCase):
        def test_1(self):
            arrayA = [2, 1, 3, 0]
            arrayB = [1, 3, 2, 4]
            arrayC = [4, 2, 5, 3]
            result = solution(arrayA, arrayB, arrayC)
            self.assertEqual(result, 7)  # maximum B=3, maximum C=4

        def test_2(self):
            arrayA = [2, 0, 1]
            arrayB = [1, 3, 2]
            arrayC = [2, 0, 1]
            result = solution(arrayA, arrayB, arrayC)
            self.assertEqual(result, 2)

        def test_3(self):
            arrayA = [1, 1, 0]
            arrayB = [2, 1, 3]
            arrayC = [2, 0, 1]
            result = solution(arrayA, arrayB, arrayC)
            self.assertEqual(result, 1)

        def test_4(self):
            arrayA = [0, 2, 0]
            arrayB = [1, 1, 2]
            arrayC = [0, 1, 2]
            result = solution(arrayA, arrayB, arrayC)
            self.assertEqual(result, 3)

        def test_5(self):
            arrayA = [1, 1, 2, 0]
            arrayB = [2, 2, 1, 3]
            arrayC = [1, 2, 3, 4]
            result = solution(arrayA, arrayB, arrayC)
            self.assertEqual(result, 5)

    unittest.main()