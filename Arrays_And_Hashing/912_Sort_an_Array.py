# Link: https://leetcode.com/problems/sort-an-array/description/

"""Problem Description:
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
"""


# Solution: T.C: O(n^2), S.C: O(1)  - Insertion sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key=nums[i]
            j=i-1
            while(j>=0 and key<nums[j]):
                nums[j+1]=nums[j]
                j-=1
            nums[j+1]=key
        return nums



# Solution: T.C: O(n^2), S.C: O(1) - Selection sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            minimum=i
            for j in range(i+1, len(nums)):
                if (nums[j]<nums[minimum]):
                    minimum=j
            nums[i], nums[minimum]=nums[minimum], nums[i]
        return nums


# Solution: T.C: O(n^2), S.C: O(1) - Bubble sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if (nums[j]>nums[j+1]):
                    nums[j], nums[j+1]=nums[j+1], nums[j]

        return nums

# Solution: T.C: O(n^2), S.C: O(1) - Optimized Bubble sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        swapped=False
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if (nums[j]>nums[j+1]):
                    nums[j], nums[j+1]=nums[j+1], nums[j]
                    swapped=True
            if not swapped:
                break
        return nums

# Solution: T.C: O(nlogn), S.C: O(n) - Merge sort
class Solution:
    def merge_sort(self, nums, left, right):
        if (left<right):
            mid=(left+right)//2
            self.merge_sort(nums, left,mid)
            self.merge_sort(nums, mid+1, right)
            self.merge(nums, left, mid, right)

    def merge(self, nums, p, q, r):
        n1=q-p+1; n2=r-q

        l1=[0]*n1; l2=[0]*n2

        for i in range(n1):
            l1[i]=nums[p+i]
        
        for j in range(n2):
            l2[j]=nums[q+1+j]
        
        i=0; j=0; k=p

        while(i<n1 and j<n2):
            if (l1[i]<=l2[j]):
                nums[k]=l1[i]
                i+=1
            else:
                nums[k]=l2[j]
                j+=1
            k+=1
        
        while (i<n1):
            nums[k]=l1[i]
            k+=1; i+=1
        
        while (j<n2):
            nums[k]=l2[j]
            k+=1; j+=1
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums)-1)
        return nums
        
