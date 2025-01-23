# https://learn.codesignal.com/course/93/unit/3/practice/2

# Your task is to design a 1-dimensional game where a player moves along a path determined by an array of integers.

# The path is an array of integers, each ranging from -100 to 100, inclusive. The size of the array n, i.e., the total number of steps on the path, can range from 1 to 500, inclusive. Each integer a_i in the array signifies how many steps the player can move and in which initial direction:

# A positive integer allows the player to move that many steps to the right.
# A negative integer directs the player to move that many steps to the left.
# Zero signifies a blockade that prevents further movement.
# The game proceeds along the following rules:

# The player starts at the first position of the array (0-indexed) and moves according to the value at the player's current position in the array.

# If the value in the current position is zero, then the game ends. If the player's current position leads them outside of the array's boundaries, then their ability to move in the current direction ceases.

# If the latter happens, then the player reverses their direction and continues to move according to similar rules, but now the directions are inverted: positive integers lead the player to the left, and negative integers point to the right.

# The game ends when the player encounters a blockade or the array boundaries for the second time and so can no longer move.

# You are to implement a function titled evaluatePath(numbers). This function should take an array of integers as input, representing the path and its rules, and return a tuple (position, moves), where:

# position: This is the player's final position (0-indexed) when the game ends.
# moves: This is the total number of moves made by the player until the game ends.
# It's guaranteed that the game will not lead to an infinite loop, i.e. the path to the next blockade or the array boundaries would not require the player to visit the same position more than once.

# For instance, given an array [3, 4, 1, 1, -3, 1]. The output would be (4, 5). Here's how it works:

# The player starts at position 0, where the value is 3. They move 3 steps to the right and land on the 3rd position. Total moves till now: 1.

# At position 3, the value is 1. They move 1 step to the right, landing on the 4th position. Total moves till now: 2.

# At position 4, the value is -3. They move 3 steps to the left, landing back on position 1. Total moves meanwhile: 3.

# At position 1, the value is 4. They move 4 steps to the right, landing on position 5. Total moves thus far: 4.

# At position 5, the value is 1, which would lead them out of the array's right boundary. So, they reverse their direction.

# After reversing direction at position 5, they move 1 step to the left and land on position 4. Total moves till now: 5.

# Now, with the reversed direction, the player is at position 4 where the value is -3. In the reversed direction, -3 indicates 3 steps to the right. But this would again lead to the right boundary of the array. Since they have already reversed direction once, they cannot move further in any direction and the game ends.

# At the end of the game, the player is at position 4 having made a total of 5 moves, thereby, the function returns (4, 5).

def evaluatePath(numbers):
    position = 0
    moves = 0
    direction = 1
    reversed = False
    
    while 0 <= position < len(numbers) and numbers[position] != 0:
        next_pos = position + numbers[position] * direction
        
        if next_pos < 0 or next_pos >= len(numbers):
            if reversed:
                return (position, moves)
            direction *= -1
            reversed = True
            continue
            
        position = next_pos
        moves += 1
        
    return (position, moves)

print(evaluatePath([3, 4, 1, 1, -3, 1])) # (4, 5)

import unittest

class EvaluatePathTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(evaluatePath([2, 1, -3, 4]), (2, 1))

    def test2(self):
        self.assertEqual(evaluatePath([0]), (0, 0))

    def test3(self):
        self.assertEqual(evaluatePath([3, 4, 1, 1, -3, 1]), (4, 5))

    def test4(self):
        self.assertEqual(evaluatePath([3, -3]), (0, 0))

    def test5(self):
        self.assertEqual(evaluatePath([3, 2, -1, 2, 2, -1, 4]), (1, 7))

    def test6(self):
        self.assertEqual(evaluatePath([1]*500), (0, 998))    

if __name__ == '__main__':
    unittest.main()