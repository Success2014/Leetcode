# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:24:21 2015

@author: Neo
"""

def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    
    j = 0 # pointer of last position of different number
    
    for i in xrange(1, len(nums)):
        if nums[i] != nums[j]:
            nums[j + 1] = nums[i]
            j += 1
    return j + 1


nums = [1,1,2,2,4,4,4,4,4,4,5,6,6,6,6]
print removeDuplicates(nums)
    