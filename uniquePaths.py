# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 14:27:54 2015

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

idea:
1 1 1 1 
1 2 3 4
1 3 6 10

@author: Neo
"""

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        """dynamic programming, 每个的步数是其左边和上面的步数的和"""
        if m == 1 and n == 1:
            res = [[1]]
        if m > 1 and n == 1:
            res = [[1] for i in range(n)]
        if m == 1 and n > 1:
            res = [[1 for i in range(n)]]
        else:
            res = [[1 for i in range(n)] for j in range(m)]
        
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = res[i][j-1] + res[i-1][j]
        return res[m-1][n-1]



sol = Solution()        
print sol.uniquePaths(3,4)
print sol.uniquePaths(2,1)