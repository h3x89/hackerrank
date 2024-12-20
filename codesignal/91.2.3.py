# https://learn.codesignal.com/course/91/unit/2/practice/3

# Your task is to implement a function that duplicates every digit in a given non-negative integer number, n. For example, if n equals 1234, the function should return 11223344.

# To prevent possible integer overflow, it is guaranteed that n will be a non-negative integer that does not exceed 10^4. Solve this task without converting n into a string or performing any other type of casting. Your job is to work strictly with integer operations.

# Keynote:
# Focus on the essence of the problem, which is processing each digit of the number independently while maintaining the digit order. There is no need to look for mathematical patterns or clever simplifications; plain and straightforward processing will suffice. Utilize the toolbox of basic programming skills: loops, conditions, and mathematical operations. Good luck!

def solution(n):
    result = 0
    multiplier = 1
    
    # Handle special case for 0
    if n == 0:
        return 0
        
    while n > 0:
        digit = n % 10
        # Add the digit twice, shifting the second one by multiplier
        result += (digit * multiplier) + (digit * multiplier * 10)
        multiplier *= 100  # Move two positions for next digit pair
        n //= 10
    return result

print(solution(1234))

import unittest

class SolutionTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution(1234), 11223344)

    def test2(self):
        self.assertEqual(solution(1), 11)

    def test3(self):
        self.assertEqual(solution(22), 2222)

    def test4(self):
        self.assertEqual(solution(9876), 99887766)

    def test5(self):
        self.assertEqual(solution(10000), 1100000000)

    def test6(self):
        self.assertEqual(solution(0), 0)

    def test7(self):
        self.assertEqual(solution(3333), 33333333)

    def test8(self):
        self.assertEqual(solution(4444), 44444444)

    def test9(self):
        self.assertEqual(solution(5555), 55555555)

    def test10(self):
        self.assertEqual(solution(6666), 66666666)

if __name__ == '__main__':
    unittest.main()