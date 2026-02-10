# Link: https://leetcode.com/problems/rotate-array/description/

"""Problem Description:
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

# Solution: T.C: O(N^2); O(1)
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
        
# Solution: T.C: O(N); O(1)
class Solution:
    def reverse(self, nums, i,j):
        while (i<=j):
            nums[i], nums[j]=nums[j], nums[i]
            i+=1; j-=1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1) 
        self.reverse(nums, k, len(nums)-1) 
        
