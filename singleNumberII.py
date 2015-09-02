# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 21:57:16 2015

Given an array of integers, every element appears three times except for one. 
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. 
Could you implement it without using extra memory?




@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber(self, nums):
        """差一点的办法就是用hash table记录每个数出现的次数。
        但是用了额外的memory."""
        d = {}
        for num in nums:
            if d.has_key(num):
                d[num] += 1
            else:
                d[num] = 1
        
        for key,val in d.items():
            if val == 1:
                return d[key]
    
    def singleNumber2(self, nums):
        """
        http://liangjiabin.com/blog/2015/03/leetcode-single-number-ii-in-python.html
        32位整数逐位计算，把数组中所有数的第i位加起来，模3得到的1或0便是x第i位的值。
        如数组[2, 2, 2, 1]，二进制位[10, 10, 10, 01]，最低位加起来是1，模3得1，
        第二位加起来是3，模3得0，所以要找的数为二进制01，即1。        
        python是弱类型，自动处理溢出。所以用一个flag来记录是否是负数"""
        
        res = 0
        neg = 0
        for i in xrange(32):
            sums = 0
            for num in nums:
                if num < 0:
                    neg += 1
                    num = ~(num - 1)#对负数减1取反
                sums += (num >> i) & 1
                sums %= 3
            res |= (sums & 1) << i
        if neg % 3 != 0:
            res = -res
        return res
    
    
    def singleNumber3(self, nums):
        one = 0
        two = 0
        three = 0
        for i in range(len(nums)):
            two |= nums[i] & one #two为1时，不管A[i]为什么，two都为1
            one = nums[i] ^ one  #异或操作，取nums[i]的值
            #以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。            
            three = one & two 
            one &= ~three
            two &= ~three
        return one
        
        
        


sol = Solution()
print sol.singleNumber3([8,8,8,1])        
        
        
        
        
        