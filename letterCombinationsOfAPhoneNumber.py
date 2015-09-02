# -*- coding: utf-8 -*-
"""
Created on Sat Jul 04 16:09:47 2015

Given a digit string, return all possible letter combinations that the number 
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Although the above answer is in lexicographical order, your answer could 
be in any order you want.

Tags: Backtracking String
Similar Problems (M) Generate Parentheses (M) Combination Sum



Idea:
用brute force recursive.
'a': ad, ae, af
'b': bd, be, bf


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
            self.combinations(digits, 0, '', res, d)
        return res
        
    def combinations(self, digits, idx, string, res, d):
        if idx == len(digits):
            res.append(string)
            return
        for letter in d[digits[idx]]:
            string_new = string + letter #must use a new string, try string += letter
            self.combinations(digits, idx+1, string_new, res, d)
        
        
        
sol = Solution()        
print sol.letterCombinations('234')
        
        
        
        
        
        
        
        