# https://learn.codesignal.com/course/93/unit/3/practice/1

# You are given an array of n integers, ranging from 1 to 100 inclusive. Each integer represents a player's progress on a linear gameboard, indicating how many steps they can move to the right. However, the course is fraught with challenges; there exist several obstacles, represented by negative integers.

# Your task is to return a transformed array structuring the gameboard in a new way: if an integer can lead the player to an obstacle on its right (within the range of its value), replace the number with the index of the obstacle. If the number represents an obstacle (a negative integer), replace it with -1. If none of these conditions are met, retain the original integer.

# Keep in mind, this task is an innovative take on our previous analysis lesson, implementing a "Move Until Obstacle" game. Remember, your array will have no more than 500 elements, and the elements in the array range from -100 to 100, inclusive. Good luck with your coding journey!

# For instance, given an array [3, 2, -3, 1, 2], the output would be [2, 2, -1, 1, 2].

# Here's how it works:

# Replace the first position with 2 because a player at the first position can move 3 steps but will hit the obstacle at the 2nd index.
# Replace the second position with 2 because a player at the second position can move 2 steps but will hit the obstacle at the 2nd index.
# Replace the negative number -3 at the third position with -1 because it represents an obstacle.
# Keep the number 1 at the fourth position as there are no obstacles in its range.
# Keep the number 2 at the fifth position as there are no further positions or obstacles to impact it.

def solution(numbers):
    result = []
    for i in range(len(numbers)):
        if numbers[i] < 0:
            result.append(-1)
        else:
            # Check range from current position to max possible steps
            found_obstacle = False
            for j in range(1, numbers[i] + 1):
                if i + j >= len(numbers):
                    break
                if numbers[i + j] < 0:
                    result.append(i + j)
                    found_obstacle = True
                    break
            if not found_obstacle:
                result.append(numbers[i])
    return result

print(solution([3, 2, -3, 1, 2])) # [2, 2, -1, 1, 2]

import unittest

class SolutionTests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution([1, 2, 3, 2, -3, 5, 2, 7, -1, 4]), [1, 2, 4, 4, -1, 8, 8, 8, -1, 4])

    def test_case_2(self):
        self.assertEqual(solution([3, 4, -1, 2, 5, -2, 1, 5, 6]), [2, 2, -1, 5, 5, -1, 1, 5, 6])

    def test_case_3(self):
        self.assertEqual(solution([-1, 2, 3, 4, 5]), [-1, 2, 3, 4, 5])

    def test_case_4(self):
        self.assertEqual(solution([5, 4, 3, 2, 1, -1]), [5, 5, 5, 5, 5, -1])

    def test_case_5(self):
        self.assertEqual(solution([7, 6, 5, 4, -1, 2, 1]), [4, 4, 4, 4, -1, 2, 1])

    def test_case_6(self):
        self.assertEqual(solution([1, 1, 1, 1, 1, 1, -1]), [1, 1, 1, 1, 1, 6, -1])

    def test_case_7(self):
        self.assertEqual(solution([-2, 3, 2, -4, 5, 1, -1, 2]), [-1, 3, 3, -1, 6, 6, -1, 2])

if __name__ == '__main__':
    unittest.main()