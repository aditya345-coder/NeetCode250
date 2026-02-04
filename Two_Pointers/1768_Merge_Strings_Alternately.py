# Link: https://leetcode.com/problems/merge-strings-alternately/

"""Problem Description:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

# Solution: T.C: O(n+m); S.C: O(n+m)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0; j=0
        merged_string=[]
        while(i<len(word1) or j<len(word2)):
            if (i<len(word1)):
                merged_string.append(word1[i])
                i+=1
            if (j<len(word2)):
                merged_string.append(word2[j])
                j+=1
        return "".join(merged_string)
