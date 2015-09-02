# -*- coding: utf-8 -*-
"""
Created on Fri Aug 07 17:00:39 2015

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