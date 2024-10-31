#  https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# Difficulty: Easy
# Description: Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(nums.count(val)):
            nums.remove(val)