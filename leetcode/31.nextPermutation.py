# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is impossible, it must rearrange it to the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        
        while i >= 0 and nums [i + 1] <= nums[i]:
            i -= 1
        
        if i >= 0 :
            j = len(nums) - 1
            while(nums[j] <= nums[i]):
                j -= 1
            
            self.swap(nums, i, j)
        
        self.reverse(nums, i + 1)
        

    def nextPermutation2(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1   
        
        
        
    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        
    def reverse(self, nums, start):
        i = start
        j = len(nums) - 1
        while ( i < j):
            self.swap(nums, i, j)
            i += 1
            j -= 1