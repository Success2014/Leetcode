# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:18:34 2015

Related to question Excel Sheet Column Title
Given a column title as appear in an Excel sheet, 
return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 


@author: Neo
"""

class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        if not s:
            return 0
        letter_int = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                      'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                      'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
                      'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        
        lens = len(s)        
        used = 0
        for i in xrange(lens-1): # for AAA, then A-Z, AA-ZZ have been used
            used += 26**(i+1)
        curt = 0
        for j in xrange(lens):
            if j == lens - 1: # if it is the last digit
                curt += letter_int[s[j]]
            else: # not the last digit
                curt += (letter_int[s[j]] - 1) * (26**(lens-j-1))
        return used + curt
    def titleToNumber2(self,s):
        ans = 0
        letter_int = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,
                      'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,
                      'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,
                      'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
        for e in s:            
            ans = ans * 26 + letter_int[e] - letter_int['A'] + 1
        return ans
    """
    26 进制转成 10 进制
    """
    def titleToNumber3(self,s):
        ans = 0
        for e in s:
            ans = ans * 26 + ord(e) - ord('A') + 1
        return ans

sol = Solution()
print sol.titleToNumber3("AAA")














