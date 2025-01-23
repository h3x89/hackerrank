# https://learn.codesignal.com/course/93/unit/3/practice/3

# You are the developer of a unique board game and are now dealing with the challenge of quantifying player progress, assuming different starting positions.

# The game is played on a linear board that can be described as an array of integers, from 1 to n, with n ranging from 
# 1
# 1 to 
# 500
# 500 inclusive. Each position in the array is a move value that a player can take, signifying the number of steps a player can move rightward. An obstacle is a specific integer value on which the player cannot land.

# Your task is to implement the solution(numbers, obstacle) function, which calculates and returns an array steps. For every i in steps, the algorithm should calculate the number of steps required for a player to reach the end of the array from the i-th position without landing on an obstacle. If the player encounters an obstacle, steps[i] should should be -1.

# Each number in the numbers array can range from 
# 1
# 1 to 
# 10
# 10, and the obstacle value can range between 
# 1
# 1 and 
# 10
# 10, inclusive.

# The return value should be steps, the array with calculated values.

# For example, if numbers is [5, 3, 2, 6, 2, 1, 7] and obstacle is 3, the function would return an array [3, -1, 3, 1, 2, 2, 1]. The first value 3 indicates that starting from position 0, the player will have to make three moves before reaching the end of the board. The second value, -1, indicates that starting from 1, the player is on an obstacle. Therefore, progression from 1 is not possible. And so on.

def solution(numbers, obstacle):
    n = len(numbers)
    steps = [-1] * n  # Initialize all with -1
    steps[-1] = 1 if numbers[-1] != obstacle else -1  # Last position
    
    # Work backwards from second-to-last position
    for i in range(n-2, -1, -1):
        if numbers[i] == obstacle:
            continue  # Already -1
            
        jump = numbers[i]
        next_pos = i + jump
        
        if next_pos >= n:  # Can reach end directly
            steps[i] = 1
        elif next_pos < n and steps[next_pos] != -1:
            steps[i] = 1 + steps[next_pos]
            
    return steps

print(solution([5, 3, 2, 6, 2, 1, 7], 3)) # [3, -1, 3, 1, 2, 2, 1]

import unittest

class SolutionTests(unittest.TestCase):
    def test01(self):
        self.assertEqual(solution([5, 3, 2, 6, 2, 1, 7], 3), [3, -1, 3, 1, 2, 2, 1])

    def test02(self):
        self.assertEqual(solution([2, 4, 2, 1, 3, 2, 8, 4, 7], 4), [-1, -1, -1, -1, -1, -1, 1, -1, 1])

    def test03(self):
        self.assertEqual(solution([1, 1, 1, 1, 1], 1), [-1, -1, -1, -1, -1])

    def test04(self):
        self.assertEqual(solution([8, 1, 6, 2, 4, 7, 3], 7), [1, 2, 1, -1, 1, -1, 1])

    def test05(self):
        self.assertEqual(solution([10, 9, 8, 7, 6, 5], 5), [1, 1, 1, 1, 1, -1])

    def test06(self):
        self.assertEqual(solution([10]*500, 1), [50 - i // 10 for i in range(500)])

    def test07(self):
        self.assertEqual(solution([1]*500, 1), [-1]*500)

    def test08(self):
        self.assertEqual(solution([i for i in range(1, 11)]*2, 10), [5, 4, 5, 3, -1, 4, 3, 2, 2, -1, 4, 3, 2, 2, -1, 1, 1, 1, 1, -1])

    def test09(self):
        self.assertEqual(solution([i for i in range(1, 11)]*2, 1), [-1, 4, 5, 3, 3, 4, 3, 2, 2, 2, -1, 3, 2, 2, 2, 1, 1, 1, 1, 1])

    def test10(self):
        self.assertEqual(solution([10 - i for i in range(10)]*50, 5), [50 - i // 10 if i % 10 != 5 else -1 for i in range(500)])


if __name__ == '__main__':
    unittest.main()