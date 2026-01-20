# Link: https://leetcode.com/problems/longest-common-prefix/description/

"""Problem Description:
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


## Solution: T.C: O(N^2), S.C: O(N)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result=strs[0]
        for i in range(1, len(strs)):
            max_prefix=""
            for j in range(min(len(result),len(strs[i]))):
                if (len(result)==0 or result[j]!=strs[i][j]):
                    break
                max_prefix+=strs[i][j]
            result=max_prefix
        return result
