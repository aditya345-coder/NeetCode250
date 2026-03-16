# Link: https://leetcode.com/problems/contains-duplicate-ii/description/

"""Problem Description:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

## Brute Force Solution: Time Complexity: O(n^2)  Space Complexity: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i]==nums[j] and abs(i-j)<=k):
                    return True
        return False

##Solution: Time Complexity: O(n)  Space Complexity: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap={}
        for i in range(len(nums)):
            if (nums[i] not in hashmap):
                hashmap[nums[i]]=i
            else:
                if abs(hashmap[nums[i]]-i)<=k:
                    return True
                else:
                    hashmap[nums[i]]=i
        return False

## Alternate Solution: Time Complexity: O(n)  Space Complexity: O(1)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set(); l=0
        for r in range(len(nums)):
            if (r-l>k):
                window.remove(nums[l])
                l+=1
            if (nums[r] in window):
                return True
            window.add(nums[r])
        return False

