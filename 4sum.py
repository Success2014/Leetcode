# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:28:09 2015

Given an array S of n integers, are there elements a, b, c, and d in S 
such that a + b + c + d = target? Find all unique quadruplets in the 
array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        d = {}
        res = set()
        for p in xrange(n):
            for q in xrange(p+1,n):
                if nums[p] + nums[q] not in d:
                    d[nums[p] + nums[q]] = [(p,q)]
                else:
                    d[nums[p] + nums[q]].append((p,q))
        for i in xrange(n):
            for j in xrange(i+1, n-2):
                if target - nums[i] - nums[j] in d:
                    for k in d[target - nums[i] - nums[j]]:
                        if k[0] > j:
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]
        
        
sol = Solution()
print sol.fourSum([1, 0, -1, 0, -2, 2],0)
        
        
        
        
        