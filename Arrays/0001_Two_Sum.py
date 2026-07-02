"""
LeetCode 1. Two Sum

Difficulty: Easy

Topics:
- Arrays
- Hash Map

Problem Summary:
Given an array of integers and a target value, return the indices
of the two numbers whose sum equals the target. Exactly one valid
pair exists, and the same element cannot be used twice.

Approach:
Use a hash map to store previously seen numbers and their indices.
For each element, calculate the required complement (target - current).
If the complement already exists in the hash map, return the two
indices immediately. Otherwise, store the current number and continue.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        s = {}

        for i in range(len(nums)):
            num = nums[i]
            remain = target - num

            if remain in s:
                return [s[remain], i]

            s[num] = i