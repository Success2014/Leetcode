# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:41:29 2015

Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.

idea:
Use dynamic programming.
Initialization with the last row.
Go one level down each step.
Dynamically update the list from back to front.
0  0  0   0
2  0  0   0
5  6  0   0
11 10 13  0
15 11 18 16


@author: Neo
"""

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        
        res = [0 for i in range(len(triangle))]
        res[0] = triangle[0][0]
        
        for i in xrange(1, len(triangle)):
            for j in xrange(len(triangle[i])-1, -1, -1): # triangle[i]!!!
                if j == len(triangle[i]) - 1:#last one in a row only has 1 neigbor
                    res[j] = res[j-1] + triangle[i][j] 
                elif j == 0: # first one in a row only has 1 neighbor
                    res[j] = res[j] + triangle[i][j]
                else: # element in the middle has 2 neighbors
                    res[j] = min(res[j],res[j-1]) + triangle[i][j]
        print res                    
        return min(res)
        
        
t1 = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]        
        
sol = Solution()
print sol.minimumTotal(t1)
        
        
        
        
        