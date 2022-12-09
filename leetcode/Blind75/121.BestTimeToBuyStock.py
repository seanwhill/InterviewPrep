from typing import *

def maxProfit(self, prices: List[int]) -> int:
    maxProf = 0
    
    l ,r = 0, 1
    
    while r < len(prices):
        
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxProf = max(profit, maxProf)
        else:
            l = r
        
        r += 1
    
    return maxProf

def maxProfit(self, prices: List[int]) -> int:
    res = 0
    
    l = 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
    return res