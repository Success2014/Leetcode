# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 18:03:38 2015

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

idea:
add from back to front, and insert 1 at the end
or add from front to back, adn insert 1 at the front

@author: Neo
"""

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        res = [1,1]
        for i in xrange(rowIndex-1): # number of repeated calculation
            for j in xrange(len(res)-1,0,-1): #只算到第0个数前
                res[j] += res[j-1]
            res.append(1)
        return res
        
#        for i in xrange(1, rowIndex): # number of repeated calculation
#            for j in xrange(i,0,-1): # j could be len(res)
#                res[j] = res[j] + res[j-1]
#            res.append(1)
#        return res
    
    def getRow2(self, rowIndex):
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in xrange(1, rowIndex):
            for j in xrange(len(res)-1):
                res[j] = res[j] + res[j+1]
            res.insert(0, 1)
        return res
        
        
sol = Solution()
print sol.getRow(4)        
print sol.getRow2(5)
        
        
        
        
        
        
        
        
        
        
        
        
        
        