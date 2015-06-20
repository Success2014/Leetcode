# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 09:05:21 2015

ideas:two pointers i,j. i loop through nums, j is the starting pointer of 
numbers to keep. Numbers to the left of j are to discard

@author: Neo
"""

def removeElement(nums, val):
    j = 0
    
    for i in xrange(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j
    
    
nums = [4,5]
val = 4
print removeElement(nums, val)