# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:22:49 2015

Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. 
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
Tags: Array Backtracking
Similar Problems: (M) Combination Sum


@author: Neo
"""
from time import time
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()
        self.combHelper(candidates, [], target, res)
        return res
    
    def combHelper(self, candidates, cand, target, res):
#        if target < 0:
#            return
        if target == 0 and cand not in res:            
            res.append(cand[:])
            #must use[:], otherwise point to cand, will change
            #see http://www.codeskulptor.org/viz/index.html
            
        
        for i, val in enumerate(candidates):
            if target < val:
                return
            cand.append(val)
            self.combHelper(candidates[i+1:],cand,target-val,res)
            cand.pop()
        
        
c1 = [10,1,2,7,6,1,5]
t1 = 8
c2 = [24,31,6,19,18,30,7,33,10,10,10,15,21,33,31,10,9,15,22,6,13,11,24,17,28,33,26,9,24,11,28,14,29,29,28,12,17,22,33,14,19,8,25,27,7,13,24,33,23,12,34,24,10,23,28,25,22] 
t2 = 26
c3 = [14,22,8,31,30,26,9,34,20,13,10,22,6,12,18,22,28,19,14,17,24,24,22,14,27,30,6,23,25,14,33,5,23,7,23,18,28,20,9,5,20,14,22,21,21,6,9,6,12,10,19,31,21,28,32,14,23,33,32,14]
t3 = 29
sol = Solution()
t0 = time()
print sol.combinationSum2(c3,t3)
print 'Time consumed: %2.3f' %(time()-t0), "s"
        
        
        
        
        
        
        
        
        
        
        
        
        
