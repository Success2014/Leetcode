# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 14:32:12 2015

Given n pairs of parentheses, write a function to generate all combinations of 
well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"

Tags: Backtracking String
Similar Problems (M) Letter Combinations of a Phone Number 
(E) Valid Parentheses

idea:
列举出所有合法的括号匹配，使用dfs。
如果左括号的数量大于右括号的数量的话，就不能产生合法的括号匹配。

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        self.helper(n,n,'',res)
        return res
    
    def helper(self, l, r, string, res):
        """l是左括号剩余数量，r是右括号剩余数量"""
        if r < l: # discard ')('
            return
        if l == 0 and r == 0:
            res.append(string)            
        if l > 0:
            self.helper(l-1,r,string+'(',res)
        if r > 0:
            self.helper(l,r-1,string+')',res)


sol = Solution()
print sol.generateParenthesis(1)