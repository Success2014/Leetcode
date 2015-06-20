# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 14:22:06 2015

Count the number of prime numbers less than a non-negative number, n.

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes1(self, n): # this method times out, too slow
        if n <= 2:
            return 0
        if n == 3:
            return 1
            
        count = 0
        for i in xrange(n):
            if self.isPrime(i):
                count += 1
        return count
        
        
    def isPrime(self, num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for x in xrange(3, int(num**0.5)+1, 2):
            if num % x == 0:
                return False
        return True
    
    '''
    逆向思维，反着堆上去
    '''    
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [0,0] + [1]*(n-2) # total length is n
        for i in xrange(2, int(n**0.5)+1):
            if primes[i] == 1:
                for j in xrange(i*i, n, i):
                    primes[j] = 0
    
        return sum(primes)
        
sol = Solution()
print sol.countPrimes(0)
print sol.countPrimes(4)        
print sol.countPrimes(5)        
print sol.countPrimes(6)        
print sol.countPrimes(7)        
print sol.countPrimes(8)        
        
        
        
        
        
        