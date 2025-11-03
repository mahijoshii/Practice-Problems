# Int pratice questions python

# Two sum
# Given an array nums and a target, return indices of the two numbers that add up to target.
# Assume exactly one solution and cannot use the same element twice.
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # value -> index
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in seen:
                return [seen[diff], i]
            seen[val] = i

