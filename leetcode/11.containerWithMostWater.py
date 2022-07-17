# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

from typing import *

class Solution:
    #Pretty sure this could fail in some use cases. Passes leetcode though
    def maxArea_moreEfficient(self, height: List[int]) -> int:
        max_area = 0
        N = len(height)
        left = 0
        right = N - 1
        
        while left < right:
            h = min(height[left], height[right])
            area = (right - left) * h
            if area > max_area:
                max_area = area
                
            while height[left] <= h and left < right:
                left += 1
                
            while height[right] <= h and left < right:
                right -= 1
                
        return max_area

    #mySolution    
    def maxArea(self, height: List[int]) -> int:
        maxArea = l = 0
        r = len(height) - 1
        
        while l < r:
            
            maxArea = max(maxArea, ( min(height[l], height[r]) * (r - l) ))
            if(height[l] > height[r]):
                r -= 1
            else:
                l += 1
        
        return maxArea