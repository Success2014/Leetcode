# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 09:16:53 2015

Implement pow(x, n).

二分法。注意处理负指数。

@author: Neo
"""

class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            return 1.0/self.myPow(x,-n)
        if n % 2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return self.myPow(x*x, n/2)*x
        return x*self.myPow(x,n-1)




sol = Solution()
print sol.myPow(2,3)
print sol.myPow(2,-1)