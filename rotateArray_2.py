# -*- coding: utf-8 -*-
"""
Created on Sun Aug 09 15:27:14 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        for i in xrange(k):
            tmp = nums.pop()
            nums.insert(0, tmp)
            
        