# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 21:57:48 2015

@author: Neo
"""

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [[0 for i in xrange(n)] for j in xrange(m)]
        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[m-1][n-1]
        