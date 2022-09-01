
# 53. Maximum Subarray
# Easy

# 20075

# 977

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23

from typing import List
import sys


def maxSubArray( nums: List[int]) -> int:       
    MAX_SUM = -sys.maxsize - 1
    CURR_SUM = 0        
    for i in range(0,len(nums)):
        CURR_SUM += nums[i]            
        if(MAX_SUM < CURR_SUM):
            MAX_SUM = CURR_SUM
            
        if (CURR_SUM < 0):
            CURR_SUM = 0
    
    return MAX_SUM

print(maxSubArray(nums=[-3,8,-2,4,-5,6]))
        