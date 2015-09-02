# -*- coding: utf-8 -*-
"""
Created on Mon Aug 03 11:18:04 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        res = []
        self.helper(n,n,'',res)
        return res
    
    def helper(self,l,r,string,res):
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(string)
        if l > 0:
            self.helper(l-1,r,string+'(',res)
        if r > 0:
            self.helper(l,r-1,string+')',res)


sol = Solution()        
n = 3
print sol.generateParenthesis(n)