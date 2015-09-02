# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 11:28:11 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = grid[0][0]
        
        for j in xrange(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in xrange(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
        
        