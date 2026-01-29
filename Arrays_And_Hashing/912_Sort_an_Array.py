# Link: https://leetcode.com/problems/sort-an-array/description/

"""Problem Description:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


# Solution: T.C: O(n^2), S.C: O(1)  - Insertion sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key=nums[i]
            j=i-1
            while(j>=0 and key<nums[j]):
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums



# Solution: T.C: O(n^2), S.C: O(1)
