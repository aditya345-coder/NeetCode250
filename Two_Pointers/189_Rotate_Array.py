# Link: https://leetcode.com/problems/rotate-array/description/

"""Problem Description:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

# Solution: T.C: O(0); O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k%len(nums)):
            ele=nums[len(nums)-1]
            for j in range(len(nums)-1, -1,-1):
                nums[j]=nums[j-1]
            nums[0]=ele
        
# Solution: T.C: O(0); O(1)
