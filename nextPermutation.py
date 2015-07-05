# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 17:15:57 2015

Implement next permutation, which rearranges numbers into the lexicographically 
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible 
order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its 
corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


1. 从尾部往前搜索，先找到第一个下降的数字，标记之。
例子： 12431， 则我们找到的是 2
2. 还是从尾往前搜索，找到第一个比2大的数字 ，交换之。
12431 --> 13421
由于从后往前一直到2都是升序的，所以第一个比2的数就是最小的比2大的数。
3. 将421进行反序。这样我们可以得到一个高位增加后的最小的后续值
13421 --> 13124
同样由于从后往前一直到这个位置都是升序的，所以翻转一下肯定是最小的数。

@author: Neo
"""

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):        
        n = len(nums)
        if n > 1:
            p = -1
            for i in xrange(n-1, 0, -1):
                if nums[i] > nums[i-1]:
                    p = i - 1 # # Find the largest i such that num[i] < num[i + 1]
                    break
            
            if p >= 0:
                for i in xrange(n-1, 0, -1):
                    if nums[i] > nums[p]:# Find the largest l such that num[p] < num[l] (if p exists)
                        q = i
                        break
                nums[p], nums[q] = nums[q], nums[p]
            # reverse all the numbers after pth position
            t = n - 1
            p += 1
            while p < t:
                nums[p], nums[t] = nums[t], nums[p]
                p += 1
                t -= 1
        
        return nums


sol = Solution()        
print sol.nextPermutation([1,2,4,3,1])
print sol.nextPermutation([1,1])      
print sol.nextPermutation([4,3,2,1])      
print sol.nextPermutation([1,2])        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        