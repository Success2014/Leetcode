# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:30:30 2015
https://gist.github.com/ElninoFong/d08051d98e634991cd93


@author: Neo
"""

class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
        n = len(prices)
        if n <= 1:
            return 0
        
        local = [0] * (k+1)
        glo = [0] * (k+1)
        for i in xrange(n-1):
            diff = prices[i+1] - prices[i]
            for j in xrange(k+1,0,-1):
                local[j] = max( glo[j-1] + max(diff,0), local[j-1]+diff)
                glo[j] = max(glo[j],local[j])
        return glo[k]

    def quickSolve(self, size, prices):
        sum = 0
        for x in range(size - 1):
            if prices[x + 1] > prices[x]:
                sum += prices[x + 1] - prices[x]
        return sum

sol = Solution()        
k = 3
prices = [4,2,6,3,4,1,8,2,6]
print sol.maxProfit(k,prices)