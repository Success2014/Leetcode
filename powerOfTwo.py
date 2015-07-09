# -*- coding: utf-8 -*-
"""
Created on Wed Jul 08 23:38:12 2015

Given an integer, write a function to determine if it is a power of two.


@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        """return false for non-positive. Or move one bit to right."""
        if n <= 0:
            return False
        count = 0
        while n!=1:
            count += n & 1
            n >>= 1
        return count == 0
        
    def isPowerOfTwo2(self, n):
        return (n>0) and (n & (n-1)==0)
    
    def isPowerOfTwo3(self, n):
        while n != 0 and n % 2 == 0:
            n = n/2
        return n == 1


sol = Solution()        
print sol.isPowerOfTwo3(1)
print sol.isPowerOfTwo3(2)
print sol.isPowerOfTwo3(3)
print sol.isPowerOfTwo3(4)
print sol.isPowerOfTwo3(5)
print sol.isPowerOfTwo3(6)

            
        
        
        
        
        
        
        
        
        
        
        