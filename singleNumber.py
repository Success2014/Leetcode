# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 21:41:02 2015

Given an array of integers, every element appears twice except for one. 
Find that single one.

Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?

用Hash table,一个一个放进去，看到重复就pop，这样到最后就只剩一个。但是这样做用了extra memeory.

Solution:

XOR-ing a number with itself is zero. If we XOR all numbers together, it would
effectively cancel out all elements that appear twice leaving us with only the single
number. As the XOR operation is both commutative and associative, the order in how
you XOR them does not matter.

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res = res ^ num
        return res


sol = Solution()
print sol.singleNumber([1,2,2,23,5,1,23])        
print sol.singleNumber([1,2,2,23,23,2,2,2,5,2,1,1,1])#如果是偶数次，也成立