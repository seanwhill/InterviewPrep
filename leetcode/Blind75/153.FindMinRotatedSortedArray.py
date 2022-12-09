from typing import *

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        mid = -1
        res = 5001
        while l <= r:
            
            mid = (l + r) // 2
            res = min(nums[mid], res)

            #left
            if nums[l] <= nums[mid]:
                if nums[l] > nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right
            else:
                if nums[l] > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
                    
                    
                    
        return res