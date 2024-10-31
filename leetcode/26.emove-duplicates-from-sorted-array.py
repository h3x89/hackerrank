# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150

# Problem:
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the length of the list is 0, return 0
        if len(nums) == 0:
            return 0
        index = 0
        # Initialize a variable to keep track of the index
        for element in nums:
            # If the element is not equal to the element at the index
            if element != nums[index]:
                # Increment the index
                index += 1
                # Assign the element to the index
                nums[index] = element
        # Return num of unique elements
        # return nums[:index + 1]
        return index+1

# p = Solution()
# print(p.removeDuplicates([1, 1, 2]))  # Output: [1, 2]
# # print(p.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))  # Output: [0, 1, 2, 3, 4]