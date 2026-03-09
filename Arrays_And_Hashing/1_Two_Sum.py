# Link: https://leetcode.com/problems/two-sum/description/


"""Problem Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# Brute Force Solution: Time Complexity: O(n^2), Space Complexity: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        # Return an empty list if no solution is found
        return []

# Solution: Time Complexity: O(n), Space Complexity: O(n) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            val=target-nums[i]
            if (val in hashmap.keys()):
                return [i, hashmap.get(val)]
            hashmap[nums[i]]=i
        return [-1,-1]

