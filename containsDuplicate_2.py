# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:30:26 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = 1
        
        return False