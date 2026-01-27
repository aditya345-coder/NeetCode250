# Link: https://leetcode.com/problems/top-k-frequent-elements/description/


"""Problem Description:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""


# Solution: T.C: O(nlogn), S.C: O(n)
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            hashmap[nums[i]]=hashmap.setdefault(nums[i], 0)+1
        
        # Sort by value in descending order
        sorted_dict_desc = dict(sorted(hashmap.items(), key=lambda item: item[1], reverse=True))
        
        return list(sorted_dict_desc.keys())[:k]

# Alternate Solution: T.C: O(), S.C: O()


