# -*- coding: utf-8 -*-
"""
Created on Thu Jun 04 09:05:21 2015

Given an array and a value, remove all instances of that value in place and 
return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond 
the new length.

Tags: Array Two Pointers
Similar Problems (E) Remove Linked List Elements



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