# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:14:11 2015

@author: Neo
"""

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        n1 = len(v1)
        n2 = len(v2)
        
        if n1 > n2:
            return -1 * self.compareVersion(version2, version1)
        
        for i in xrange(n1):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1
            else:
                if i == n1 - 1 and n1 == n2:
                    return 0
        
        for j in xrange(i+1, n2):
            if int(v2[j]) != 0:
                return -1
        
        return 0
            
            
            
            
            
            
            
            
            
            