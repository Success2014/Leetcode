# -*- coding: utf-8 -*-
"""
Created on Wed Aug 05 10:30:39 2015

@author: Neo
"""

class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        d = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }
        res = []
        if digits:
            self.helper(res, digits, 0, d, '')
        return res
        
    def helper(self, res, digits, idx, d, string):
        if len(string) == len(digits):
            res.append(string)
            return 
        for letter in d[digits[idx]]:
            self.helper(res, digits, idx+1, d, string+letter)
        
        
        
        
        
        
        