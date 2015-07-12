# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:46:56 2015

Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Tags: Array Dynamic Programming
Similar Problems: (M) Unique Paths (H) Dungeon Game

idea:
Dynamic Programming.


@author: Neo
"""

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = grid
        for i in xrange(m):
            for j in xrange(n):
                if not ((i == 0) and (j == 0)):                    
                    if i == 0: # first row
                        res[i][j] += res[i][j-1]
                    elif j == 0: # first column
                        res[i][j] += res[i-1][j]
                    else:
                        res[i][j] += min(res[i-1][j],res[i][j-1]) 
#        print res
        return res[m-1][n-1]
    
    def minPathSum2(self, grid):
        """Another implementation of dynamic programming"""
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in xrange(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in xrange(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in xrange(1,m):
            for j in xrange(1,n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[m-1][n-1]
            
        
        
        


grid1 = [[1,2,3],[1,2,1],[3,1,2]]
grid2 = [[1,2,3]]
grid3 = [[1],[2],[3]]
sol = Solution()        
print sol.minPathSum2(grid1)
print sol.minPathSum2(grid2)
print sol.minPathSum2(grid3)