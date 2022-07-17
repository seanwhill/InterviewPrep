from typing import *
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

import heapq

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1

    freq = [[]  for i in range(len(nums) + 1)]

    for key, value in count.items():
        freq[value].append(key)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if(len(res) == k):
                return res


# O(N + M + KlogN)
# N is nums in list. M is unique values
def topKFrequentHeap(self, nums, k):
  count = {}
  for num in nums:
      count[num] = count.get(num, 0) + 1
  
  heap = []
  
  for key, value in count.items(): #have to rearrange items because heap will sort by first value in the tuple
      heapq.heappush(heap, (-value, key)) #minheap by default so use negative value
      
  
  res = []
  for _ in range(k):
      val = heapq.heappop(heap) #logN heapPop
      res.append(val[1])
  
  return res



  
