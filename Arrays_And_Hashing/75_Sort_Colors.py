# Link: https://leetcode.com/problems/sort-colors/description/

"""Problem Description:
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

# Alternate Solution:  T.C: O(3*N), S.C: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0=0; c1=0; c2=0
        for i in range(len(nums)):
            if (nums[i]==0):
                c0+=1
            elif (nums[i]==1):
                c1+=1
            else:
                c2+=1
        
        idx=0
        for i in range(c0):
            nums[idx]=0
            idx+=1
        for i in range(c1):
            nums[idx]=1
            idx+=1
        for i in range(c2):
            nums[idx]=2
            idx+=1
        return nums



# Solution: T.C: O(N), S.C: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0; mid=0; high=len(nums)-1
        while(mid<=high):
            if (nums[mid]==0):
                nums[low], nums[mid]=nums[mid], nums[low]
                low+=1; mid+=1
            elif (nums[mid]==1):
                mid+=1
            else:
                nums[high], nums[mid]=nums[mid], nums[high]
                high-=1
                
        return nums
