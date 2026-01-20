# Link: https://leetcode.com/problems/valid-palindrome/

"""Problem Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


# Solution: Time Complexity:O(N^2) Space Complexity: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_org=""
        for i in range(len(s)):
            if (s[i].isalnum()):
                clean_org+=s[i].lower()
        
        rev_org=""
        for i in range(len(clean_org)-1, -1, -1):
            rev_org+=clean_org[i]
        
        return clean_org==rev_org

# Alternate Solution: Time Complexity:O(N^2) Space Complexity: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        proper_string=""
        for i in range(len(s)):
            if (s[i].isalnum()):
                proper_string+=s[i].lower() # time complexity is more due to the fact that "strings are immutable", 
                                            # so inside this happening: "Allocate new memory → copy all characters from the old string → add the new character"
        
        return proper_string=="".join(reversed(proper_string))


# Alternate Solution:  Time Complexity:O(N) Space Complexity: O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0; j=len(s)-1
        while i<j:
            while (i<j and not s[i].isalnum()):
                i+=1
            while(i<j and not s[j].isalnum()):
                j-=1
            if (s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
        return True
