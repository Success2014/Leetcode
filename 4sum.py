# -*- coding: utf-8 -*-
"""
Created on Mon Jul 06 13:28:09 2015

Given an array S of n integers, are there elements a, b, c, and d in S 
such that a + b + c + d = target? Find all unique quadruplets in the 
array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

Tags:  Array Hash Table Two Pointers
Similar Problems: (M) Two Sum (M) 3Sum

需要用到哈希表的思路，这样可以空间换时间，以增加空间复杂度的代价来降低时间复杂度。
首先建立一个字典dict，字典的key值为数组中每两个元素的和，每个key对应的value为这两
个元素的下标组成的元组，元组不一定是唯一的。如对于num=[1,2,3,2]来说，
dict={3:[(0,1),(0,3)], 4:[(0,2),(1,3)], 5:[(1,2),(2,3)]}。这样就可以检查
target-key这个值在不在dict的key值中，如果target-key在dict中并且下标符合要求，
那么就找到了这样的一组解。由于需要去重，这里选用set()类型的数据结构，
即无序无重复元素集。最后将每个找出来的解(set()类型)转换成list类型输出即可。


@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        d = {}
        res = set()
        for p in xrange(n):
            for q in xrange(p+1,n):
                if nums[p] + nums[q] not in d:
                    d[nums[p] + nums[q]] = [(p,q)]
                else:
                    d[nums[p] + nums[q]].append((p,q))
        for i in xrange(n):
            for j in xrange(i+1, n-2):
                if target - nums[i] - nums[j] in d:
                    for k in d[target - nums[i] - nums[j]]:
                        if k[0] > j:
                            res.add((nums[i],nums[j],nums[k[0]],nums[k[1]]))
        return [list(i) for i in res]
        
        
sol = Solution()
print sol.fourSum([1, 0, -1, 0, -2, 2],0)
        
        
        
        
        