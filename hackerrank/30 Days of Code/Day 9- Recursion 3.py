# https://www.hackerrank.com/challenges/30-recursion/problem?isFullScreen=true

def factorial(n):
    # base case - if n <= 1, return 1
    if n <= 1:
        return 1
    # recursive call
    return n * factorial(n - 1)

if __name__ == '__main__':
    # Read input value:
    n = int(input().strip())

    # Call recursive function:
    result = factorial(n)

    # Print result:
    print(result)