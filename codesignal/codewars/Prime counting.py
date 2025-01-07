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

def count_primes_less_than(n):
    
    # If n is less than 2, there are no prime numbers.
    if n < 2:
        return 0
    
    # Sieve of Eratosthenes algorithm:
    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

    # First, we create a list of n elements, all of them set to True.
    primes = [True] * n

    # We set the first two elements to False, since 0 and 1 are not prime numbers.
    primes[0] = primes[1] = False

    # We iterate over the list, starting from 2, and set all the multiples of the current number to False.
    for i in range(2, int(n ** 0.5) + 1):
        # If the current number is prime, we set all its multiples to False.
        if primes[i]:
            # We start from i * i, since all the numbers before that have already been marked as False.
            for j in range(i * i, n, i):
                primes[j] = False
    return sum(primes)

# Test cases:
print(count_primes_less_than(7)) # Expected: 3
print(count_primes_less_than(100)) # Expected: 25

