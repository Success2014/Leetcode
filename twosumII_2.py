# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:45:18 2015

@author: Neo
"""

def twoSum(nums, target):
    L = 0
    R = len(nums) - 1
    
    while L < R:
        s = nums[L] + nums[R]
        if s == target:
            return (L+1,R+1)
        elif s < target:
            L += 1
        else:
            R -= 1
        
nums = [1,2,3,4,5,9,12,15,19,20,22,24]
print twoSum(nums, 35)        