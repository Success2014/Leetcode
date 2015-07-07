# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 10:07:38 2015

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.


@author: Neo
"""

class Solution:
    # @param {string} num1
    # @param {string} num2
    # @return {string}
    def multiply(self, num1, num2):
        """这个能AC"""
        num1 = int(num1)
        num2 = int(num2)
        
        return str(num1*num2)
    
    def multiply2(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        arr = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                arr[i+j] += int(num1[i]) * int(num2[j])
        res = []
        for i in xrange(len(arr)):
            digit = arr[i] % 10
            carry = arr[i] / 10
            if i < len(arr) - 1:
                arr[i + 1] += carry
            res.insert(0, str(digit))
        while res[0] == "0" and len(res)>1:
            del res[0]
        return ''.join(res)


sol = Solution()        
print sol.multiply("125","80")
print sol.multiply2("125","80")
print sol.multiply2("0","0")
print sol.multiply2("9133", "0")
