# Link: https://leetcode.com/problems/longest-common-prefix/description/

"""Problem Description:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

# Solution:  T.C: O(nlogn), S.C: O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        strs1=strs[0]; strs2=strs[len(strs)-1]
        i=0
        while(i<len(strs1)):
            if (strs1[i]==strs2[i]):
                i+=1
            else:
                break
        return "" if i==0 else strs1[:i]
# Description: sort the array then compare the first and last elements and return the empty strings if index is 0 otherwise provide the substring till i.

# Solution:   T.C: O(n^2), S.C: O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(len(prefix)):
            for word in strs:
                if (i==len(word) or word[i]!=prefix[i]):
                    return prefix[:i]
        return prefix
