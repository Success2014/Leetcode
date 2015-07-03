# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 15:40:37 2015

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

@author: Neo
"""

class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        """dynamic programming, 每个的步数是其左边和上面的步数的和.
        如果有障碍，把那个格子设为0."""
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                res[i][0] = 1
            else:
                break
        for j in range(n):
            if obstacleGrid[0][j] == 0:
                res[0][j] = 1
            else:
                break
        
        for i in range(1, m):
            for j in range(1, n):                
                if obstacleGrid[i][j] == 0:                        
                    res[i][j] = res[i][j-1] + res[i-1][j]
        return res[m-1][n-1]


blockgrid1 = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]        
blockgrid2 = [[1,0]]

sol = Solution()
print sol.uniquePathsWithObstacles(blockgrid1)