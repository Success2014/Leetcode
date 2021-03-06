# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 11:19:31 2015

Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

Tags:  Backtracking
Similar Problems (M) Next Permutation 
(H) Permutations II (M) Permutation Sequence (M) Combinations



@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in xrange(len(nums)):            
            for j in self.permute(nums[:i]+nums[i+1:]):                
                res.append([nums[i]]+j)
        return res
        
        
        
sol = Solution()        
print sol.permute([1,2,3])
        
        