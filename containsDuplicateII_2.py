# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:35:14 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        
        for i,val in enumerate(nums):
            if val in d and i - d[val] <= k:
                return True
            d[val] = i
        return False