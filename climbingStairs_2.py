# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 12:14:50 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        dp = [1,1]
        for i in xrange(2,n+1):
            dp[0],dp[1] = dp[1],sum(dp)
        return dp[1]