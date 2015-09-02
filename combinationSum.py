# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 17:48:11 2015

Given a set of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. 
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

Tags: Array Backtracking
Similar Problems: (M) Letter Combinations of a Phone Number 
(M) Combination Sum II (M) Combinations (M) Combination Sum III


@author: Neo
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        """DFS"""
        res = []
        candidates.sort()
        self.combHelper(candidates, [], target, res)
        return res
        
    def combHelper(self, candidates, cand, target, res):
        if target < 0:
            return
        if target == 0:
            res.append(cand[:])
        
        for i, val in enumerate(candidates):
            cand.append(val)
            self.combHelper(candidates[i:], cand, target - val, res)
            cand.pop()
    
    
    def combinationSum2(self, candidates, target):
        """DFS. Use a stack. total is the sum up to now. 
        start is the starting point,
        no need to look at the old numbers.
        res is a list to tracking the progress."""
        candidates.sort()
        stack = [(0,0,[])]
        result = []
        while stack:
            total, start, res = stack.pop()
            if total == target:
                result.append(res)
            for i in xrange(start, len(candidates)):#w/o start, there'll be duplicates
                t = total + candidates[i]
                if t > target:
                    break
                stack.append((t, i, res + [candidates[i]]))
        
        return result
        
    
    
        
sol = Solution()        
print sol.combinationSum([2,3,6,7],7)
print sol.combinationSum2([2,3,6,7],7)        

        
        
        
        
        
        
        
        
        
        
        
        
        
        