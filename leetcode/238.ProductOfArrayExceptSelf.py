from typing import *

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


#prefix * postfix
def productExceptSelf(self, nums: List[int]) -> List[int]:
  prefix = [1] * len(nums)
  for i in range(len(nums)): #prefix
      if i == 0:
          prefix[0] = nums[i]
      else:
          prefix[i] = prefix[ i - 1 ] * nums[i]

  postfix = [1] * len(nums)
  for i in range(len(nums) - 1, 0, -1): #postfix
      if i == len(nums) - 1:
          postfix[i] = nums[i]
      else:
          postfix[i] = postfix[i + 1] * nums[i]

  res = []
  for i in range(len(nums)):
      prefixVal = 1
      postfixVal = 1
      if i != 0:
          prefixVal = prefix[i - 1]
      if i != len(nums) - 1:
          postfixVal = postfix[i + 1]
          
      res.append(prefixVal * postfixVal)
          
  return res

def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    
    return res