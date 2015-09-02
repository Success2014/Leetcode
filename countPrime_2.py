# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:24:37 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [0,0] + [1]*(n-2) # totally n slots
        for i in xrange(2, int(n**0.5)+1):
            if primes[i] == 1:
                for j in xrange(i*i, n, i):
                    primes[j] = 0
        
        return sum(primes)