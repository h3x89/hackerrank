# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

# Problem:
# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Clarification:


# Example 1:

# Input: nums = [1,1,1,2,2,3]

# Output: 5, nums = [1,1,2,2,3]

import collections
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 1, -1): # Start from the end of the list
            current = nums[i]
            previous = nums[i-1]
            previous_previous = nums[i-2]

            if current == previous == previous_previous: # If the current element is equal to the previous element and the element before the previous element
                nums.pop(i) # Remove the current element
        print(nums)
        return len(nums)

p = Solution()
print(p.removeDuplicates([1, 1, 1, 2, 2, 3]))  # Output: 5, nums = [1, 1, 2, 2, 3]