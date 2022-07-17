from typing import *

def twoSum(self, nums: List[int], target: int) -> List[int]:
    sumDict = {}
    
    for i in range(len(nums)):
        num = nums[i]
        
        if(num in sumDict):
            return [sumDict[num], i]
        
        sumDict[target - num] = i
    