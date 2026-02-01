# Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

"""Problem Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

# Solution: T.C: O(n), S.C: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        map={}; temp_target=target
        for i in range(len(numbers)):
            temp_target-=numbers[i]
            if (temp_target in map):
                return [map[temp_target], i+1]
            else:
                map[numbers[i]]=i+1
            temp_target=target
        return [0,0]

# Solution: T.C: O(N), S.C: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0; j=len(numbers)-1
        while (i<j):
            if (numbers[i]+numbers[j]==target):
                return [i+1,j+1]
            elif (numbers[i]+numbers[j]<target):
                i+=1
            else:
                j-=1
        return [-1,-1]
