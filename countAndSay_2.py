# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 10:04:23 2015

@author: Neo
"""

class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if n <= 0:
            return ''
        
        result = ['1']
        for i in xrange(n-1):
            count = 1
            prev = None
            tmp = []
            for s in result:
                if s == prev:
                    count += 1
                elif (prev is not None) and s != prev:
                    tmp.append(str(count))
                    tmp.append(str(prev))
                    count = 1
                prev = s
            tmp.append(str(count))
            tmp.append(str(prev))
            
            result = tmp
        return ''.join(result)