# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
from typing import *

#O(n^2)
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            #break out if it's greater than 0 because there will never be any negatives in the rest of the list since it's sorted
            if i ==0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res
        
    def twoSum(self, numbers: List[int], i : int, res: List[List[int]]):
        l =  i + 1
        r = len(numbers) - 1
        
        while(l < r):
            
            sum = numbers[i] + numbers[l] + numbers[r]
                                                    
            if sum == 0:
                res.append([numbers[i], numbers[l], numbers[r]])
                #Don't repeat so we move pointers down and up and see if there's anything left
                l += 1
                r -= 1
                while l < r and numbers[l] == numbers[l-1]:
                    l += 1
                        
            elif sum > 0:
                r -= 1
            else:
                l += 1