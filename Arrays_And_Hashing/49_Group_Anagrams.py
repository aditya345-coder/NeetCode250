# Link: https://leetcode.com/problems/group-anagrams/description/

"""Problem Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""


## Solution: T.C: O(nlogn), S.C: (n)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for words in strs:
            dic["".join(sorted(words))].append(words)
        
        return list(dic.values())


## Alternate Solution: T.C: O(M*N), S.C: (N)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for word in strs:
            count=[0]*26
            for c in word:
                count[ord(c)-ord('a')]+=1
            lst=tuple(count)
            dic[lst].append(word)
        
        return list(dic.values())
