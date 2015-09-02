# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 22:10:31 2015

@author: Neo
"""

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        res = [[0 for i in xrange(n)] for j in xrange(m)]
        
        for j in xrange(n):
            if obstacleGrid[0][j] == 0:
                res[0][j] = 1
            else:
                break
        
        for i in xrange(m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                break
        for i in xrange(1,m):
            for j in xrange(1,n):
                if obstacleGrid[i][j] == 0:
                    res[i][j] = res[i][j-1] + res[i-1][j]
                else:
                    res[i][j] = 0
                        
        return res[m-1][n-1]
        
        
        
obstacleGrid = [[0,0]]        
sol = Solution()
print sol.uniquePathsWithObstacles(obstacleGrid)