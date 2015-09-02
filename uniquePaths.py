# -*- coding: utf-8 -*-
"""
Created on Fri Jul 03 14:27:54 2015

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Tags: Array Dynamic Programming
Similar Problems (M) Unique Paths II (M) Minimum Path Sum (H) Dungeon Game




Note: m and n will be at most 100.

idea:
1  1  1   1   1
1  2  3   4   5
1  3  6  10  15
1  4 10  20  35

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
    
    def uniquePaths2(self, m, n):
        """用组合的理论，比如上面4*5的格子，必须要向右走4步，向下走3步。
        你其实就是有7个格子。然后把RRRR和DDD放到这7个格子里面。当所有的R定了，
        D就定了。或者说当所有的D定了，R就定了。
        所以答案就是:
        m-1+n-1 choose m-1"""
        if m==1 and n==1:
            return 1
        return self.nChoosek(m+n-2,m-1)
    
    def fact(self, n):
        """return factorial of a non-negative number"""
        res = 1
        for i in xrange(1, n+1):
            res *= i
        return res
    
    def nChoosek(self, n, k):
        if n == 0:
            return 0
        elif k == 0:
            return 1
        else:
            return self.fact(n)/self.fact(k)/self.fact(n-k)



sol = Solution()        
print sol.uniquePaths(3,4)
print sol.uniquePaths(2,1)
print sol.uniquePaths(1,1)
print sol.uniquePaths2(3,4)
print sol.uniquePaths2(2,1)
print sol.uniquePaths2(1,1)