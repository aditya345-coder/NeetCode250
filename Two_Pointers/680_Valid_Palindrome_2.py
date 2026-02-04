# Link: https://leetcode.com/problems/valid-palindrome-ii/description/

"""Problem Description:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

# Solution: T.C: O(n); S.C: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i=0; j=len(s)-1
        while (i<j):
            if (s[i]==s[j]):
                i+=1; j-=1
            else:
                return self.isPalindrome(s, i+1, j) or self.isPalindrome(s, i, j-1)
        return True

    def isPalindrome(self, s, i, j):
        while(i<j):
            if (s[i]==s[j]):
                i+=1; j-=1
            else:
                return False
        return True
