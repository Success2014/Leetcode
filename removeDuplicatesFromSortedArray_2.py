# -*- coding: utf-8 -*-
"""
Created on Sat Aug 08 16:54:57 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        
        j = 0
        for i in xrange(1,n):
            if nums[j] != nums[i]:
                nums[j+1] = nums[i]
                j += 1
                
        return j+1
            