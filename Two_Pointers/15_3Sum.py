# Link: https://leetcode.com/problems/3sum/

"""Problem Description:
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# Solution: T.C: O(n^3); S.C: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        summ=[]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[i]+nums[j]+nums[k]==0):
                        if (sorted([nums[i], nums[j], nums[k]]) not in summ):
                            summ.append(sorted([nums[i], nums[j], nums[k]]))
        return summ

# Alternate Solution: T.C: O(n^2); S.C: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(); result=[]
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j=i+1; k=len(nums)-1
            while(j<k):
                summ=nums[i]+nums[j]+nums[k]
                if (summ==0):
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                elif (summ<0):
                    j+=1
                else: 
                    k-=1
        return  result
