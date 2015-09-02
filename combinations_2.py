# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:32:37 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        res = []
        curt = []
        self.dfs(1,n,k,curt,res)
        return res
    
    def dfs(self, start, n, k, curt, res):
        if len(curt) == k:
            res.append(curt[:])
            return
        for i in xrange(start, n+1):
            
            self.dfs(i+1, n, k, curt+[i], res)
        