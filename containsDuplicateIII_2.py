# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:13:30 2015

@author: Neo
"""

import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        d = collections.OrderedDict()
        for i in xrange(len(nums)):
            key = nums[i]/t if t else nums[i]
            for j in (key-1, key, key+1):
                if j in d and abs(d[j] - nums[i]) <=t:
                    return True
            
            
        
            if len(d) == k:
                d.popitem(last=False)
                
            d[key] = nums[i]
        
        return False
                    
        
        