# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:27:44 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        curt = []
        self.dfs(candidates, target, curt, res)
        return res
        
    def dfs(self, candidates, target, curt, res):
        
        if target == 0 and curt not in res:
            res.append(curt[:])
            return
        
        for i in xrange(len(candidates)):
            if target < candidates[i]:
                return
            
            curt.append(candidates[i])
            self.dfs(candidates[i+1:], target-candidates[i], curt, res)
            curt.pop()
        