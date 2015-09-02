# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 15:27:01 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        d = {}
        res = set()
        for i in xrange(n):
            for j in xrange(i+1, n):
                s = nums[i] + nums[j]
                if d.has_key(s):
                    d[s].append((i,j))
                else:
                    d[s] = [(i,j)]
        
        for i in xrange(n):
            for j in xrange(i+1, n-2):
                tmp =  target - nums[i] - nums[j]
                if d.has_key(tmp):
                    for pair in d[tmp]:
                        if pair[0] > j:
                            res.add((nums[i],nums[j],nums[pair[0]],nums[pair[1]]))
        return [list(i) for i in res]
                    
                    