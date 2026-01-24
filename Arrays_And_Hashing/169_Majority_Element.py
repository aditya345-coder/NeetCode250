# Link: https://leetcode.com/problems/majority-element/description/

"""Problem Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

# Solution: T.C: O(n), S.C: O(n)
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=hashmap.setdefault(nums[i], 0)+1
        
        majority=len(nums)//2

        for key,val in hashmap.items():
            if (val>majority):
                return key
        
        return 0

# Solution: T.C: O(n) S.C: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer Moore's voting algorith - used for finding majority
        ## It has 2 steps:
        ### first find the candidate to be majority element
        ### Confirm wheather it is a majority element or not.
        count=0; cand=0
        for i in range(len(nums)):
            if (count==0):
                cand=nums[i]
            if (nums[i]==cand):
                count+=1
            else:
                count-=1
        
        return cand
