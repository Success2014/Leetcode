# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 21:10:43 2015

Given an array of integers, find out whether there are two distinct 
indices i and j in the array such that the difference between nums[i]
 and nums[j] is at most t and the difference between i and j is at most k.

http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
https://leetcode.com/discuss/38176/python-ordereddict

如果： | nums[i] - nums[j] | <= t   式a
等价： | nums[i] / t - nums[j] / t | <= 1   式b
推出： | floor(nums[i] / t) - floor(nums[j] / t) | <= 1   式c
​等价： floor(nums[j] / t) ∈ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 式d
其中式b是式c的充分非必要条件，因为逆否命题与原命题等价，所以：

如果： floor(nums[j] / t) ∉ {floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1} 非d
推出： | nums[i] - nums[j] | > t   非a
因此只需要维护一个大小为k的窗口（字典）numDict，其中键为nums[i] / t，值为nums[i]。

遍历数组nums时，检查nums[i]与键集{floor(nums[i] / t) - 1, floor(nums[i] / t), floor(nums[i] / t) + 1}
对应的值的差值即可。


@author: Neo
"""
import collections
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0 or k < 1:
            return False
        dic = collections.OrderedDict()
        for i in xrange(len(nums)):
            key = nums[i] / t if t else nums[i] # if t=0, just nums[i]
            for j in (key - 1, key, key + 1): # check if there's number within this range
                if (j in dic) and abs(dic[j] - nums[i]) <= t: # integer division could bring error, so need to check abs(dic[j] - nums[i]) <= t
                    return True
            
            if len(dic) == k:
                dic.popitem(last=False)
                
            dic[key] = nums[i]
        return False


sol = Solution()
#print sol.containsNearbyAlmostDuplicate([1,5,8,9,12],3,2)        
print sol.containsNearbyAlmostDuplicate([-1,-1],1,0)        
        
        
        