# You are given an input array consisting of n integers ranging from 0 to 100, inclusive, where n represents the length of the array. Your task is to return a new array of tuples. Each tuple should consist of an element from the input array paired with its geometrical mean with the 'opposite' element. The 'opposite' element of any element in the array is defined as the element at the corresponding position from the end of the array.

# Assume that the geometrical mean of two numbers, a and b, is calculated as: 
# sqrt
# (
# a
# ×
# b
# )
# sqrt(a×b), where sqrt stands for square root.

# A few notes:

# If the length of the array, n, is odd, the middle element is considered to be its own 'opposite'.
# The elements of the input array will be in the range from 
# 0
# 0 to 
# 100
# 100, inclusive.
# Calculate the geometrical mean to two decimal places. For example, the geometrical mean of 
# 2
# 2 and 
# 8
# 8 is 
# 4.00
# 4.00 (since 
# sqrt
# (
# 2
# ×
# 8
# )
# =
# 4
# sqrt(2×8)=4).
# Round down to two decimal places. For instance, the geometrical mean of 2 and 8 is 4.00, not 4.472.
# For example, for numbers = [1, 2, 3, 4, 5], the output should be solution(numbers) = [(1, 2.24), (2, 2.83), (3, 3.0), (4, 2.83), (5, 2.24)].

def solution(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        opposite = numbers[n - i - 1]
        mean = (numbers[i] * opposite) ** 0.5
        result.append((numbers[i], round(mean, 2)))
    return result

print(solution([1, 2, 3, 4, 5]))