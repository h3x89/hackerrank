# https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

# Objective
# Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

# Note:  is considered to be an even index.

# Example


# Print abc def

# Input Format

# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a string, .

# Constraints

# Output Format

# For each String  (where ), print 's even-indexed characters, followed by a space, followed by 's odd-indexed characters.

# Sample Input

# 2
# Hacker
# Rank
# Sample Output

# Hce akr
# Rn ak
# Explanation

# Test Case 0: 






# The even indices are , , and , and the odd indices are , , and . We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().

# Test Case 1: 




# The even indices are  and , and the odd indices are  and . We then print a single line of  space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for i in range(n):
    s = input()
    # This line uses string slicing to split and print characters:
    # s[::2] takes every 2nd char starting from index 0 (even indices)
    # s[1::2] takes every 2nd char starting from index 1 (odd indices)
    # The space between them creates the required format
    print(s[::2], s[1::2])
    