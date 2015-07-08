# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 00:26:08 2015

Given an array of non-negative integers, you are initially positioned at the 
first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. 
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)


题目应该假设了数组里的数是能够到达最后的。

idea:
res: step needed
cur: how far we can reach now using res steps
nxt: how far we can reach next using res+1 steps


    [2, 1, 2, 3, 1, 1, 1]
res  0  1  1  2  2  3
cur  0  2  2  4  4  6
nxt  2  2  4  6  6  6
i    0  1  2  3  4  5  6 

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        res = 0
        cur = 0
        nxt = 0
        for i in xrange(len(nums)):
            if i > cur: # nothing needed when i <= cur
                res += 1
                cur = nxt
            nxt = max(nxt, i + nums[i])
            if cur >= len(nums) - 1:
                return res
#        return res


sol = Solution()        
print sol.jump([2, 1, 2, 3, 1, 1, 1])
print sol.jump([2,3,1,1,4])            
        
        
        
        
        
        
        