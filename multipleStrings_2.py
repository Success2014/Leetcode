# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 16:26:14 2015

@author: Neo
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        prodt = [0 for i in range(len(num1)+len(num2))]
        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                prodt[i+j] += int(num1[i]) * int(num2[j])
        
        res = 0
        t = 1
        for i in xrange(len(prodt)):
            res += prodt[i]*t#prodt[i]最大81，乘以t不会溢出，但是没有之前的算法快
            t *= 10
        return str(res)


sol = Solution()        
print sol.multiply("25","25")