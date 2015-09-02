# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:50:54 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
            return 0
        odd = 0
        even = 0
        for i in xrange(len(nums)):
            if i % 2:
                odd = max(odd+nums[i],even)
            else:
                even = max(even+nums[i],odd)
        return max(odd,even)