# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:33:48 2015

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. 
Return its length: 4.

Your algorithm should run in O(n) complexity.

Tags Array

idea:
用hashmap记录每一个数是否被访问过。
对于数组的每一个数都一直往上+1，往下-1确定两边的长度。

用dictionary, get item的平均时间复杂度为O(1), 可以把key设为list中的数, value用于
标记是否访问过。遍历所有的key, 不断找寻其+1和-1得到的值是否在dictionary中, 
记下最长的连续序列长度。


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        d = {x : False for x in nums}#False is not visited
        maxLen = -1 
        for num in d:
            if d[num] == False:
                high = num + 1
                highLen = 0 # length of larger numbers
                while d.has_key(high) and d[high] == False:
                    highLen += 1
                    d[high] = True
                    high +=1
                    
                
                low = num - 1
                lowLen = 0 # length of smaller numbers
                while d.has_key(low) and d[low] == False:
                    lowLen += 1
                    d[low] = True
                    low -= 1
                    
                
                maxLen = max(maxLen, highLen + lowLen + 1)
        return maxLen
        
        
        
sol = Solution()        
nums = [100, 4, 200, 1, 3, 2]
print sol.longestConsecutive(nums)
        
        
        
        
        
        
        
        
        
        