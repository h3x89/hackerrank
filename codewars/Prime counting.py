# https://www.codewars.com/kata/638c92b10e43cc000e615a07

# You need to count the number of prime numbers less than or equal to some natural n.

# For example:

# count_primes_less_than(34) = 11
# count_primes_less_than(69) = 19
# count_primes_less_than(420) = 81
# count_primes_less_than(666) = 121

# 1 ≤ n ≤ 10^10
 
# Code length limited to 3000 characters to avoid hardcoding.
# Good luck!

from math import ceil

def count_primes_less_than(n):
    # Handle edge cases
    if n < 2:
        return 0
    
    # Create a boolean array "is_prime[0..n]" and initialize
    # all entries it as true. A value in is_prime[i] will
    # finally be false if i is Not a prime, else true.
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Use Sieve of Eratosthenes to mark non-prime numbers as false
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Update all multiples of i starting from i*i
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Count number of prime numbers
    return sum(is_prime)

# Test cases
print(count_primes_less_than(34))  # Expected: 11
print(count_primes_less_than(69))  # Expected: 19
print(count_primes_less_than(420)) # Expected: 81
print(count_primes_less_than(666)) # Expected: 121

# 100 random tests for n <= 10^6
import random

for _ in range(100):
    n = random.randint(0, 10 ** 6)
    print(f"{n}: {count_primes_less_than(n)}")


# import unittest

# class TestPrimeCounting(unittest.TestCase):
#   def test_count_primes_less_than_100(self):
#     self.assertEqual(count_primes_less_than(100), 25)

#   def test_count_primes_less_than_7(self):
#     self.assertEqual(count_primes_less_than(7), 3)

#   def test_count_primes_less_than(self):
#     self.assertEqual(count_primes_less_than(420), 81)
#     self.assertEqual(count_primes_less_than(666), 121)
#     self.assertEqual(count_primes_less_than(34), 11)
#     self.assertEqual(count_primes_less_than(69), 19)


# if __name__ == '__main__':
#   unittest.main()
    