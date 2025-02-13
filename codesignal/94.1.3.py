# https://codesignal.com/learn/course/94/unit/1/practice/3

# Alice enjoys playing a jumping game on two parallel roads, roadA and roadB, each filled with integers. The game begins with Alice choosing a starting point on roadA, and then moving according to the following rules:

# 1. Alice selects a starting point on roadA.
# 2. Each element in both roads dictates exactly where to jump on the other road. If Alice is at the i-th position of roadA, where roadA[i] = x, then she moves to the x-th position of roadB. Similarly, if Alice is at the i-th position of roadB, where roadB[i] = y, then she moves to the y-th position of roadA.
# 3. Alice continues these jumps until she ends up at an already visited spot on either road in the current route, which signifies the end of this game. It's important to note that if a spot was visited in a previous route but not in the current route, it is not considered as an already visited spot.
# 4. The distance covered in each jump is defined as 1 unit, no matter where she jumps to on the other road.

# Your task is to create a function that receives these two roads, roadA and roadB, as its parameters. The function should calculate and return an array of total distances Alice covers during her game for each possible starting point on roadA. More specifically, the result should be an array results, where results[i] denotes the total distance covered if Alice starts from roadA[i].

# The two input lists, roadA and roadB, contain n and m number of elements respectively. The number of elements in each list can range from 1 to 100, inclusive. Each element in roadA can have a value ranging from 0 to m−1, inclusive. Similarly, each element in roadB can have a value ranging from 0 to n−1, inclusive. This ensures that any element in either of the lists will be a valid index in the other list.

# Example

# For instance, if Alice's roads are given as roadA = [1, 0, 2] and roadB = [2, 0, 1], the function should return [2, 4, 4] because:

# - If Alice starts from roadA[0], her first jump takes her to roadB[1]. The value at this index tells her to jump to roadA[0], but since that's where she started this route (and thus it's already visited), she stops. As a result, Alice covers a total distance of 2 units.

# - If Alice starts from roadA[1], she jumps to roadB[0] which then redirects her to roadA[2]. From roadA[2], she jumps to roadB[1] which then leads her to roadA[0]. From roadA[0], she jumps to roadB[1] again but realizes this is the spot she has already visited in this route. Thus, in this case she covers a total distance of 4 units.

# - If Alice starts from roadA[2], her first jump takes her to roadB[2] and then the rule at this position directs her to roadA[1]. She has not yet visited roadA[1] in this route, so she follows the instruction and jumps to roadB[0], which also directs her to roadA[2], which she has visited in this route already so she stops there. Therefore, she covers a total distance of 4 units before landing on an already visited spot in her current route.

def solution(roadA, roadB):
    n = len(roadA)
    m = len(roadB)
    
    results = []
    
    for start in range(n):
        visited_A = set()
        visited_B = set()
        
        current_position_A = start
        distance = 0
        
        while True:
            if current_position_A in visited_A:
                break
            
            visited_A.add(current_position_A)
            distance += 1
            
            # Jump to roadB
            next_position_B = roadA[current_position_A]
            
            if next_position_B in visited_B:
                break
            
            visited_B.add(next_position_B)
            distance += 1
            
            # Jump back to roadA
            current_position_A = roadB[next_position_B]
        
        results.append(distance)
    
    return results

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution([1, 0, 2], [2, 0, 1]), [2, 4, 4])

    def test2(self):
        self.assertEqual(solution([0, 0, 0, 0, 0], [0, 0, 1, 2, 3]), [2, 3, 3, 3, 3])

    def test3(self):
        self.assertEqual(solution([1, 2, 3, 0], [2, 3, 0, 1]), [8, 8, 8, 8])

    def test4(self):
        self.assertEqual(solution([2, 2, 2, 2], [3, 2, 1, 0]), [3, 2, 3, 3])

    def test5(self):
        self.assertEqual(solution([1, 2, 1], [0, 2, 1]), [3, 2, 2])

if __name__ == '__main__':
    unittest.main()