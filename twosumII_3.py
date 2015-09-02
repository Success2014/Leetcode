# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:14:36 2015

@author: Neo
"""

def twosum(nums, target):
    
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] + nums[j] == target:
            return (i+1, j+1)
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            i += 1
    
    return (-1, -1)
    

nums1 = [1,2,3,4]
t1 = 5
print twosum(nums1,t1)

nums2 = [4,8,10,29,31]
t2 = 42
print twosum(nums2,t2)
    

    
    
    
    
    
    
    
    