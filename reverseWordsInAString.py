# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:22:48 2015

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

Python处理string的能力很强大
@author: Neo
"""

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])
    def reverseWords2(self, s):
        res = ""
        j = len(s)
        for i in xrange(len(s) - 1, -1, -1):
            if s[i].isspace():
                j = i
            elif i == 0 or s[i - 1].isspace():
                if len(res) != 0:
                    res += " " 
                res += s[i:j]                
        return res
        



sol = Solution()        
print sol.reverseWords2(" a")
print len(sol.reverseWords2(" a"))