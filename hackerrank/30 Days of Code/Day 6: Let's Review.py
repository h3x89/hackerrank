# https://www.hackerrank.com/challenges/30-review-loop/problem?isFullScreen=true

input = input()
input = input.split("\n")
T = int(input[0]) # Number of test cases
# for i in range(1, T+1): # For each test case
#     S = input[i]
#     even = ""
#     odd = ""
#     for j in range(len(S)):
#         if j % 2 == 0:
#             even += S[j]
#         else:
#             odd += S[j]
#     print(even + " " + odd)

for test_case in range(1, T+1): # For each test case
    word = input[test_case]
    even = ""
    odd = ""
    for i in range(len(word)):
        if i % 2 == 0:
            even += word[i]
        else:
            odd += word[i]
    print(even + " " + odd)
    


# Simple input:
# 2
# Hacker
# Rank

# Simple output:
# Hce akr
# Rn ak
