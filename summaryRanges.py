# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 16:17:26 2015

Given a sorted integer array without duplicates, return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        """两个指针"""
        res = []
        if len(nums) == 1:
            return [str(nums[0])]
        i = 0
        j = 0
        while j < len(nums):
            if j == len(nums) - 1 or nums[j+1] - nums[j] != 1:
                if j > i:
                    res.append("{0}->{1}".format(nums[i],nums[j]))
                else:
                    res.append(str(nums[j]))
                i = j + 1
            
            j += 1
        return res
    def summaryRanges2(self, nums):
        """https://leetcode.com/discuss/42199/6-lines-in-python
        holding the current range in an extra variable r to make things easier.
        Note that r contains at most two elements, so the in-check takes 
        constant time."""
        ranges, r = [], []
        for n in nums:
            if n-1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, x)) for x in ranges]


sol = Solution()
#print sol.summaryRanges2([])
print sol.summaryRanges2([0,1,2,4,5,7])    
print sol.summaryRanges2([0,1,2,3,5,7,9,10])