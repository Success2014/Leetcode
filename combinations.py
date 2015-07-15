# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 11:04:56 2015

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Tags: Backtracking
Similar Problems: (M) Combination Sum (M) Permutations


idea: 用递归穷举

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if n < 1:
            return []
        if n < k:
            return []
        
        res = []
        curt = []
        self.helper(1, n, k, curt, res)
        return res
    
    def helper(self, i, n, k, curt,res):
        
        if len(curt) == k:            
            res.append(curt)            
            return 
        for j in xrange(i, n+1):            
            self.helper(j+1,n,k,curt+[j],res)
        
        
        

sol = Solution()
print sol.combine(4,3)
        

        
        
        
        
        
        
        