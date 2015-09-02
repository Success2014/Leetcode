# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 12:14:34 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        curt = []
        self.dfs(candidates, target, curt, res)
        return res
    
    def dfs(self, candidates, target, curt, res):
        if target < 0:
            return
        if target == 0:
            res.append(curt[:])
            return
        for i in xrange(len(candidates)):
            curt.append(candidates[i])
            self.dfs(candidates[i:], target - candidates[i], curt, res)
            curt.pop()
            