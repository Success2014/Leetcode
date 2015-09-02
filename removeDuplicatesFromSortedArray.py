# -*- coding: utf-8 -*-
"""
Created on Wed Jun 03 11:24:21 2015

题目意思是要让所有unique的数都在数组最前面，同时返回unique数的长度.
用双指针。一个用来扫描数组，另一个用来保存unique number 的位置。

@author: Neo
"""

def removeDuplicates(nums):
    if len(nums) <= 1:
        return len(nums)
    
    j = 0 # pointer of last position of different number
    
    for i in xrange(1, len(nums)):
        if nums[j] != nums[i]:
            nums[j + 1] = nums[i]
            j += 1
    return j + 1


nums = [1,1,2,2,4,4,4,4,4,4,5,6,6,6,6]
print removeDuplicates(nums)
    