# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:12:52 2015

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        neg = 0        
        
        for i in xrange(32):
            sum = 0
            for num in nums:
                if num < 0:
                    neg += 1
                    num = ~(num - 1) #very important
                sum += (num >> i) & 1
            sum %= 3
            res |= (sum & 1) << i
        
        if neg % 3:
            res = - res
        return res
        

sol = Solution()        
print sol.singleNumber([1])
print sol.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])