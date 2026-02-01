# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

"""Problem Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""


# Solution:
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        for i in range(len(nums)):
            if (nums[i]!=nums[j]):
                j+=1
                nums[i], nums[j] = nums[j], nums[i]
        return j+1
