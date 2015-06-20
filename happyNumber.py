# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 16:00:52 2015

Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by the 
sum of the squares of its digits, and repeat the process until 
the number equals 1 (where it will stay), or it loops endlessly 
in a cycle which does not include 1. Those numbers for which 
this process ends in 1 are happy numbers.
Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1


@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):        
        num_set = set()
        while n != 1 and n not in num_set:
            num_set.add(n)
            summ = 0
            while n:
                digit = n % 10
                summ += digit*digit
                n /= 10
            n = summ
            
        return n == 1


sol = Solution()        
print sol.isHappy(0)
        
        
        
        
        
        
        
        
        
        
        